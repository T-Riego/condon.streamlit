# Plano de Execução — Sprints

[[HOME|← Home]]

---

## Fase 1 — MVP (4-6 semanas)

### Sprint 1 — Motor de Cálculos (Semanas 1-2)

| # | Tarefa | Prioridade |
|---|--------|-----------|
| 1.1 | `calc_agua.py` — consumo individual, % proporcional, custo/m³, esgoto | Alta |
| 1.2 | `calc_gas.py` — conversão kg→m³, custo/m³, custo por unidade | Alta |
| 1.3 | `calc_rateio.py` — despesas/14, síndico/13, fundo reserva | Alta |
| 1.4 | `calc_total.py` — consolidação + ROUNDUP sem centavos | Alta |
| **1.5** | **`arredondamentos.py` — ROUND, ROUNDDOWN, ROUNDUP idênticos Excel** | **CRÍTICA** |
| 1.6 | Casos especiais: AP 201 (piscina), AP 601 (split), AP 801 (saldo) | Alta |
| **1.7** | **Testes com dados reais Abril/2026** (resultado esperado nos PDFs) | **CRÍTICA** |
| **1.8** | **Validar: diferença Python vs planilha = R$ 0,00 para todos APs** | **CRÍTICA** |

**Critério de conclusão**: Todos os 14 apartamentos com total = valor da planilha.

---

### Sprint 2 — Banco e Interface (Semanas 3-4)

| # | Tarefa | Prioridade |
|---|--------|-----------|
| 2.1 | Modelar banco SQLite (ver [[../03-Tecnico/Modelo-Dados]]) | Alta |
| 2.2 | Script importação histórico Feb/2023 → Abr/2026 | Média |
| 2.3 | Streamlit: Dashboard (competência atual, status, pendências) | Alta |
| 2.4 | Streamlit: Entrada de leituras (água + gás por AP) | Alta |
| 2.5 | Streamlit: Lançamento conta COPASA | Alta |
| 2.6 | Streamlit: Lançamento despesas mensais | Alta |
| 2.7 | Streamlit: Visualização Tabelas 1, 2, 3 consolidadas | Alta |
| 2.8 | Streamlit: Checklist de conferência | Média |

---

### Sprint 3 — PDFs e Finalização (Semanas 5-6)

| # | Tarefa | Prioridade |
|---|--------|-----------|
| 3.1 | PDF "Planilha Geral" (layout idêntico ao atual) | Alta |
| 3.2 | PDF "Planilha AP 201" (com nota desconto internet) | Alta |
| 3.3 | PDF "Planilha AP 601" (com nota fundo reserva separado) | Alta |
| 3.4 | Recibos PDF (17 modelos) com valor por extenso em português | Alta |
| 3.5 | Controle de pagamentos (data, forma, nº recibo, enviado) | Média |
| 3.6 | Histórico mensal (consulta por competência) | Média |
| **3.7** | **Teste final: gerar Abril/2026 completo e comparar planilha real** | **CRÍTICA** |
| 3.8 | Deploy MVP (Streamlit Cloud ou Docker local) | Média |

---

## Fase 2 — Produção (após MVP validado)

| Sprint | Foco | Duração |
|--------|------|---------|
| Sprint 4 | Next.js + FastAPI + PostgreSQL + migração SQLite | 2 semanas |
| Sprint 5 | Frontend mobile-first (PWA): leituras, despesas, dashboard | 3 semanas |
| Sprint 6 | PDFs no backend + envio automático WhatsApp/email | 2 semanas |
| Sprint 7 | Testes, deploy, treinamento do Robson | 2 semanas |

### Entregáveis Fase 2
- App PWA para Android (Robson lê medidores no celular)
- Tela mobile com lanterna ativada
- Dashboard com gráficos de consumo histórico
- Envio automático PDFs por WhatsApp/email
- Checklist interativo de conferência
- Controle de acesso (Robson admin, Tiago dev)
- Backup automático PostgreSQL
