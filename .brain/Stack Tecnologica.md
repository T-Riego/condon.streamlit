# Stack Tecnológica

> Decisão de tecnologia: 2 fases.

## Fase 1 — MVP (4-6 semanas)

| Componente | Tecnologia | Justificativa |
|---|---|---|
| Linguagem | **Python 3.11+** | Decimal nativo, melhor para cálculos financeiros |
| UI | **Streamlit** | Prototipagem rápida, widgets de input |
| Banco | **SQLite** | Zero infraestrutura, suficiente para 14 APs |
| PDF | **ReportLab** ou **WeasyPrint** | Layout idêntico ao atual |
| Testes | **pytest** | Validação contra dados reais |
| Deploy | **Streamlit Cloud** ou Docker local | Gratuito |

### Estrutura MVP
```
/src
  /core/           # Motor de cálculos (reutilizável na Fase 2)
    calc_agua.py
    calc_gas.py
    calc_rateio.py
    calc_total.py
    arredondamentos.py
    extenso.py       # Valor por extenso (substitui VBA)
  /models/          # SQLAlchemy models
  /streamlit/       # Páginas da UI
  /pdf/             # Geração de PDFs
  /import/          # Importação de dados legados
  /tests/           # pytest com dados reais
```

## Fase 2 — Produção (8-12 semanas)

| Componente | Tecnologia | Justificativa |
|---|---|---|
| Frontend | **Next.js 14+ (App Router)** | PWA, SSR, mobile-first |
| Estilo | **Tailwind CSS** | Responsivo, rápido |
| Backend | **FastAPI** | Reusa motor Python, async, docs automáticas |
| Banco | **PostgreSQL** | Integridade, backup, auditoria |
| ORM | **SQLAlchemy** (backend) / **Prisma** (se full Next.js) | |
| PDF | **ReportLab** (via API) | Mesmo da Fase 1 |
| Auth | **NextAuth.js** | Login Robson + Tiago |
| Deploy | **Vercel** (front) + **Railway/Render** (API) | |

### PWA Features
- Funciona offline (service worker)
- Instalável no Android do Robson
- Modo leitura de medidores (tela simplificada)
- Sync quando online

## Opções Descartadas

| Opção | Motivo |
|---|---|
| Canvas/Figma | Ferramenta de design, não de dev |
| Kanban (Trello) | Gestão de tarefas, não sistema financeiro |
| Streamlit em produção | Limitado em mobile, sem offline |
| Next.js puro (sem Python) | JS não tem Decimal nativo, risco de erro em arredondamentos |
| Flutter | Complexo demais para o escopo, 2 codebases |
| Django + HTMX | Bom, mas menos moderno; Streamlit é mais rápido para MVP |

---
**Tags**: #stack #tecnologia #decisao
