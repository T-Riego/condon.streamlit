# Fundo de Reserva

> Controle de saldo acumulado mês a mês. Atualmente R$150/AP/mês.

## Regra Atual
- Valor mensal por unidade: **R$150,00** (configurável)
- Contribuição mensal total: 150 × 14 = **R$2.100,00**
- Controlado na aba [[Planilha - VRS DEVIDOS E OUTROS]] linhas 161-172

## Fórmula
```excel
saldo_final = saldo_anterior + entradas - saidas
C162 = J161    (carrega para mês seguinte)
E161 = 150*14  (contribuição mensal)
F162 = LANCTºS!G26   (saídas vinculadas a despesas específicas)
```

## Histórico de Valores
| Período | Valor/AP/mês |
|---|---|
| Antes de Fev/2024 | Não existia |
| Fev/2024 | R$300 |
| Atual | **R$150** |

## Saldo Atual (Março/2026)
- Saldo existente em 28/02/2026: **R$38.030,60**
- Entradas Mar/2026: R$2.100,00
- Saídas: R$0,00
- **Saldo em 31/03/2026: R$40.130,60**

## Verificação
```excel
U172 = J172 = 'PLAN P COND'!G71    # saldo bate com planilha de saída
```

## No AP 601
O fundo de reserva é pago **separadamente** por Gilberto Augusto Beltrão.
Ver [[Casos Especiais]].

---
**Tags**: #fundo #reserva #saldo
