# Dados de Teste — Abril/2026

> Valores reais extraídos dos PDFs. Usar para validar o motor de cálculos.

## Despesas do Mês

| Data | Descrição | Valor R$ |
|---|---|---|
| 10/04/26 | Conservadora Campos de Oliveira | 1.443,66 |
| 15/04/26 | Manutenção Elevador ThyssenKrupp | 1.231,11 |
| 15/04/26 | Conta de Água COPASA (rateada) | 236,41 |
| 17/04/26 | Conta de Luz CEMIG | 429,96 |
| 20/04/26 | Retenções Federais/Municipais | 238,45 |
| 25/03/26 | Seguro do Prédio (4ª/6) | 259,06 |
| 28/04/26 | Honorários Contadora Mayra | 162,00 |
| 01/04/26 | Internet Câmeras | 65,00 |
| **TOTAL** | | **4.065,65** |

## Rateio
```
Rateio parcial = ROUND(4065.65/14, 2) = 290.40
Síndico        = ROUND(290.40/13, 2)  = 22.34
Fundo reserva  = 150.00
RATEIO FINAL   = 462.74
```

## Valores por Unidade

| APTº | Água m³ | Água/Esgoto R$ | Gás m³ | Gás R$ | Rateio R$ | Total R$ |
|---|---|---|---|---|---|---|
| COND | 18,457 | 236,41 | 0,000 | 0,00 | 0,00 | 0,00 |
| 201 | 21,886 | 281,88 | 0,000 | 0,00 | 462,74 | 745 |
| 202 | 16,763 | 215,24 | 2,741 | 103,82 | 462,74 | 782 |
| 301 | 19,759 | 253,65 | 4,059 | 153,73 | 462,74 | 871 |
| 302 | 19,988 | 256,59 | 2,429 | 92,00 | 462,74 | 812 |
| 401 | 25,559 | 329,05 | 1,414 | 53,56 | 462,74 | 846 |
| 402 | 23,777 | 305,87 | 4,820 | 182,56 | 462,74 | 952 |
| 501 | 25,421 | 326,78 | 1,213 | 45,94 | 462,74 | 836 |
| 502 | 13,441 | 173,17 | 1,029 | 38,97 | 462,74 | 675 |
| 601 | 3,979 | 50,68 | 0,582 | 22,04 | 462,74 | 536 |
| 602 | 0,682 | 8,79 | 0,130 | 4,92 | 462,74 | 477 |
| 701 | 13,458 | 173,29 | 0,785 | 29,73 | 462,74 | 666 |
| 702 | 7,190 | 91,93 | 3,761 | 142,45 | 462,74 | 698 |
| 801 | 4,531 | 58,51 | 0,423 | 16,02 | 462,74 | 538 |
| 802 | 14,109 | 181,86 | 2,440 | 92,42 | 462,74 | 738 |

## Fundo de Reserva
```
Saldo em 28/02/2026:  R$ 38.030,60
Entradas Mar/2026:    R$ 2.100,00
Saídas:               R$ 0,00
Saldo em 31/03/2026:  R$ 40.130,60
```

## Notas Especiais nos PDFs
- **AP 201**: "DESCONTAR A INTERNET DE R$ 65,00"
- **AP 601**: "DESCONTAR O VALOR DO FUNDO DE RESERVA DE R$ 150,00" → "VALOR A PAGAR PARA O CONDOMÍNIO: R$ 386,00"

## Dados Bancários (rodapé)
```
Banco Inter, AG 0001, CC 26620410-4
Condomínio do Residencial Neápolis
CNPJ 09.408.714/0001-08
PIX = CNPJ
```

## Validação Python (executada em 26/04/2026)
- Rateio final: ✅ R$ 462,74
- ROUNDUP todos os APs: ✅ 14/14 corretos
- Fundo reserva: ✅ R$ 40.130,60

---
**Tags**: #teste #dados #validacao #abril2026
