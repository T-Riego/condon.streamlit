# Rateio e Despesas

> Lógica de divisão das despesas condominiais entre os moradores.

## Tipos de Despesa (Abril/2026)

| Despesa | Valor R$ | Rateável |
|---|---|---|
| Conservadora Campos de Oliveira | 1.443,66 | Sim |
| Manutenção Elevador ThyssenKrupp | 1.231,11 | Sim |
| Conta de Água COPASA | 236,41 | Sim (rateada separado) |
| Conta de Luz CEMIG | 429,96 | Sim |
| Retenções Federais/Municipais | 238,45 | Sim |
| Seguro do Prédio (parcela 4ª/6) | 259,06 | Sim |
| Honorários Contadora Mayra | 162,00 | Sim |
| Internet Câmeras | 65,00 | Sim |
| **TOTAL** | **4.065,65** | |

## Fórmula do Rateio

```
rateio_parcial = ROUND(total_despesas / 14, 2)
                = ROUND(4065.65 / 14, 2)
                = 290.40

rateio_sindico = ROUND(rateio_parcial / 13, 2)
               = ROUND(290.40 / 13, 2)
               = 22.34

fundo_reserva  = 150.00 (configurável)

RATEIO FINAL   = 290.40 + 22.34 + 150.00 = 462.74
```

## Por que /14 e depois /13?

- **÷14**: Todas as 14 unidades pagam a base das despesas
- **÷13**: O síndico administra o condomínio e recebe "serviço do síndico" como compensação. A sobretaxa é distribuída entre os **13 outros** moradores (o síndico não paga para si mesmo)

## Retenções (DARF)
- A contadora (Mayra S. P. Oliveira) calcula as retenções
- Gera DARF para pagamento
- Valores federais e municipais são responsabilidade do condomínio
- Entram como despesa normal no rateio

## Nota sobre Água
A água da COPASA é rateada **separadamente** (proporcional ao consumo individual), não entra no rateio geral. O valor que aparece nos lançamentos (R$236,41 no exemplo) é o consumo condominial que vai para o rateio geral.

Ver [[Formulas e Arredondamentos]] para detalhes de cada arredondamento.
Ver [[Fundo de Reserva]] para controle do saldo.

---
**Tags**: #rateio #despesas #regras
