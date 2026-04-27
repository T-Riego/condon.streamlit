# Planilha p Condôm 202302 em diante — Histórico

> **~50 fórmulas**. Compilação de 39 meses (Fev/2023 → Abr/2026).

## Estrutura

Aba **TODAS**: 3.393 linhas, blocos de ~87 linhas por mês.

Cada bloco mensal tem 2 seções:
1. **Lançamentos** — DATA | DESCRIÇÃO | VALOR (R$)
2. **Valores Devidos por Unidade** — APTº | COPASA consumo/valor | GÁS consumo/valor | RATEIO | TOTAL

## Evolução das Regras (descoberta na análise)

| Período | Divisor síndico | Fundo reserva |
|---|---|---|
| Fev-Mai/2023 | /14 (igual aos demais) | Não existia |
| Jun/2023 em diante | **/13** (síndico isento) | Não existia |
| Fev/2024 em diante | /13 | **R$300/AP/mês** |
| Posteriormente | /13 | **R$150/AP/mês** (atual) |

## Abas auxiliares
- **202508 VALIDA** — Versão final de Ago/2025
- **202508 INUTILIZADA** — Versão descartada (tarifa errada, custos água 3x maiores)

## Refs externas
```excel
D3210 = '[1]VRS. DEVIDOS E OUTROS'!I3286    # data
G3383 = '[1]VRS. DEVIDOS E OUTROS'!F3480    # saída fundo reserva
```

## 240+ merged cells (A:G) — headers, textos, blocos de pagamento.

---
**Tags**: #planilha #historico
