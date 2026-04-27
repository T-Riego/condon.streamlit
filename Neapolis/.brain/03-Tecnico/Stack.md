# Stack Tecnológica

[[HOME|← Home]]

---

## Decisão Final: Estratégia em 2 Fases

### Fase 1 — MVP de Validação (4-6 semanas)

**Stack**: `Python` + `Streamlit` + `SQLite` + `ReportLab`

| Componente | Ferramenta | Justificativa |
|-----------|-----------|--------------|
| Motor de cálculos | Python + `decimal.Decimal` | Replica arredondamentos Excel com precisão |
| Interface | Streamlit | UI funcional em dias, sem frontend separado |
| Banco de dados | SQLite | Zero infraestrutura, 14 unidades = suficiente |
| Geração de PDFs | ReportLab | Layout idêntico ao atual |
| Deploy | Streamlit Cloud (grátis) ou Docker local | |

**Por que não alternativas?**
- **Canvas/Figma**: ferramentas de design, não de desenvolvimento
- **Next.js puro**: JS não tem Decimal nativo; ROUNDDOWN/ROUNDUP em float é propenso a erro
- **Streamlit em produção**: limitado para mobile/offline

---

### Fase 2 — Produção (8-12 semanas após MVP validado)

**Stack**: `Next.js (PWA)` + `FastAPI` + `PostgreSQL`

| Componente | Ferramenta | Justificativa |
|-----------|-----------|--------------|
| Frontend | Next.js + Tailwind CSS | PWA responsivo, funciona no Android do Robson |
| Offline | Service Worker | Leituras de medidores sem internet |
| API | FastAPI | Reusa 100% do motor Python da Fase 1 |
| Banco | PostgreSQL | Integridade, backup, auditoria |

---

## Pré-requisitos de Desenvolvimento

```bash
# Fase 1
python >= 3.11
pip install streamlit reportlab sqlalchemy

# Testes
pip install pytest

# Fase 2 (futura)
node >= 20
pip install fastapi uvicorn
```

---

## Estrutura de Pastas Planejada

```
/src
  /core          # Motor de cálculos — reusável Fase 1 e 2
    arredondamentos.py   # ROUND, ROUNDDOWN, ROUNDUP idênticos ao Excel
    calc_agua.py         # consumo, %, custo água/esgoto
    calc_gas.py          # conversão kg→m³, custo gás
    calc_rateio.py       # despesas/14, síndico/13, fundo
    calc_total.py        # consolidação + ROUNDUP final
  /models              # Modelos SQLAlchemy/Prisma
  /api                 # FastAPI (Fase 2)
  /frontend            # Next.js (Fase 2)
  /streamlit           # UI Streamlit (Fase 1)
  /pdf                 # Geração de PDFs
  /import              # Importação dados legados
  /tests               # Testes com dados reais
```
