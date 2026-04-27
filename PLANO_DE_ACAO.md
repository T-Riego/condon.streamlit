# Plano de Ação — Sistema ADM Condomínio Neápolis

**Data**: 26/04/2026
**Projeto**: Migração de planilhas Excel para sistema web/mobile
**Condomínio**: Residencial Neápolis — 14 unidades, 8 andares, BH/MG

---

## 1. Diagnóstico Completo das Planilhas

### O que foi analisado

Foram analisados **6 arquivos Excel** (1.940+ fórmulas), **3 PDFs de saída**, **1 macro VBA**, **3 arquivos MD** de reuniões e **1 arquivo de texto** da reunião gravada de 83 minutos.

### Mapa de Complexidade

| Planilha / Aba              | Fórmulas | Complexidade | Função                                         |
| --------------------------- | -------- | ------------ | ---------------------------------------------- |
| MEDICOES E TABELAS          | 825      | Alta         | Motor central — Tabelas 1, 2 e 3               |
| VRS. DEVIDOS E OUTROS       | 603      | Alta         | Valores devidos, rateio, AP 801, fundo reserva |
| MEDICOES E COPASA HISTORICO | 289      | Média        | Histórico de leituras e tarifas COPASA         |
| LANCTºS                     | 213      | Média        | Lançamento de despesas mensais                 |
| PLAN P COND                 | 102      | Baixa        | Planilha de saída para condôminos              |
| Recibos (.xlsm)             | 72 + VBA | Média        | 17 recibos com macro Extenso()                 |
| AGUA E GAS LEITURAS         | ~60      | Baixa        | Staging de leituras (sync celular)             |
| Planilha p condôm 202302+   | ~50      | Baixa        | Compilação histórica mensal                    |
| ORIENTACOES E CONF.         | 7        | Baixa        | Checklist de validação                         |

### Dependências entre Abas (cadeia crítica)

```
AGUA E GAS LEITURAS (staging)
    ↓
MEDICOES E TABELAS (Tabela 1: leituras → consumo)
    ↓ ↑
LANCTºS (despesas)  ←→  VRS. DEVIDOS E OUTROS (rateio)
    ↓
MEDICOES E TABELAS (Tabela 2: consolidação → Tabela 3: final)
    ↓
PLAN P COND (planilha para condôminos)
    ↓
Recibos (17 modelos PDF)
    ↓
ORIENTACOES E CONF. (7 validações cruzadas → CONFERIDO/PENDENTE)
```

### Arredondamentos Mapeados (CRÍTICO)

| Operação                      | Função Excel        | Precisão                               |
| ----------------------------- | ------------------- | -------------------------------------- |
| % consumo por unidade         | `ROUND(x, 3)`       | 3 decimais                             |
| Custo água/esgoto por unidade | `ROUNDDOWN(x, 2)`   | 2 decimais, truncado                   |
| Custo gás por unidade         | `ROUND(x, 2)`       | 2 decimais                             |
| Custo/m³ água (COPASA)        | `ROUND(x, 2)`       | 2 decimais                             |
| Rateio parcial (total/14)     | `ROUND(x, 2)`       | 2 decimais                             |
| Rateio síndico (RP/13)        | `ROUND(x, 2)`       | 2 decimais                             |
| **Total a pagar**             | **`ROUNDUP(x, 0)`** | **Sem centavos (arredonda PARA CIMA)** |

### Pendências Resolvidas pela Análise

| Pendência do MD.md              | Resolvido? | Resposta                                                                      |
| ------------------------------- | ---------- | ----------------------------------------------------------------------------- |
| Lista exata dos 14 apartamentos | Sim        | 201, 202, 301, 302, 401, 402, 501, 502, 601, 602, 701, 702, 801, 802          |
| Identificação de medidores      | Sim        | 15 água (201 tem 2), 15 gás (colunas C-Q nas planilhas)                       |
| Regra AP 201/piscina            | Sim        | 2 medidores: gás_201 = gas_apt + gas_piscina, água só 1 medidor               |
| Significado de "cg10"           | Sim        | Referência à célula CG10 na aba MEDICOES E COPASA HISTORICO — custo/m³ de gás |
| Significado de "f105"           | Sim        | Referência à célula F105 na aba VRS. DEVIDOS E OUTROS — rateio final mensal   |
| Fórmula do síndico              | Sim        | rateio_parcial = total/14; síndico = rateio_parcial/13                        |
| 3 tipos de planilha             | Sim        | Geral, AP 201 (desconto internet), AP 601 (desconto fundo + valor separado)   |
| Regra de não cobrar centavos    | Sim        | ROUNDUP(total, 0) — arredonda para cima ao inteiro                            |
| Modelo do recibo                | Sim        | 17 modelos, VBA Extenso(), ref. externa a MEDICOES E TABELAS                  |
| Lucas e Clara                   | Parcial    | Recebem planilhas personalizadas (Lucas = AP 201? Clara = AP 601?)            |
| Senha do Adm.xlsx               | Não        | Arquivo criptografado — senha necessária                                      |

