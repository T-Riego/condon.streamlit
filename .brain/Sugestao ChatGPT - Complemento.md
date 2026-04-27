# Sugestão ChatGPT — Complemento (MD1.md)

> Arquivo original: `MD1.md` na raiz do projeto. Continuação do plano base.

## O que contém
- Fórmula do consumo condominial
- Rateio do consumo condominial (/14)
- Regra de esgoto proporcional (regra de 3)
- Cálculo de gás (conversão 2.5 kg/m³)
- Tabela 2: consolidação
- Etapa 7: lançamento de despesas
- Tabela 3: valores finais + verificação (diferença = 0)
- Controle de pagamentos (campos sugeridos)
- Geração de recibos (PDF)
- Histórico e banco legado
- Checklist mensal (18 itens)
- 9 módulos detalhados
- 10 regras consolidadas
- 10 telas sugeridas com campos

## Avaliação
Complementa bem o MD.md com mais detalhes operacionais. As fórmulas estão corretas em nível conceitual, mas **sem a precisão de arredondamento** que a análise das planilhas revelou:
- Usa `consumo_agua_unidade / soma_consumo_agua_individual` → correto
- Mas não especifica ROUND(x, 3) para o percentual
- Não menciona ROUNDDOWN para custo água
- Não menciona ROUNDUP para total final

Todos esses detalhes foram capturados em [[Formulas e Arredondamentos]].

## Referência
Arquivo original: `../MD1.md`

---
**Tags**: #chatgpt #sugestao #complemento
