# VRS. DEVIDOS E OUTROS — Valores Devidos

> **603 fórmulas**. Aba mais complexa em contabilidade. Rateio, AP 801, fundo de reserva.

## Valores Devidos por Unidade (linhas 2-88)

Blocos mensais de 7 linhas, 12 meses (Mai/2025 → Abr/2026).

Padrão por mês:
```excel
Linha 3: consumo COPASA m³ por unidade
Linha 4: COPASA água/esgoto R$ por unidade
Linha 5: gás consumo m³
Linha 6: gás R$
Linha 7: despesas R$
Linha 8: TOTAL A PAGAR ARRED. = SUM(C8:P8) + LANCTºS!C34
Linha 9: TOTAL EXATO = SUM(D4+D6+D7) por unidade
```

Colunas C-Q = condomínio + 14 APs, R = TOTAL/MÊS.

### Verificação dupla
Coluna W: `W2 = SUM(A2:U2) = SUM(Y2:AS2)` (tabela esquerda = tabela direita duplicada)
```excel
R87 = R85 = 'MEDICOES E TABELAS'!G161    # total deve bater
R88 = R86 = 'MEDICOES E TABELAS'!H161    # total exato deve bater
```

## Rateio Mensal (linhas 94-105)

```excel
A94 = LANCTºS!B34          # data
B94 = LANCTºS!C37          # total despesas
C94 = ROUND(B94/14, 2)     # rateio parcial (÷14)
D94 = ROUND(C94/13, 2)     # síndico (÷13)
E94 = LANCTºS!C34          # fundo reserva
F94 = E94 + D94 + C94      # RATEIO FINAL ←← "f105" na linha 105!
```

Verificação: `N105 = F105 = 'PLAN P COND'!G31`

## AP 801 — Saldo Acumulado (linhas 110-123)

AP 801 (Alberto Jacomini de Souza) tem controle de saldo:
```excel
A112 = A8        # data
C112 = P8        # valor pago
D112 = B112-C112 # saldo
G112 = D112+E112 # saldo acumulado
B113 = G112      # carrega para mês seguinte
```
Verificação: `H109 = G123 = 'MEDICOES E TABELAS'!X158`

## AP 201 — Pagamentos (linhas 129-140)

Rastreamento de pagamentos com refs a [[Planilha - LANCTºS]]:
```excel
H129 = LANCTºS!C11
D129 = B129 - C129    # diferença pago vs esperado
```

## Fundo de Reserva (linhas 161-172)

```excel
C161 = saldo_anterior
E161 = 150 * 14         # R$2.100/mês
F162 = LANCTºS!G26      # saídas vinculadas a despesas
J161 = C161 + E161 - F161   # saldo final
C162 = J161              # carrega para mês seguinte
```
Verificação: `U172 = J172 = 'PLAN P COND'!G71`

## Referências
- Puxa de: [[Planilha - LANCTºS]] (totais, datas, fundo)
- Alimenta: [[Planilha - MEDICOES E TABELAS]] (F105 = rateio)
- Alimenta: [[Planilha - Recibos]] (AP 801 — saldo)

---
**Tags**: #planilha #rateio #formulas #critico
