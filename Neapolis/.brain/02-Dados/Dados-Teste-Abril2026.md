# Dados de Teste — Abril/2026

[[HOME|← Home]]

> Estes são os dados reais do mês de Abril/2026 extraídos dos PDFs.
> Usar para validar que o motor Python reproduz exatamente os mesmos resultados.

---

## Resultados por Unidade

| APTº | Água m³ | Água/Esgoto R$ | Gás m³ | Gás R$ | Rateio R$ | **Total R$** |
|------|---------|---------------|--------|--------|-----------|------------|
| COND | 18,457 | 236,41 | 0,000 | 0,00 | 0,00 | — |
| 201 | 21,886 | 281,88 | 0,000 | 0,00 | 462,74 | **745** |
| 202 | 16,763 | 215,24 | 2,741 | 103,82 | 462,74 | **782** |
| 301 | 19,759 | 253,65 | 4,059 | 153,73 | 462,74 | **871** |
| 302 | 19,988 | 256,59 | 2,429 | 92,00 | 462,74 | **812** |
| 401 | 25,559 | 329,05 | 1,414 | 53,56 | 462,74 | **846** |
| 402 | 23,777 | 305,87 | 4,820 | 182,56 | 462,74 | **952** |
| 501 | 25,421 | 326,78 | 1,213 | 45,94 | 462,74 | **836** |
| 502 | 13,441 | 173,17 | 1,029 | 38,97 | 462,74 | **675** |
| 601 | 3,979 | 50,68 | 0,582 | 22,04 | 462,74 | **536** |
| 602 | 0,682 | 8,79 | 0,130 | 4,92 | 462,74 | **477** |
| 701 | 13,458 | 173,29 | 0,785 | 29,73 | 462,74 | **666** |
| 702 | 7,190 | 91,93 | 3,761 | 142,45 | 462,74 | **698** |
| 801 | 4,531 | 58,51 | 0,423 | 16,02 | 462,74 | **538** |
| 802 | 14,109 | 181,86 | 2,440 | 92,42 | 462,74 | **738** |

---

## Despesas e Rateio

```
Total Despesas Abril/2026: R$ 4.065,65

Rateio:
  Parcial  = ROUND(4065,65 / 14, 2) = 290,40
  Síndico  = ROUND(290,40 / 13, 2)  = 22,34
  Fundo    = 150,00
  FINAL    = 290,40 + 22,34 + 150,00 = 462,74
```

---

## Fundo de Reserva

```
Saldo Abril/2026: R$ 40.130,60
```

---

## Como Usar nos Testes

```python
# Exemplo de teste de regressão
def test_total_ap201():
    resultado = calc_total(
        agua_esgoto=Decimal("281.88"),
        gas=Decimal("0.00"),
        rateio=Decimal("462.74")
    )
    assert resultado == Decimal("745")

def test_total_ap402():
    resultado = calc_total(
        agua_esgoto=Decimal("305.87"),
        gas=Decimal("182.56"),
        rateio=Decimal("462.74")
    )
    assert resultado == Decimal("952")
```

---

## Observações

- AP 201: gás = 0,00 em Abril/2026 (zero consumo ou piscina fechada?)
- AP 602: consumo de água extremamente baixo (0,682 m³) — unidade possivelmente desocupada
- Confirmar com Robson se os dados de Abril/2026 são os mais recentes disponíveis
