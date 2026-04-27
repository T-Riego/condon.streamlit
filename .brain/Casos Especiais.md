# Casos Especiais

> Regras que fogem do padrão dos 14 APs. Cada uma deve ter tratamento explícito no código.

## AP 201 — Dois Medidores + Desconto Internet

### Medidores
- **Medidor 1**: água/gás do apartamento (normal)
- **Medidor 2**: gás da piscina ("201 GAS PISC.")
- Na Tabela 2: `custo_gas_201 = ROUND((gas_apt + gas_piscina) * custo_m3, 2)`
- Coluna D na planilha usa Z6 (piscina) em vez de Z5

### Desconto Internet
- Planilha AP 201 inclui nota: **"APARTAMENTO 201: DESCONTAR A INTERNET DE R$ 65,00"**
- O desconto aparece DEPOIS da tabela de valores (não altera o cálculo do rateio)
- A internet R$65 está nos lançamentos de despesas como item rateado entre todos

### Planilha Personalizada
- PDF separado com a nota de desconto
- Mesmos valores que a planilha geral + nota extra

## AP 601 — Pagamento Separado (Condomínio vs Fundo)

### Situação
- Dono do apartamento paga condomínio
- **Gilberto Augusto Beltrão** paga fundo de reserva separadamente
- Resultado: 2 recibos separados (601 COND + 601 FRESERV)

### Planilha AP 601
Nota extra no PDF:
```
APTº 601: DESCONTAR O VALOR DO FUNDO DE RESERVA DE R$ 150,00
VALOR A PAGAR PARA O CONDOMÍNIO: R$ 386,00
```
(386 = 536 total - 150 fundo)

### Recibos
- Aba **601 COND**: valor sem fundo, usa coluna $R$154
- Aba **601 FRESERV**: só R$150, nome = Gilberto Augusto Beltrão

## AP 801 — Saldo Acumulado

### Situação
- **Alberto Jacomini de Souza** tem controle de saldo/crédito
- Aba VRS. DEVIDOS E OUTROS linhas 110-123 rastreia:
  - Valor devido vs valor recebido
  - Saldo credor acumulado mês a mês
- Recibo 801 puxa dados de VRS (8 fórmulas especiais)

### Fórmulas
```excel
C112 = P8          # valor pago
D112 = B112-C112   # diferença
G112 = D112+E112   # saldo acumulado
B113 = G112         # carrega pro próximo mês
```

## Síndico — Rateio 13 Unidades

- Total despesas dividido por **14** = rateio parcial
- Rateio parcial dividido por **13** = sobretaxa síndico
- O síndico (1 AP) não paga a própria sobretaxa para si
- Desde Jun/2023 (antes era /14 para tudo)
- Ver [[Rateio e Despesas]]

## Lucas e Clara — Informações Personalizadas

- Recebem planilhas com informações extras/personalizadas
- **Pendência**: confirmar quais APs são Lucas e Clara
- Hipótese: Lucas = AP 201 (desconto internet)? Clara = AP 601 (fundo separado)?
- Ver [[Pendencias Abertas]]

---
**Tags**: #especial #regras #ap201 #ap601 #ap801
