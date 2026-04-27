# Casos Especiais

[[HOME|← Home]]

---

## AP 201 — Dois Medidores + Desconto Internet

**Medidores**: 1 água (unidade), 2 gás (unidade + piscina)

```python
# Água: medidor único, cálculo normal
custo_agua_201 = ROUNDDOWN(consumo_m3 * preco_m3 + esgoto * pct, 2)

# Gás: soma dos dois medidores
custo_gas_201 = ROUND((gas_apt + gas_piscina) * custo_gas_m3, 2)
```

**Nota na planilha PDF**:
> "DESCONTAR A INTERNET DE R$ 65,00"

- Desconto de R$ 65 é aplicado **quando aplicável** (confirmar mensalmente com Robson)
- Lucas mora no AP 201 (recebe planilha personalizada)

---

## AP 601 — Dois Donos (COND ≠ FUNDO)

**Regra**: O condomínio e o fundo de reserva têm donos diferentes.

| Valor | Destinatário |
|-------|-------------|
| Condomínio (água + gás + rateio s/ fundo) | Proprietário principal |
| Fundo de reserva (R$ 150,00) | Gilberto Augusto Beltrão |

**Nota na planilha PDF**:
> "DESCONTAR O VALOR DO FUNDO DE RESERVA DE R$ 150,00"
> "VALOR A PAGAR PARA O CONDOMÍNIO: R$ XXX,00"

**Recibos**: 2 recibos separados — `AP 601 COND` e `AP 601 FRESERV`

---

## AP 801 — Saldo Acumulado

- **Proprietário**: Alberto Jacomini de Souza
- Mantém controle de saldo acumulado na aba `VRS. DEVIDOS E OUTROS`
- Recibo especial com saldo acumulado

```
saldo_novo = saldo_anterior + valor_competencia - valor_pago
```

---

## Síndico — Rateio Diferenciado

- Robson (síndico) não paga o rateio para si mesmo
- O valor que seria dele é dividido entre os outros 13 condôminos

```python
rateio_parcial = ROUND(total_despesas / 14, 2)   # divisão base
rateio_sindico = ROUND(rateio_parcial / 13, 2)   # adicional por unidade
# Total por unidade (exceto síndico):
# rateio_final = rateio_parcial + rateio_sindico + fundo_reserva
```

---

## Lucas e Clara — Planilhas Personalizadas

- **Lucas**: AP 201 (confirmado) — recebe planilha com nota de desconto internet
- **Clara**: AP não confirmado ainda (pendência — ver [[../04-Plano/Pendencias]])

---

## Recibos — 17 Modelos

| Tipo | Qtd | Detalhes |
|------|-----|---------|
| Padrão (201-702) | 11 | Puxam dados de `MEDICOES E TABELAS` |
| AP 601 COND | 1 | Apenas condomínio (sem fundo reserva) |
| AP 601 FRESERV | 1 | Apenas fundo de reserva (Gilberto) |
| AP 801 | 1 | Com saldo acumulado (Alberto) |
| Templates "NÃO USAR" | 3 | Modelos de referência — não usar em produção |

**Macro VBA `Extenso()`**: Converte valor monetário para texto em português.
- Exemplo: `745.00` → `"Setecentos e quarenta e cinco reais"`
- Deve ser reimplementada em Python para geração de recibos PDF
