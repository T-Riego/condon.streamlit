# Recibos — 17 Modelos + VBA

> **72 fórmulas + macro VBA Extenso()**. Arquivo: `Recibos 202511 em diante.xlsm`

## 17 Abas (uma por recibo)

| Aba | Tipo | Morador/Nota |
|---|---|---|
| 201-702 (11 abas) | Padrão | Condomínio + fundo reserva juntos |
| 601 COND | Especial | Só condomínio (dono diferente do fundo) |
| 601 FRESERV | Especial | Só fundo reserva → Gilberto Augusto Beltrão |
| 801 | Especial | Com saldo acumulado → Alberto Jacomini de Souza |
| 3 templates "NAO USAR" | Referência | Modelos base (não usar em produção) |

## Fórmulas Padrão (4 por aba)

Todas referenciam workbook externo `[1]`:
```excel
B4 = '[1]MEDICOES E TABELAS'!$I${row}     # nº recibo
E4 = '[1]MEDICOES E TABELAS'!$G${row}     # valor R$
C10 = '[1]MEDICOES E TABELAS'!$E$139      # período vencimento
D12 = '[1]MEDICOES E TABELAS'!$J${row}    # data
```

Mapeamento de linhas: 201→146, 202→147, 301→148, 302→149, 401→150, 402→151, 501→152, 502→153, 601 COND→154, 602→155, 701→156, 702→157, 601 FRESERV→160.

### Exceções
- **601 COND**: usa coluna `$R$154` (valor só condomínio)
- **801**: 8 fórmulas puxando de VRS. DEVIDOS E OUTROS (saldo, crédito, débito)

## Macro VBA — Extenso()

Módulo: `Modulo1`. Converte valor monetário para português por extenso.
```
450.50 → "quatrocentos e cinquenta reais e cinquenta centavos"
```

Cadeia de funções: `Extenso()` → `Trilhoes()` → `Bilhoes()` → `Milhoes()` → `Milhares()` → `Centenas()` → `Dezenas()` → `Unidades()` + `Centavos()`

Fórmula de array em cada aba: `{=Extenso(E4)&","}`

**No sistema novo**: implementar em Python (lib `num2words` ou função customizada).

---
**Tags**: #planilha #recibos #vba #pdf
