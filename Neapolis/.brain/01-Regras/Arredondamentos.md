# Arredondamentos — Mapeamento Completo

[[HOME|← Home]]

> **CRÍTICO**: Os arredondamentos devem ser idênticos ao Excel.
> Um `ROUND` onde deveria ser `ROUNDDOWN` produz resultados errados.

---

## Tabela de Referência

| Operação | Função Excel | Casas | Comportamento |
|----------|-------------|-------|---------------|
| % consumo por unidade | `ROUND(x, 3)` | 3 | Arredondamento normal |
| Custo água/esgoto por unidade | `ROUNDDOWN(x, 2)` | 2 | **TRUNCA** (não arredonda) |
| Custo gás por unidade | `ROUND(x, 2)` | 2 | Arredondamento normal |
| Custo/m³ água (COPASA) | `ROUND(x, 2)` | 2 | Arredondamento normal |
| Rateio parcial (total/14) | `ROUND(x, 2)` | 2 | Arredondamento normal |
| Rateio síndico (RP/13) | `ROUND(x, 2)` | 2 | Arredondamento normal |
| **Total a pagar** | **`ROUNDUP(x, 0)`** | **0** | **Arredonda PARA CIMA ao inteiro** |

---

## Implementação Python

```python
from decimal import Decimal, ROUND_HALF_UP, ROUND_DOWN, ROUND_UP

def excel_round(value: Decimal, decimals: int) -> Decimal:
    """Equivalente ao ROUND() do Excel."""
    quantize_str = Decimal(10) ** -decimals
    return value.quantize(quantize_str, rounding=ROUND_HALF_UP)

def excel_rounddown(value: Decimal, decimals: int) -> Decimal:
    """Equivalente ao ROUNDDOWN() do Excel — TRUNCA."""
    quantize_str = Decimal(10) ** -decimals
    return value.quantize(quantize_str, rounding=ROUND_DOWN)

def excel_roundup(value: Decimal, decimals: int) -> Decimal:
    """Equivalente ao ROUNDUP() do Excel — arredonda PARA CIMA."""
    quantize_str = Decimal(10) ** -decimals
    return value.quantize(quantize_str, rounding=ROUND_UP)
```

---

## Armadilhas Comuns

1. **Nunca usar `float`** — ponto flutuante tem erros de precisão
2. **`ROUNDDOWN` ≠ `round()`** — Python `round()` usa ROUND_HALF_EVEN (bancário)
3. **`ROUNDUP` arredonda para cima SEMPRE** — `1.001` vira `2` com `ROUNDUP(x, 0)`
4. **Entradas do Excel** — ao importar, converter strings com vírgula decimal para `Decimal`

---

## Exemplo Verificado (Abril/2026)

```
AP 201 — Água:
  consumo = 21.886 m³
  pct = ROUND(21.886 / 209.543, 3) = ROUND(0.10444..., 3) = 0.104
  custo = ROUNDDOWN(21.886 * preco_m3 + esgoto_total * 0.104, 2) = 281.88

Rateio Abril/2026:
  total_despesas = 4.065,65
  parcial = ROUND(4065.65 / 14, 2) = ROUND(290.403..., 2) = 290.40
  sindico = ROUND(290.40 / 13, 2) = ROUND(22.338..., 2) = 22.34
  fundo = 150.00
  final = 290.40 + 22.34 + 150.00 = 462.74

AP 201 — Total:
  total = ROUNDUP(281.88 + 0.00 + 462.74, 0) = ROUNDUP(744.62, 0) = 745
```
