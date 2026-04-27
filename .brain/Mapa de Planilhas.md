# Mapa de Planilhas Analisadas

> Índice de todas as planilhas do sistema atual com contagem de fórmulas e função.

## Planilha Principal: Planilhas mensais 202508 em diante RASCUNHO EM USO.xlsx

| Aba | Fórmulas | Complexidade | Nota |
|---|---|---|---|
| [[Planilha - MEDICOES E TABELAS\|MEDICOES E TABELAS]] | 825 | Alta | Motor central — Tabelas 1, 2 e 3 |
| [[Planilha - VRS DEVIDOS E OUTROS\|VRS. DEVIDOS E OUTROS]] | 603 | Alta | Valores devidos, rateio, AP 801, fundo reserva |
| [[Planilha - LANCTºS\|LANCTºS]] | 213 | Média | Despesas mensais com 12 períodos |
| [[Planilha - PLAN P COND\|PLAN P COND]] | 102 | Baixa | Documento enviado aos condôminos |
| MEDICOES E COPASA HISTORICO | 289 | Média | Histórico de leituras e tarifas COPASA |
| ORIENTACOES E CONF. | 7 | Baixa | Checklist (7 validações cruzadas CONFERIDO/PENDENTE) |
| DADOS DO PAGTº | 0 | — | Puro data entry (PIX, datas, recibos) |
| COPIAR PLAN P COND P TODAS | 5 | — | Template para cópia individual |

**Total: ~2.044 fórmulas na planilha principal**

## Outras Planilhas

| Arquivo | Fórmulas | Função |
|---|---|---|
| [[Planilha - AGUA E GAS LEITURAS\|ÁGUA E GÁS LEITURAS.xlsx]] | ~60 | Staging/sync de leituras do celular |
| [[Planilha - Recibos\|Recibos 202511 em diante.xlsm]] | 72 + VBA | 17 recibos com macro Extenso() |
| [[Planilha - Historico Condom\|Planilha p condôm 202302 em diante.xlsx]] | ~50 | Compilação mensal (39 meses) |
| Adm.xlsx | ? | **CRIPTOGRAFADO** — senha necessária |

## Cadeia de Dependências

```
AGUA E GAS LEITURAS (staging celular)
       ↓
MEDICOES E TABELAS ←→ LANCTºS ←→ VRS. DEVIDOS E OUTROS
       ↓
PLAN P COND (saída PDF)
       ↓
Recibos (.xlsm — 17 modelos)
       ↓
ORIENTACOES E CONF. (7 checks finais)
```

---
**Tags**: #planilhas #analise #mapa
