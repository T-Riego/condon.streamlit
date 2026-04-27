# Critérios de Sucesso (Aceitação)

[[HOME|← Home]]

---

## Critérios Funcionais

O sistema será considerado funcional quando, para **qualquer mês processado**:

| # | Critério | Tolerância |
|---|---------|-----------|
| 1 | Consumo calculado de cada AP = consumo na planilha Excel | Diferença = 0 |
| 2 | Custo água/esgoto de cada AP = valor na planilha | Diferença ≤ R$ 0,01 |
| 3 | Custo gás de cada AP = valor na planilha | Diferença = 0 |
| 4 | Rateio final = valor na planilha | Diferença = 0 |
| 5 | Total a pagar de cada AP = valor na planilha | Diferença = 0 |
| 6 | Soma dos totais + fundo reserva = total da competência | Diferença = 0 |
| 7 | PDF gerado é visualmente idêntico ao atual | Aprovação do Robson |
| 8 | Recibo PDF contém valor correto por extenso em português | Aprovação do Robson |

---

## Dados de Validação

Usar **Abril/2026** como conjunto de dados de teste primário:
→ Ver [[../02-Dados/Dados-Teste-Abril2026]]

---

## Teste de Regressão Sugerido

```python
# tests/test_abril2026.py

EXPECTED = {
    201: {"agua_esgoto": Decimal("281.88"), "gas": Decimal("0.00"), "total": Decimal("745")},
    202: {"agua_esgoto": Decimal("215.24"), "gas": Decimal("103.82"), "total": Decimal("782")},
    301: {"agua_esgoto": Decimal("253.65"), "gas": Decimal("153.73"), "total": Decimal("871")},
    302: {"agua_esgoto": Decimal("256.59"), "gas": Decimal("92.00"), "total": Decimal("812")},
    401: {"agua_esgoto": Decimal("329.05"), "gas": Decimal("53.56"), "total": Decimal("846")},
    402: {"agua_esgoto": Decimal("305.87"), "gas": Decimal("182.56"), "total": Decimal("952")},
    501: {"agua_esgoto": Decimal("326.78"), "gas": Decimal("45.94"), "total": Decimal("836")},
    502: {"agua_esgoto": Decimal("173.17"), "gas": Decimal("38.97"), "total": Decimal("675")},
    601: {"agua_esgoto": Decimal("50.68"), "gas": Decimal("22.04"), "total": Decimal("536")},
    602: {"agua_esgoto": Decimal("8.79"), "gas": Decimal("4.92"), "total": Decimal("477")},
    701: {"agua_esgoto": Decimal("173.29"), "gas": Decimal("29.73"), "total": Decimal("666")},
    702: {"agua_esgoto": Decimal("91.93"), "gas": Decimal("142.45"), "total": Decimal("698")},
    801: {"agua_esgoto": Decimal("58.51"), "gas": Decimal("16.02"), "total": Decimal("538")},
    802: {"agua_esgoto": Decimal("181.86"), "gas": Decimal("92.42"), "total": Decimal("738")},
}
```

---

## Verificação de Soma (Conferência)

```python
soma_totais = sum(ap["total"] for ap in EXPECTED.values())
# soma_totais deve ser igual ao total_a_ratear da competência
```