---

## 2. Recomendação de Stack Tecnológica

### Por que NÃO as outras opções

**Canvas/Figma**: Ferramentas de design, não de desenvolvimento. Inúteis para cálculos financeiros.

**Kanban (Trello, Notion)**: Bom para gestão de tarefas, não para sistema com cálculos complexos e geração de PDFs. Poderia ser usado apenas para gerenciar o projeto de desenvolvimento.

**Streamlit puro (produção)**: Excelente para MVP e validação, mas tem limitações sérias para uso mobile em campo (leitura de medidores), UI pouco customizável, e não funciona offline.

**Next.js puro (sem Python)**: JavaScript não tem módulo Decimal nativo. Precision.js/Decimal.js existem, mas replicar os arredondamentos ROUNDDOWN/ROUNDUP do Excel em JS é propenso a erros sutis. Python é mais seguro para cálculos financeiros.

### Recomendação Final: Estrat��gia em 2 Fases

#### FASE 1 — MVP de Validação (4-6 semanas)

**Stack**: Python + Streamlit + SQLite + ReportLab

**Justificativa**:

- Python `decimal.Decimal` reproduz arredondamentos Excel com precisão
- Streamlit permite UI funcional em dias
- Teste lado-a-lado com planilhas reais (mesmo mês, mesmos dados = mesmos resultados)
- ReportLab gera PDFs com layout idêntico ao atual
- SQLite é suficiente para 14 unidades e zero infraestrutura extra
- Deploy via Streamlit Cloud (gratuito) ou Docker local

**Entregáveis da Fase 1**:

1. Motor de cálculos Python validado contra dados reais
2. Interface de entrada de dados (leituras, despesas, COPASA)
3. Geração de 3 planilhas PDF (geral, 201, 601)
4. Geração de recibos PDF com valor por extenso
5. Banco de dados com dados importados das planilhas históricas
6. Suite de testes automatizados (dados reais = resultado esperado)

#### FASE 2 — Aplicação de Produção (8-12 semanas)

**Stack**: Next.js (PWA) + FastAPI + PostgreSQL

**Justificativa**:

- PWA funciona no celular Android do Robson para leituras in loco
- Funciona offline (service worker + sync quando tiver internet)
- FastAPI reusa 100% do motor Python validado na Fase 1
- Next.js + Tailwind CSS = UI moderna e responsiva
- PostgreSQL para integridade, backup automático, auditoria
- Possibilidade de multi-condomínio no futuro

**Entregáveis da Fase 2**:

1. App web responsivo (PWA) para Android/desktop
2. Tela mobile para leitura de medidores (com lanterna ativada)
3. Dashboard com gráficos de consumo e histórico
4. Envio automático de PDFs por WhatsApp/email
5. Checklist interativo de conferência mensal
6. Controle de acesso (Robson admin, Tiago dev)
7. Backup automático PostgreSQL

---

## 3. Plano de Execução Detalhado

### FASE 1 — MVP

#### Sprint 1 (Semana 1-2): Motor de Cálculos

| #   | Tarefa                                                                                   | Prioridade |
| --- | ---------------------------------------------------------------------------------------- | ---------- |
| 1.1 | Criar módulo `calc_agua.py` — consumo individual, % proporcional, custo/m³, esgoto       | Alta       |
| 1.2 | Criar módulo `calc_gas.py` — conversão kg→m³, custo/m³, custo por unidade                | Alta       |
| 1.3 | Criar módulo `calc_rateio.py` — despesas/14, síndico/13, fundo reserva                   | Alta       |
| 1.4 | Criar módulo `calc_total.py` — consolidação + ROUNDUP sem centavos                       | Alta       |
| 1.5 | Criar módulo `arredondamentos.py` — funções ROUND, ROUNDDOWN, ROUNDUP idênticas ao Excel | Crítica    |
| 1.6 | Implementar casos especiais (AP 201, 601, 801)                                           | Alta       |
| 1.7 | Criar testes com dados reais de Abril/2026 (resultado esperado nos PDFs)                 | Crítica    |
| 1.8 | Validar: diferença entre cálculo Python e planilha = R$ 0,00 para todos os APs           | Crítica    |

#### Sprint 2 (Semana 3-4): Banco de Dados e Interface

