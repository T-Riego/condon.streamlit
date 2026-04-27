# Fórmulas Críticas

[[HOME|← Home]]

> Estas fórmulas devem ser reproduzidas **com precisão exata** no Python.
> Qualquer desvio resultará em valores diferentes da planilha real.

---

## Consumo Individual

```python
consumo = leitura_atual - leitura_anterior
```

---

## Percentual de Consumo (para esgoto)

```python
pct_consumo = ROUND(consumo_unidade / consumo_total_copasa, 3)
```
- Base: total medido pela COPASA (não soma individual)
- Arredondado em 3 casas decimais

---

## Custo Água/Esgoto por Unidade

```python
custo_agua = ROUNDDOWN(
    consumo_m3 * preco_m3 + (esgoto + recurso_hidrico) * pct_consumo,
    2
)
```
- `ROUNDDOWN` → trunca (não arredonda normalmente)
- Precisão: 2 casas decimais

---

## Consumo Condominial (Residual)

```python
consumo_cond = total_copasa - SUM(consumos_individuais)
# Áreas comuns: corredor, garagem, jardim, etc.
```

---

## Custo Gás

```python
custo_gas = ROUND(consumo_gas_m3 * custo_gas_m3, 2)

# AP 201 — especial (inclui piscina)
custo_gas_201 = ROUND((gas_apt + gas_piscina) * custo_gas_m3, 2)

# Conversão kg → m³
volume_m3 = quantidade_kg / 2.5
```

---

## Rateio de Despesas

```python
rateio_parcial = ROUND(total_despesas / 14, 2)   # divide por 14 unidades
rateio_sindico = ROUND(rateio_parcial / 13, 2)    # síndico não paga pra si
fundo_reserva = 150.00                             # valor variável (conferir mensalmente)

rateio_final = rateio_parcial + rateio_sindico + fundo_reserva
```

---

## Total a Pagar (Tabela 3)

```python
total = ROUNDUP(custo_agua + custo_gas + rateio_final, 0)
# SEM CENTAVOS — sempre arredonda PARA CIMA ao inteiro
```

---

## Verificação Obrigatória

```python
diferenca = total_a_ratear - soma_calculada
# DEVE ser exatamente 0.00 — se não for, há erro nos cálculos
```

---

## Implementação Python (módulos planejados)

| Fórmula | Módulo |
|---------|--------|
| ROUND, ROUNDDOWN, ROUNDUP | `arredondamentos.py` |
| Consumo + % + custo água | `calc_agua.py` |
| Consumo + custo gás | `calc_gas.py` |
| Rateio parcial, síndico, fundo | `calc_rateio.py` |
| Total final + verificação | `calc_total.py` |

> Use `decimal.Decimal` em Python — **nunca `float`** para operações financeiras.
