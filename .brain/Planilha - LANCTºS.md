# LANCTºS — Lançamento de Despesas

> **213 fórmulas**. Despesas mensais com 12 períodos (Mai/2025 → Abr/2026).

## Estrutura

Linhas 3-34: itens de despesa. Cada período tem 4 colunas: REF data, VALOR, DATA pagamento, INFORMAR NA PLAN. (sim/não).

## Itens de Despesa

| Linha | Descrição |
|---|---|
| 3 | Conservadora Campos de Oliveira |
| 4 | Manutenção Elevador - ThyssenKrupp |
| 5 | Conta de água COPASA (link automático) |
| 6 | Conta de luz CEMIG |
| 7 | Retenções federais/municipais |
| 8 | Seguro do prédio |
| 9-23 | Diversos (limpeza, reparos, gás, síndico, internet câmeras...) |
| 24 | Conta água total (link a MEDICOES E TABELAS) |
| 33 | Consumo total água (link a MEDICOES E TABELAS) |
| 34 | Fundo de reserva (carrega mês anterior) |

## Fórmulas-chave

### Links automáticos com outras abas
```excel
# Conta água (linha 5)
C5 = 'VRS. DEVIDOS E OUTROS'!C4    (meses iniciais)
AU5 = 'MEDICOES E TABELAS'!AQ43    (meses recentes)

# Conta água total (linha 24)
AU24 = 'MEDICOES E TABELAS'!AZ43

# Consumo total (linha 33)
AU33 = 'MEDICOES E TABELAS'!AS43

# Fundo reserva (linha 34) — carrega do mês anterior
G34 = C34, K34 = G34, ..., AU34 = AQ34
```

### Totais
```excel
C37 = SUM(C3:C23)     # total despesas do mês
AQ38 = AQ37 = 'PLAN P COND'!G27    # verificação cruzada
```

### Validação por linha (linhas 46-80)
```excel
A46 = SUM(B3:AY3) = SUM(B46:AY46)    # boolean check
AZ3 = A3 = AY3    # descrição bate com canonical
```

## Referências
- Puxa de: [[Planilha - MEDICOES E TABELAS]] (contas água, consumo)
- Puxa de: [[Planilha - VRS DEVIDOS E OUTROS]] (custos água iniciais)
- Alimenta: [[Planilha - VRS DEVIDOS E OUTROS]] (totais para rateio)
- Alimenta: [[Planilha - PLAN P COND]] (verificação G27)

---
**Tags**: #planilha #despesas #formulas
