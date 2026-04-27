# Modelo de Dados

[[HOME|← Home]]

---

## Entidades Principais

### Condominio
```
id, nome, cnpj, banco_info, pix_key
```

### UnidadeHabitacional
```
id, condominio_id, numero (201-802), andar,
ativo, participa_rateio, participa_sindico, observacoes
```
- `participa_sindico = False` para o AP do síndico (Robson)

### Morador
```
id, unidade_id, nome, cpf, email, telefone,
eh_pagador, eh_sindico
```

### Medidor
```
id, unidade_id, tipo (agua|gas), identificador,
descricao, ativo
```
- AP 201 tem 3 medidores: 1 água + 2 gás (unidade + piscina)

---

## Ciclo Mensal

### Competencia
```
id, ano_mes (202604), data_vencimento,
status (aberta | conferida | fechada), oficio_numero
```

### Leitura
```
id, competencia_id, medidor_id, data_medicao,
leitura_anterior, leitura_atual, consumo_calculado
```

### ContaCopasa
```
competencia_id, consumo_total_m3, valor_total,
valor_agua, valor_esgoto, valor_recurso,
custo_por_m3, data_leitura, data_vencimento
```

### AbastecGas
```
data_compra, quantidade_kg, valor_total,
preco_por_kg, volume_m3, custo_por_m3
```

### Despesa
```
competencia_id, descricao, valor, data_referencia,
tipo, rateavel, base_rateio (14 | 13), informar_condom
```

---

## Resultados

### ValorDevido
```
competencia_id, unidade_id,
agua_consumo_m3, agua_esgoto_r$,
gas_consumo_m3, gas_valor_r$,
rateio_r$, total_exato, total_arredond, observacoes
```

### Pagamento
```
valor_devido_id, valor_pago, data_pagamento,
forma_pagamento, numero_recibo, recibo_enviado,
nome_pagador, doc_pagador, observacoes
```

### FundoReserva
```
competencia_id, saldo_anterior, entradas,
saidas, saldo_final, valor_por_unidade
```

---

## Casos Especiais no Modelo

| Unidade | Campo Especial | Valor |
|---------|---------------|-------|
| AP 201 | `tem_desconto_internet` | R$ 65,00 (quando aplicável) |
| AP 601 | `pagamento_fracionado` | True (COND ≠ FRESERV) |
| AP 801 | `saldo_acumulado` | Calculado mês a mês |
| Síndico | `participa_sindico` | False na UnidadeHabitacional |

---

## Diagrama Simplificado

```
Condominio
  └── UnidadeHabitacional (14 unidades)
        ├── Morador (1..N)
        └── Medidor (1 água + 1-2 gás)
              └── Leitura (1 por competência)

Competencia (1 por mês)
  ├── ContaCopasa
  ├── AbastecGas
  ├── Despesa (N)
  ├── ValorDevido (14, um por unidade)
  │     └── Pagamento (0..N)
  └── FundoReserva
```
