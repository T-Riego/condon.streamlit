# Modelo de Dados

> Entidades e relacionamentos para o banco de dados do sistema.

## Entidades Principais

### Condominio
| Campo | Tipo | Nota |
|---|---|---|
| id | int PK | |
| nome | str | "Condomínio Residencial Neápolis" |
| cnpj | str | "09.408.714/0001-08" |
| endereco | str | Belo Horizonte/MG |
| banco | str | "Banco Inter" |
| agencia | str | "0001" |
| conta | str | "26620410-4" |
| pix_key | str | CNPJ |

### UnidadeHabitacional
| Campo | Tipo | Nota |
|---|---|---|
| id | int PK | |
| condominio_id | FK | |
| numero | str | "201" a "802" |
| andar | int | 2 a 8 |
| ativo | bool | |
| participa_rateio_geral | bool | True (14 unidades) |
| participa_rateio_sindico | bool | False para o síndico |
| observacoes | str | Notas especiais (201, 601, 801) |

### Morador
| Campo | Tipo | Nota |
|---|---|---|
| id | int PK | |
| unidade_id | FK | |
| nome | str | |
| cpf | str | |
| email | str | |
| telefone | str | |
| eh_pagador | bool | Quem efetivamente paga |
| eh_sindico | bool | |
| ativo | bool | |

### Medidor
| Campo | Tipo | Nota |
|---|---|---|
| id | int PK | |
| unidade_id | FK | |
| tipo | enum | agua / gas |
| identificador | str | |
| descricao | str | Ex: "201 GAS PISC." |
| ativo | bool | |

### Competencia
| Campo | Tipo | Nota |
|---|---|---|
| id | int PK | |
| ano_mes | str | "202604" |
| data_vencimento | date | |
| oficio_numero | str | "04/2026" |
| status | enum | aberta / conferida / fechada |
| created_at | datetime | |

### Leitura
| Campo | Tipo | Nota |
|---|---|---|
| id | int PK | |
| competencia_id | FK | |
| medidor_id | FK | |
| data_medicao | date | Dias 27-29 |
| leitura_anterior | decimal | Auto-preenchido do mês anterior |
| leitura_atual | decimal | |
| consumo_calculado | decimal | atual - anterior |
| observacoes | str | |

### ContaCopasa
| Campo | Tipo | Nota |
|---|---|---|
| id | int PK | |
| competencia_id | FK | |
| consumo_total_m3 | decimal | Total da conta |
| valor_total | decimal | |
| valor_agua | decimal | Abastecimento |
| valor_esgoto | decimal | |
| valor_recurso_hidrico | decimal | |
| custo_por_m3 | decimal | ROUND(total/consumo, 2) |
| data_leitura | date | |
| data_vencimento | date | |
| data_pagamento | date | |

### AbastecimentoGas
| Campo | Tipo | Nota |
|---|---|---|
| id | int PK | |
| data_compra | date | |
| quantidade_kg | decimal | |
| valor_total | decimal | |
| preco_por_kg | decimal | |
| volume_m3 | decimal | kg / 2.5 |
| custo_por_m3 | decimal | |

### Despesa
| Campo | Tipo | Nota |
|---|---|---|
| id | int PK | |
| competencia_id | FK | |
| descricao | str | |
| valor | decimal | |
| data_referencia | date | |
| tipo | str | conservadora / elevador / luz / agua / retencao / seguro / contadora / internet / sindico / outros |
| rateavel | bool | |
| base_rateio | int | 14 ou 13 |
| informar_na_planilha | bool | |

### ValorDevido
| Campo | Tipo | Nota |
|---|---|---|
| id | int PK | |
| competencia_id | FK | |
| unidade_id | FK | |
| agua_consumo_m3 | decimal | |
| agua_esgoto_valor | decimal | ROUNDDOWN(x, 2) |
| gas_consumo_m3 | decimal | |
| gas_valor | decimal | ROUND(x, 2) |
| rateio_valor | decimal | |
| total_exato | decimal | agua + gas + rateio |
| total_arredondado | int | ROUNDUP(exato, 0) |
| observacoes | str | |

### Pagamento
| Campo | Tipo | Nota |
|---|---|---|
| id | int PK | |
| valor_devido_id | FK | |
| valor_pago | decimal | |
| data_pagamento | date | |
| forma_pagamento | str | PIX Inter / PIX Bradesco / PIX Nubank / depósito |
| numero_recibo | int | |
| recibo_gerado | bool | |
| recibo_enviado | bool | |
| nome_pagador | str | Pode ser diferente do morador |
| doc_pagador | str | |
| observacoes | str | |

### FundoReserva
| Campo | Tipo | Nota |
|---|---|---|
| id | int PK | |
| competencia_id | FK | |
| saldo_anterior | decimal | |
| entradas | decimal | 150 × 14 |
| saidas | decimal | |
| saldo_final | decimal | anterior + entradas - saidas |
| valor_por_unidade | decimal | Configurável (atual: 150) |

## Relacionamentos
```
Condominio 1──N UnidadeHabitacional
UnidadeHabitacional 1──N Morador
UnidadeHabitacional 1──N Medidor
Competencia 1──N Leitura
Medidor 1──N Leitura
Competencia 1──1 ContaCopasa
Competencia 1──N Despesa
Competencia 1──N ValorDevido
UnidadeHabitacional 1──N ValorDevido
ValorDevido 1──1 Pagamento
Competencia 1──1 FundoReserva
```

---
**Tags**: #modelo #dados #banco #entidades