| #   | Tarefa                                                                             | Prioridade |
| --- | ---------------------------------------------------------------------------------- | ---------- |
| 2.1 | Modelar banco SQLite (unidades, medidores, leituras, contas, despesas, pagamentos) | Alta       |
| 2.2 | Criar script de importação dos dados históricos (Feb/2023 → Abr/2026)              | Média      |
| 2.3 | Interface Streamlit: Dashboard (competência atual, status, pendências)             | Alta       |
| 2.4 | Interface Streamlit: Entrada de leituras (água + gás por AP)                       | Alta       |
| 2.5 | Interface Streamlit: Lançamento conta COPASA                                       | Alta       |
| 2.6 | Interface Streamlit: Lançamento despesas mensais                                   | Alta       |
| 2.7 | Interface Streamlit: Visualização Tabelas 1, 2, 3 consolidadas                     | Alta       |
| 2.8 | Interface Streamlit: Checklist de conferência                                      | Média      |

#### Sprint 3 (Semana 5-6): PDFs e Finalização

| #   | Tarefa                                                              | Prioridade |
| --- | ------------------------------------------------------------------- | ---------- |
| 3.1 | Gerar PDF "Planilha Geral" (layout idêntico ao atual)               | Alta       |
| 3.2 | Gerar PDF "Planilha AP 201" (com nota desconto internet)            | Alta       |
| 3.3 | Gerar PDF "Planilha AP 601" (com nota fundo reserva separado)       | Alta       |
| 3.4 | Gerar recibos PDF (17 modelos) com valor por extenso                | Alta       |
| 3.5 | Controle de pagamentos (data, forma, nº recibo, enviado)            | Média      |
| 3.6 | Histórico mensal (consulta por competência)                         | Média      |
| 3.7 | Teste final: gerar Abril/2026 completo e comparar com planilha real | Crítica    |
| 3.8 | Deploy MVP (Streamlit Cloud ou Docker local)                        | Média      |

### FASE 2 — Produção (após validação do MVP)

| Sprint | Foco                                                       | Duração   |
| ------ | ---------------------------------------------------------- | --------- |
| 4      | Setup Next.js + FastAPI + PostgreSQL + migração do SQLite  | 2 semanas |
| 5      | Frontend mobile-first (PWA): leituras, despesas, dashboard | 3 semanas |
| 6      | Geração de PDFs no backend + envio automático              | 2 semanas |
| 7      | Testes, deploy, treinamento do Robson                      | 2 semanas |

---

## 4. Modelo de Dados (proposto)

```
┌─────────────────┐     ┌──────────────────┐     ┌─────���────────────┐
│   Condominio     │     │ UnidadeHabitacional│    │    Morador       │
│─────────────────│     │──────────────────│     │──────────────────│
│ id               │────<│ condominio_id    │────<│ unidade_id       │
│ nome             │     │ numero (201-802) │     │ nome             │
│ cnpj             │     │ andar            │     │ cpf              │
│ banco_info       │     │ ativo            │     │ email            │
│ pix_key          │     │ participa_rateio │     │ telefone         │
└─────────────────┘     │ participa_sindico│     │ eh_pagador       │
                         │ observacoes      │     │ eh_sindico       │
                         └──────────────────┘     └──────────────────┘
                                  │
                    ┌─────────────┼─────────────┐
                    ▼                             ▼
          ┌────��─────────────┐          ┌───���──────────────┐
          │    Medidor       │          │  Competencia     │
          │──────────────────│          │───��──────────────│
          │ id               │          │ id               │
          │ unidade_id       │          │ ano_mes (202604) │
          │ tipo (agua/gas)  │          │ data_vencimento  │
          │ identificador    │          │ status (aberta/  │
          │ descricao        │          │   conferida/     │
          │ ativo            │          │   fechada)       │
          └──────────────────┘          │ oficio_numero    │
                    │                   └──────────────────┘
                    ▼                            │
          ┌──────────────────┐                   │
          │  Leitura         │                   │
          │──────────────────│                   │
          │ id               │                   │
          │ competencia_id   │◄──────────────────┘
          │ medidor_id       │
          │ data_medicao     │
          │ leitura_anterior │
          �� leitura_atual    │
          │ consumo_calculado│
          └────��─────────────┘

┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│  ContaCopasa     │  │  AbastecGas      │  │  Despesa         │
│──────────────────│  │──────────────────│  ���──────────────────│
│ competencia_id   │  │ data_compra      │  │ competencia_id   │
│ consumo_total_m3 │  │ quantidade_kg    │  │ descricao        │
│ valor_total      │  │ valor_total      │  │ valor            │
│ valor_agua       │  │ preco_por_kg     │  │ data_referencia  │
│ valor_esgoto     │  │ volume_m3        │  │ tipo             │
│ valor_recurso    │  │ custo_por_m3     │  │ rateavel         │
│ custo_por_m3     │  └─────��────────────┘  │ base_rateio (14  │
│ data_leitura     │                         │   ou 13)         │
│ data_vencimento  │                         │ informar_condom  │
└──────────────────┘                         └────���─────────────┘

┌──────────────────┐  ┌��──────────��──────┐  ┌──────────────────┐
│  ValorDevido     │  │   Pagamento      │  │  FundoReserva    │
│──────────────────│  │───��──────────────│  │──────────────────│
│ competencia_id   │  │ valor_devido_id  │  │ competencia_id   │
│ unidade_id       │  │ valor_pago       │  │ saldo_anterior   │
│ agua_consumo_m3  │  │ data_pagamento   │  │ entradas         │
│ agua_esgoto_r$   │  │ forma_pagamento  │  │ saidas           │
│ gas_consumo_m3   │  │ numero_recibo    │  │ saldo_final      │
│ gas_valor_r$     │  │ recibo_enviado   │  │ valor_por_unidade│
│ rateio_r$        │  │ nome_pagador     │  └────��─────────────┘
│ total_exato      │  │ doc_pagador      │
│ total_arredond   │  │ observacoes      │
│ observacoes      │  └──────────────────┘
└──────────────────┘
```

