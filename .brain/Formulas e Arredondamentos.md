# Fórmulas e Arredondamentos — Referência Crítica

> Reproduzir **exatamente** estes arredondamentos é o critério #1 de sucesso do projeto.

## Mapa de Arredondamentos

| Operação | Função Excel | Decimais | Python Decimal |
|---|---|---|---|
| % consumo por unidade | `ROUND(x, 3)` | 3 | `ROUND_HALF_UP` |
| Consumo arredondado | `ROUND(x, 3)` | 3 | `ROUND_HALF_UP` |
| Custo água/esgoto/unidade | `ROUNDDOWN(x, 2)` | 2 truncado | `ROUND_DOWN` |
| Custo gás/unidade | `ROUND(x, 2)` | 2 | `ROUND_HALF_UP` |
| Custo/m³ água (COPASA) | `ROUND(x, 2)` | 2 | `ROUND_HALF_UP` |
| Rateio parcial (total/14) | `ROUND(x, 2)` | 2 | `ROUND_HALF_UP` |
| Rateio síndico (RP/13) | `ROUND(x, 2)` | 2 | `ROUND_HALF_UP` |
| **Total a pagar** | **`ROUNDUP(x, 0)`** | **0 (inteiro)** | **`ROUND_CEILING` / `math.ceil`** |

## Fórmulas Consolidadas

### Consumo
```python
consumo = leitura_atual - leitura_anterior
pct_consumo = round(consumo / total_copasa, 3)  # ROUND 3
consumo_cond = total_copasa - sum(consumos_individuais)
```

### Água e Esgoto
```python
custo_m3 = round(valor_total_agua / consumo_total, 2)  # ROUND 2
# Fórmula X5 da planilha:
custo_agua_unidade = rounddown(consumo_m3 * preco_m3 + (esgoto + recurso) * pct, 2)
custo_agua_cond = round(total_conta - sum(custos_individuais), 2)  # residual
```

### Gás
```python
volume_m3 = kg / 2.5  # fator fixo
custo_m3_gas = preco_kg * 2.5  # equivalente
custo_gas_unidade = round(consumo_m3 * custo_m3, 2)  # ROUND 2
# AP 201 especial:
custo_gas_201 = round((gas_apt + gas_piscina) * custo_m3, 2)
```

### Rateio
```python
rateio_parcial = round(total_despesas / 14, 2)     # ROUND 2
rateio_sindico = round(rateio_parcial / 13, 2)     # ROUND 2
fundo_reserva = Decimal("150.00")                   # configurável
rateio_final = rateio_parcial + rateio_sindico + fundo_reserva
```

### Total Final
```python
total_exato = custo_agua + custo_gas + rateio_final
total_pagar = math.ceil(total_exato)  # ROUNDUP → SEM CENTAVOS
```

### Verificação
```python
diferenca = total_a_ratear - sum(totais_calculados)
assert diferenca == 0  # DEVE ser zero
```

## Referências de Células Importantes

| Referência | Célula | Aba | Significado |
|---|---|---|---|
| "cg10" | CG10 | MEDICOES E COPASA HISTORICO | Custo/m³ de gás |
| "f105" | F105 | VRS. DEVIDOS E OUTROS | Rateio final mensal |
| BC43 | BC43 | MEDICOES E TABELAS | Preço/m³ água |
| BD43 | BD43 | MEDICOES E TABELAS | Valor esgoto |
| BE43 | BE43 | MEDICOES E TABELAS | Valor recurso hídrico |
| AY43 | AY43 | MEDICOES E TABELAS | Consumo total COPASA m³ |
| AZ43 | AZ43 | MEDICOES E TABELAS | Valor total conta COPASA |

## Validação com Dados Reais (Abril/2026)

Todos os cálculos foram validados em Python e bateram 100%:
- Rateio final = R$ 462,74 ✓
- Todos os 14 APs: ROUNDUP bateu com PDF ✓
- Fundo reserva: R$ 40.130,60 ✓

Ver [[Dados de Teste Abril 2026]] para tabela completa.

---
**Tags**: #formulas #arredondamento #critico #referencia
