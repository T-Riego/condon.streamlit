# Fluxo Mensal — 8 Etapas

[[HOME|← Home]]

## Visão Geral

O ciclo mensal acontece entre os dias **27-29 do mês corrente** e inclui:

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

---

## Etapas Detalhadas

### Etapa 1 — Coleta de Leituras (dias 27-29)
- Robson lê fisicamente os 15 medidores de água e 15 de gás
- AP 201 tem **2 medidores de água** (unidade + piscina)
- Dados entram em `AGUA E GAS LEITURAS.xlsx` (staging/sync)

### Etapa 2 — Tabela 1: Consumo
```python
consumo = leitura_atual - leitura_anterior
```
- Calculado por unidade para água e gás

### Etapa 3 — Cálculo Água/COPASA
```python
custo_por_m3 = total_conta_copasa / consumo_total_m3
```
- Conta COPASA traz: valor total, m³ totais, valor esgoto, valor recurso hídrico

### Etapa 4 — Esgoto Proporcional
```python
pct_consumo = ROUND(consumo_unidade / consumo_total_copasa, 3)
custo_agua_unidade = ROUNDDOWN(consumo_m3 * preco_m3 + (esgoto + recurso_hidrico) * pct_consumo, 2)
```

### Etapa 5 — Cálculo Gás
```python
# Conversão: kg comprados → m³
volume_m3 = quantidade_kg / 2.5

# Custo por unidade
custo_gas = ROUND(consumo_gas_m3 * custo_gas_m3, 2)

# AP 201 (especial — inclui piscina)
custo_gas_201 = ROUND((gas_apt + gas_piscina) * custo_gas_m3, 2)
```

### Etapa 6 — Tabela 2: Consolidação
- Água + Esgoto + Gás por unidade
- **Consumo condominial (residual)**:
```python
consumo_cond = total_copasa - SUM(consumos_individuais)
```

### Etapa 7 — Lançamento Despesas
- NFs de serviços, retenções, seguro, salário do síndico, fundo de reserva
- Ver [[Formulas-Criticas#Rateio de Despesas]]

### Etapa 8 — Tabela 3: Total Final
```python
total = ROUNDUP(custo_agua + custo_gas + rateio_final, 0)  # SEM CENTAVOS
```
- **Verificação obrigatória**: `total_a_ratear - soma_calculada = 0`

---

## Saídas do Fluxo

1. **3 PDFs de planilha** (geral, AP 201, AP 601) — ver [[Casos-Especiais]]
2. **17 recibos PDF** — ver [[Casos-Especiais#Recibos]]
3. **Checklist conferido** na aba `ORIENTACOES E CONF.`
