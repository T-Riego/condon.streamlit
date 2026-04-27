# Projeto ADM Condomínio Neápolis

## Visão Geral
Sistema para administração do **Condomínio Residencial Neápolis** em Belo Horizonte/MG.
- CNPJ: 09.408.714/0001-08
- Banco Inter, AG 0001, CC 26620410-4, PIX = CNPJ
- **14 apartamentos** em **8 andares**: 201, 202, 301, 302, 401, 402, 501, 502, 601, 602, 701, 702, 801, 802
- **15 medidores** de água (AP 201 tem 2: unidade + piscina) + 15 medidores de gás
- Administrador principal: Robson (síndico)
- Desenvolvedor: Tiago (@tiagoriegos2)

## Objetivo
Substituir o sistema atual baseado em planilhas Excel por uma aplicação web/mobile que reproduza **exatamente** os mesmos cálculos, arredondamentos e resultados das planilhas existentes.

## Arquitetura de Referência (Planilhas Atuais)

### Planilhas Fonte
1. **ÁGUA E GÁS LEITURAS.xlsx** — Leituras brutas dos medidores (staging/sync)
2. **Planilhas mensais 202508 em diante RASCUNHO EM USO.xlsx** — Planilha principal com 8 abas:
   - `ORIENTACOES E CONF.` — Checklist de verificação (7 fórmulas de validação cruzada)
   - `MEDICOES E COPASA HISTORICO` — Histórico de leituras e contas COPASA (289 fórmulas)
   - `MEDICOES E TABELAS` — **Motor central de cálculos** (825 fórmulas) — Tabelas 1, 2 e 3
   - `LANCTºS` — Lançamento de despesas mensais (213 fórmulas)
   - `VRS. DEVIDOS E OUTROS` — Valores devidos, rateio, AP 801, fundo de reserva (603 fórmulas)
   - `DADOS DO PAGTº` — Dados de pagamento (puro data entry, sem fórmulas)
   - `PLAN P COND` — Planilha enviada aos condôminos (102 fórmulas)
   - `COPIAR PLAN P COND P TODAS` — Template para cópia (5 fórmulas)
3. **Planilha p condôm 202302 em diante.xlsx** — Compilação de todas as planilhas mensais enviadas
4. **Recibos 202511 em diante.xlsm** — 17 abas de recibos com macro VBA `Extenso()` (valor por extenso)
5. **Adm.xlsx** — Administração (criptografado, senha necessária)

### Fluxo Mensal (8 Etapas)
1. **Coleta de Leituras** (dias 27-29 do mês) → medidores de água e gás
2. **Tabela 1** — Consumo = leitura_atual - leitura_anterior
3. **Cálculo Água/COPASA** — custo/m³ = total_conta / consumo_total
4. **Esgoto Proporcional** — regra de 3: %_unidade = consumo_agua_unidade / soma_individual
5. **Cálculo Gás** — conversão: m³ = kg / 2.5; custo_unidade = consumo × custo/m³
6. **Tabela 2 (Consolidação)** — Água + Esgoto + Gás por unidade + Condomínio (residual)
7. **Lançamento Despesas** — NFs, retenções, seguro, síndico, fundo reserva
8. **Tabela 3 (Final)** — TOTAL = ROUNDUP(água_esgoto + gás + rateio, 0) → sem centavos

### Fórmulas Críticas (devem ser reproduzidas com precisão)

```python
# Consumo individual
consumo = leitura_atual - leitura_anterior

# Percentual de consumo (para esgoto)
pct_consumo = ROUND(consumo_unidade / consumo_total_copasa, 3)

# Custo água/esgoto por unidade
custo_agua = ROUNDDOWN(consumo_m3 * preco_m3 + (esgoto + recurso_hidrico) * pct_consumo, 2)

# Consumo condominial (residual)
consumo_cond = total_copasa - SUM(consumos_individuais)

# Custo gás
custo_gas = ROUND(consumo_gas_m3 * custo_gas_m3, 2)
# AP 201 especial: custo_gas_201 = ROUND((gas_apt + gas_piscina) * custo_gas_m3, 2)

# Rateio despesas
rateio_parcial = ROUND(total_despesas / 14, 2)
rateio_sindico = ROUND(rateio_parcial / 13, 2)
fundo_reserva = 150.00  # variável
rateio_final = rateio_parcial + rateio_sindico + fundo_reserva

# Total a pagar
total = ROUNDUP(custo_agua + custo_gas + rateio_final, 0)  # SEM CENTAVOS

# Verificação (DEVE = 0)
diferenca = total_a_ratear - soma_calculada
```

### Casos Especiais
- **AP 201**: 2 medidores (unidade + piscina gas), desconto de internet (R$65 quando aplicável)
- **AP 601**: Pagamento separado — condomínio para um dono, fundo de reserva para outro (Gilberto Augusto Beltrão)
- **AP 801**: Controle de saldo acumulado (Alberto Jacomini de Souza)
- **Síndico**: Rateio parcial entre 13 unidades (não paga para si mesmo)
- **Lucas e Clara**: Recebem planilhas com informações personalizadas

### 3 Tipos de Planilha de Saída (PDF)
1. **Planilha Geral** — Todos os dados, sem notas especiais
2. **Planilha AP 201** — Mesma + nota "DESCONTAR A INTERNET DE R$ 65,00"
3. **Planilha AP 601** — Mesma + nota "DESCONTAR O VALOR DO FUNDO DE RESERVA DE R$ 150,00" + "VALOR A PAGAR PARA O CONDOMÍNIO: R$ XXX,00"

### Recibos (17 modelos)
- 11 recibos padrão (201-702): puxam de MEDICOES E TABELAS
- 2 recibos AP 601: separados COND e FRESERV (donos diferentes)
- 1 recibo AP 801: com saldo acumulado (puxa de VRS. DEVIDOS E OUTROS)
- 3 templates "NÃO USAR" (modelos de referência)
- Macro VBA `Extenso()`: converte valor monetário para português por extenso

## Stack Recomendada
- **Fase 1 (MVP)**: Streamlit + SQLite + Python (ReportLab para PDFs)
- **Fase 2 (Produção)**: Next.js (PWA) + FastAPI + PostgreSQL

## Estrutura do Projeto (planejada)
```
/src
  /core          # Motor de cálculos (Python) — reusável entre Fase 1 e 2
    calc_agua.py
    calc_gas.py
    calc_rateio.py
    calc_total.py
    arredondamentos.py
  /models         # Modelos de dados (SQLAlchemy/Prisma)
  /api            # FastAPI endpoints (Fase 2)
  /frontend       # Next.js (Fase 2)
  /streamlit      # UI Streamlit (Fase 1)
  /pdf            # Geração de PDFs (planilhas + recibos)
  /import         # Importação de dados legados das planilhas
  /tests          # Testes com dados reais das planilhas
```

## Referências
- [[Anotacoes resumo reuniao obsidian]] — Notas da reunião de 83 min (26/04/2026)
- [[MD]] — Plano base gerado pelo ChatGPT (entidades, módulos, MVP)
- [[MD1]] — Complemento (fórmulas, regras de negócio, telas sugeridas)
- Dados para análise.zip — Planilhas originais, NFs, recibos