---

## 5. Critério de Sucesso (Aceitação)

O sistema será considerado funcional quando, para qualquer mês processado:

1. O consumo calculado de cada AP = consumo na planilha Excel (diferença = 0)
2. O custo de água/esgoto de cada AP = valor na planilha (diferença ≤ R$ 0,01)
3. O custo de gás de cada AP = valor na planilha (diferença = 0)
4. O rateio final = valor na planilha (diferença = 0)
5. O total a pagar de cada AP = valor na planilha (diferença = 0)
6. A soma dos totais + fundo reserva = total da competência
7. O PDF gerado é visualmente idêntico ao atual
8. O recibo PDF contém valor correto por extenso em português

### Dados de Teste (Abril/2026 — extraídos dos PDFs)

| APTº | Água m³ | Água/Esgoto R$ | Gás m³ | Gás R$ | Rateio R$ | Total R$ |
| ---- | ------- | -------------- | ------ | ------ | --------- | -------- |
| COND | 18,457  | 236,41         | 0,000  | 0,00   | 0,00      | 0,00     |
| 201  | 21,886  | 281,88         | 0,000  | 0,00   | 462,74    | 745,00   |
| 202  | 16,763  | 215,24         | 2,741  | 103,82 | 462,74    | 782,00   |
| 301  | 19,759  | 253,65         | 4,059  | 153,73 | 462,74    | 871,00   |
| 302  | 19,988  | 256,59         | 2,429  | 92,00  | 462,74    | 812,00   |
| 401  | 25,559  | 329,05         | 1,414  | 53,56  | 462,74    | 846,00   |
| 402  | 23,777  | 305,87         | 4,820  | 182,56 | 462,74    | 952,00   |
| 501  | 25,421  | 326,78         | 1,213  | 45,94  | 462,74    | 836,00   |
| 502  | 13,441  | 173,17         | 1,029  | 38,97  | 462,74    | 675,00   |
| 601  | 3,979   | 50,68          | 0,582  | 22,04  | 462,74    | 536,00   |
| 602  | 0,682   | 8,79           | 0,130  | 4,92   | 462,74    | 477,00   |
| 701  | 13,458  | 173,29         | 0,785  | 29,73  | 462,74    | 666,00   |
| 702  | 7,190   | 91,93          | 3,761  | 142,45 | 462,74    | 698,00   |
| 801  | 4,531   | 58,51          | 0,423  | 16,02  | 462,74    | 538,00   |
| 802  | 14,109  | 181,86         | 2,440  | 92,42  | 462,74    | 738,00   |

**Despesas Abril/2026**: Total = R$ 4.065,65
**Rateio**: Parcial = 290,40 | Síndico = 22,34 | Fundo = 150,00 | **Final = 462,74**
**Fundo Reserva**: Saldo = R$ 40.130,60

---

## 6. Próximos Passos Imediatos

1. **Confirmar stack** com Tiago (Streamlit MVP → Next.js produção)
2. **Obter senha** do Adm.xlsx para análise completa
3. **Confirmar** quem são Lucas e Clara (quais apartamentos?)
4. **Iniciar Sprint 1**: Motor de cálculos Python + testes com dados Abril/2026
5. **Configurar repositório Git** com estrutura do projeto
