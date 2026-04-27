# Planilhas Fonte — Mapa Completo

[[HOME|← Home]]

---

## Arquivos Excel

### 1. ÁGUA E GÁS LEITURAS.xlsx
- **Função**: Staging das leituras brutas dos medidores
- **Uso**: Robson digita no celular → sincroniza com planilha principal
- **Fórmulas**: ~60
- **Complexidade**: Baixa

### 2. Planilhas mensais 202508 em diante RASCUNHO EM USO.xlsx
Planilha principal com **8 abas**:

| Aba | Fórmulas | Função |
|-----|----------|--------|
| `ORIENTACOES E CONF.` | 7 | Checklist de verificação cruzada |
| `MEDICOES E COPASA HISTORICO` | 289 | Histórico de leituras e contas COPASA |
| `MEDICOES E TABELAS` | **825** | **Motor central — Tabelas 1, 2 e 3** |
| `LANCTºS` | 213 | Lançamento de despesas mensais |
| `VRS. DEVIDOS E OUTROS` | 603 | Valores devidos, rateio, AP 801, fundo reserva |
| `DADOS DO PAGTº` | 0 | Data entry puro — pagamentos recebidos |
| `PLAN P COND` | 102 | Planilha de saída para condôminos |
| `COPIAR PLAN P COND P TODAS` | 5 | Template de cópia |

### 3. Planilha p condôm 202302 em diante.xlsx
- **Função**: Compilação histórica de todas as planilhas mensais enviadas
- **Início**: Fevereiro/2023
- **Fórmulas**: ~50
- **Uso**: Referência/consulta histórica

### 4. Recibos 202511 em diante.xlsm
- **Função**: 17 recibos com macro VBA
- **Macro**: `Extenso()` — converte valor para texto em português
- **Fórmulas**: 72 + VBA
- **Início**: Novembro/2025

### 5. Adm.xlsx
- **Função**: Administração geral (detalhes desconhecidos)
- **Status**: **CRIPTOGRAFADO** — senha necessária (pendência)

---

## Referências de Células Importantes

| Referência | Aba | Significado |
|-----------|-----|------------|
| `CG10` | `MEDICOES E COPASA HISTORICO` | Custo/m³ de gás do mês |
| `F105` | `VRS. DEVIDOS E OUTROS` | Rateio final mensal |

---

## Total de Fórmulas Analisadas

**1.940+ fórmulas** distribuídas nas planilhas acima.
