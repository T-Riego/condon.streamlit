# MEDICOES E TABELAS — Motor Central

> Aba principal com **825 fórmulas**. Contém Tabelas 1, 2 e 3.
> Arquivo: `Planilhas mensais 202508 em diante RASCUNHO EM USO.xlsx`

## Tabela 1 — Leituras e Consumo (linhas 4-86)

Colunas C-Q = 15 medidores (201, 201 GAS PISC., 202...802). Coluna R = TOTAL.

### Fórmulas-chave

```excel
# Consumo atual (linha 40)
C40 = C39 - C38    (leitura atual - anterior)

# % do consumo total (linha 41)
C41 = ROUND(C40/$AY$43, 3)    (3 decimais)

# Consumo anterior (linha 42)
C42 = C38 - C37

# Variação (linha 43)
C43 = C40 - C42

# Detecção de anomalia (linhas 44-45)
C44 = (C38-C37) - (C37-C36)    (dupla diferença)
```

### Gás (linhas 78-86)
```excel
C82 = C81 - C80    (consumo gás atual)
```

## Tabela 2 — Consolidação (linhas 4-22, colunas T-AA)

### Fórmula CRÍTICA — Custo água/esgoto por unidade (célula X5)
```excel
X5 = ROUNDDOWN(W5*$BC$43 + ($BD$43+$BE$43)*V5, 2)
```
Onde:
- `W5` = consumo arredondado (ROUND 3 decimais)
- `$BC$43` = preço/m³ água
- `$BD$43` = valor esgoto
- `$BE$43` = valor recurso hídrico
- `V5` = % do consumo total

### Gás por unidade
```excel
# AP 201 (tem gás piscina)
AA5 = ROUND((Z5+Z6)*$CG$9, 2)

# Demais APs
AA7 = ROUND(Z7*$CG$10, 2)
```

### Consumo condominial (residual)
```excel
U4 = AY43 - SUM(U5:U19)    (total COPASA - soma individuais)
V4 = 1 - SUM(V5:V19)       (% restante)
X4 = IF(W4>0, ROUND(AZ43-SUM(X5:X19), 2), 0)
```

### Verificação (linhas 20-22)
```excel
U21 = AY43    (total consumo COPASA)
X21 = AZ43    (total conta COPASA)
B163 = B161 - B162    (diferença = DEVE SER 0)
```

## Tabela 3 — Resumo e Valores Finais (linhas 102-163)

### Rateio
```excel
G123 = SUM(G102:G122)         # total despesas
G124 = ROUND(G123/14, 2)      # por unidade (14 APs)
G125 = ROUND(G124/13, 2)      # síndico (13 APs)
G127 = G124 + G125 + G126     # total com ajustes
```

### Valores devidos por AP (linhas 146-159)
```excel
B146 = W5       # consumo água
C146 = X5       # custo água/esgoto
D146 = Z6       # consumo gás (AP 201 usa Z6 para piscina)
E146 = AA5      # custo gás
F146 = 'VRS. DEVIDOS E OUTROS'!$F$105    # rateio final ←← "f105"!
H146 = SUM(C146+E146+F146)               # total exato
G146 = ROUNDUP(H146, 0)                  # TOTAL SEM CENTAVOS
```

### Verificação final
```excel
G161 = SUM(G145:G158) + 150    # total + fundo reserva
G135 = SUM(G145:G159) = SUM('PLAN P COND'!G48:G62)    # cross-check
```

## Tabelas Auxiliares

### COPASA NFs (colunas AV-BF)
Dados da conta: data leitura, vencimento, pagamento, consumo m³, valor total, decomposição água/esgoto.

### Tarifas (colunas BH-BX, ocultas)
Simulação de faixas tarifárias COPASA (0-5, 5-10, 10-15, 15-20, 20-40, 40-60 m³).

### Gás (colunas CA-CG)
Histórico de compras de gás: data, kg, preço/kg, total, conversão m³, **custo/m³** ("cg10").
```excel
CG = CE * CF    # custo/m³ = preço_arredondado * 2.5
```

## Referências cruzadas
- Puxa de: [[Planilha - LANCTºS]] (totais despesas para rateio)
- Puxa de: [[Planilha - VRS DEVIDOS E OUTROS]] (F105 = rateio final)
- Alimenta: [[Planilha - PLAN P COND]] (todos os valores de saída)
- Alimenta: [[Planilha - Recibos]] (valores e nº recibo)

---
**Tags**: #planilha #motor #formulas #critico
