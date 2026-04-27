# Plano de Ação

> Documento detalhado: `../PLANO_DE_ACAO.md` (raiz do projeto)

## Resumo

### Fase 1 — MVP Streamlit (4-6 semanas)

**Sprint 1 (Sem 1-2)**: Motor de cálculos Python
- Módulos: calc_agua, calc_gas, calc_rateio, calc_total, arredondamentos
- [[Casos Especiais]] implementados
- Testes com [[Dados de Teste Abril 2026]]
- Meta: diferença = R$ 0,00 para todos os APs

**Sprint 2 (Sem 3-4)**: Banco + Interface
- SQLite com modelos ([[Modelo de Dados]])
- Importação dados históricos (Feb/2023 → Abr/2026)
- UI Streamlit: dashboard, leituras, COPASA, despesas, tabelas

**Sprint 3 (Sem 5-6)**: PDFs + Finalização
- 3 planilhas PDF (geral, 201, 601)
- 17 recibos PDF com valor por extenso
- Pagamentos e histórico
- Teste final completo

### Fase 2 — Produção (8-12 semanas)
- Next.js PWA + FastAPI + PostgreSQL
- Mobile-first para [[Robson]]
- Reusa 100% do motor Python
- Ver [[Stack Tecnologica]]

## Critério de Sucesso
Ver [[Dados de Teste Abril 2026]] — todos os valores devem bater.

## Próximos Passos
Ver [[Pendencias Abertas]]

---
**Tags**: #plano #roadmap #sprint
