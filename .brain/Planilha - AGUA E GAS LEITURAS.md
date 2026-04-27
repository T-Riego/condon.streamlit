# ÁGUA E GÁS LEITURAS — Staging de Leituras

> **~60 fórmulas**. Planilha de campo para registrar leituras no celular.

## Aba: PLANILHA GERAL (A1:AF13)

15 medidores nas colunas C-Q: 201, 201 GAS PISC., 202, 301, 302, 401, 402, 501, 502, 601, 602, 701, 702, 801, 802. Coluna R = TOTAL.

### Bloco Água (linhas 2-7)
```excel
Linha 2: leitura água (2025-03-29)
Linha 3: leitura água (2025-04-28)
Linha 4: leitura água (próxima — a preencher)
Linha 5: (A) DIF. C/LEIT. ANT. = C4-C3
Linha 6: (B) DIF. ANT. = C3-C2
Linha 7: A(-) B = C5-C6    (variação período)
```

### Bloco Gás (linhas 8-13) — mesma estrutura

### Totais
```excel
R2-R13: =SUM(C{n}:Q{n})    # totais por linha
```

## Aba: Planilha2 (Sync)

Staging mais recente, sem fórmulas (valores puros).
- Coluna A: nº AP | B: água atual | C: água anterior | D: gás atual | E: gás anterior
- Linha 17: totais SUM
- B19: "SINC" — marcador de sincronização

Valores em Planilha2 são mais recentes que PLANILHA GERAL → aguardando transferência.

## Observação
27 named ranges órfãs (QTD.A, TOT_NF, ICMS_ST...) — restos de template fiscal, sem conexão com dados.

---
**Tags**: #planilha #leituras #staging
