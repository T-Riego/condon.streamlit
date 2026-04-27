# PLAN P COND — Planilha para Condôminos

> **102 fórmulas**. Documento de saída enviado aos moradores (gera PDF).

## Estrutura

Header: "Condomínio Neápolis", nº ofício, assunto, data vencimento.
```excel
A17 = 'MEDICOES E TABELAS'!T1    # título "Lancamentos - Abril/2026"
```

## Despesas (linhas 19-31)

```excel
G27 = SUM(G19:G26)          # total despesas
G28 = ROUND(G27/14, 2)      # rateio parcial (÷14)
G29 = ROUND(G28/13, 2)      # síndico (÷13)
G30 = 'VRS. DEVIDOS E OUTROS'!F91    # fundo reserva
G31 = G28 + G29 + G30       # RATEIO FINAL por unidade
```

## Tabela 3 — Valores por AP (linhas 48-62)

Um AP por linha, todos linkados a [[Planilha - MEDICOES E TABELAS]]:
```excel
B49 = 'MEDICOES E TABELAS'!W5     # consumo água m³
C49 = 'MEDICOES E TABELAS'!X5     # custo água/esgoto R$
D49 = 'MEDICOES E TABELAS'!Z6     # consumo gás m³
E49 = 'MEDICOES E TABELAS'!AA5    # custo gás R$
F49 = $G$31                        # rateio (igual para todos)
G49 = ROUNDUP(C49+E49+F49, 0)     # TOTAL → SEM CENTAVOS
```

## Fundo de Reserva (linhas 68-71)
```excel
D68 = 'VRS. DEVIDOS E OUTROS'!B172    # contribuições
G68 = 'VRS. DEVIDOS E OUTROS'!C172
G71 = G68 + G69 - G70                 # saldo final
```

## 3 Versões de PDF Geradas

Ver [[Casos Especiais]] para detalhes:
1. **Planilha Geral** — sem notas especiais
2. **Planilha AP 201** — "DESCONTAR A INTERNET DE R$ 65,00"
3. **Planilha AP 601** — "DESCONTAR O VALOR DO FUNDO DE RESERVA DE R$ 150,00" + "VALOR A PAGAR PARA O CONDOMÍNIO: R$ XXX,00"

---
**Tags**: #planilha #saida #pdf
