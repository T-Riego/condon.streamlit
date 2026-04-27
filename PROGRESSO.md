# Sistema ADM Condomínio Neápolis — Progresso do Projeto

> Atualizado em 27/04/2026 — Sessão 2.

---

## Visão geral

Sistema de gestão condominial para o **Residencial Neápolis** (BH/MG, 14 unidades).
Substitui planilhas Excel por aplicação web completa.

---

## Arquitetura final (confirmada)

```
GitHub (T-Riego/condon.streamlit)  ──► push main ──► VPS /opt/condon/streamlit
GitHub (T-Riego/condon.web)        ──► push main ──► VPS /opt/condon/web
GitHub (T-Riego/condon.api)        ──► push main ──► VPS /opt/condon/api

VPS 187.55.77.125
  ├── Nginx (existente, porta 80/443)
  │     ├── dotf4p.com      → containers existentes  [NÃO TOCADO]
  │     ├── riegos.dev      → containers existentes  [NÃO TOCADO]
  │     ├── condon.streamlit.riegos.dev  → proxy → Traefik :8090
  │     ├── condon.web.riegos.dev        → proxy → Traefik :8090
  │     └── condon.api.riegos.dev        → proxy → Traefik :8090
  │
  ├── Traefik :8090 (interno, rede traefik-net)
  │     ├── condon.streamlit.riegos.dev → container condon-streamlit :8501
  │     ├── condon.web.riegos.dev       → container condon-web :80
  │     └── condon.api.riegos.dev       → container condon-api :8000
  │
  └── Portainer :9000 (interno, gerencia todos os containers)

Supabase (PostgreSQL)  ←── FastAPI lê/escreve
  └── https://mgkyqailpawykhzsidxd.supabase.co
```

**DNS Cloudflare (proxy OFF durante setup):**

| Tipo | Nome | IP |
|---|---|---|
| A | `condon.streamlit.riegos.dev` | `187.55.77.125` |
| A | `condon.web.riegos.dev` | `187.55.77.125` |
| A | `condon.api.riegos.dev` | `187.55.77.125` |

---

## Repositórios GitHub

| Repo | Conteúdo | Subdomínio |
|---|---|---|
| `T-Riego/condon.streamlit` | App Streamlit (Fase 1 MVP) | `condon.streamlit.riegos.dev` |
| `T-Riego/condon.web` | React/Vite frontend | `condon.web.riegos.dev` |
| `T-Riego/condon.api` | FastAPI backend | `condon.api.riegos.dev` |

CI/CD: push na branch `main` → GitHub Actions (`appleboy/ssh-action`) → SSH na VPS → `git pull` + `docker compose up --build -d`

**Secrets necessários em cada repo GitHub:**
- `VPS_HOST` = `187.55.77.125`
- `VPS_USER` = `root`
- `VPS_PASSWORD` = senha do root

---

## Fase 1 — Streamlit MVP (`app/`)

### Status: ✅ construído, pronto para subir

**Stack:** Python 3.11 + Streamlit + dados mock (SQLite pendente)

### Arquivos

| Arquivo | Função |
|---|---|
| `app/app.py` | Dashboard: 4 cards, tabela de APs, ações rápidas |
| `app/core/arredondamentos.py` | Motor de cálculos (ROUND/ROUNDDOWN/ROUNDUP do Excel) |
| `app/data/mock_data.py` | Dados reais Abril/2026 |
| `app/utils/formatters.py` | `brl()`, `m3()`, badges |
| `app/pages/1_Leituras.py` | AP 201 = 3 campos; demais = 2 |
| `app/pages/2_COPASA.py` | Conta COPASA + custo/m³ + histórico |
| `app/pages/3_Despesas.py` | Despesas + rateio ao vivo |
| `app/pages/4_Conferencia.py` | Checklist interativo |
| `app/pages/5_Pagamentos.py` | Pendentes/Pagos + registro |
| `app/pages/6_Historico.py` | Gráfico + estatísticas |
| `app/Dockerfile` | Container Python 3.11-slim |
| `app/docker-compose.yml` | Label Traefik: `condon.streamlit.riegos.dev` |
| `app/.github/workflows/deploy.yml` | CI/CD: push → VPS |

### Fórmula de rateio (validada)

```python
parcial = ROUND(total_despesas / 14, 2)   # → R$ 305,43  (abril/2026 com total corrigido)
sindico  = ROUND(parcial / 13, 2)          # → R$ 23,49  (extra por unidade)
final    = parcial + sindico + fundo       # → R$ 462,74 ✅
```

**Dados Abril/2026 validados:**

| AP | Água m³ | Água/Esgt R$ | Gás m³ | Gás R$ | Rateio R$ | Total R$ |
|---|---|---|---|---|---|---|
| 201 | 21,886 | 281,88 | 0,000 | 0,00 | 462,74 | 745,00 |
| 202 | 16,763 | 215,24 | 2,741 | 103,82 | 462,74 | 782,00 |
| 301 | 19,759 | 253,65 | 4,059 | 153,73 | 462,74 | 871,00 |
| 401 | 25,559 | 329,05 | 1,414 | 53,56 | 462,74 | 846,00 |
| ... | | | | | | |
| Total arrecadar | | | | | | **R$ 10.172,00** |

---

## Fase 2 — React/Vite Frontend (`pixel-perfect-replica/`)

### Status: ✅ construído, pronto para subir

**Stack:** React 18 + Vite + TypeScript + Tailwind + shadcn/ui + Sonner + React Router

### Páginas implementadas

| Rota | Arquivo |
|---|---|
| `/` | `Index.tsx` — Dashboard |
| `/competencias/:anoMes` | `Competencia.tsx` |
| `/competencias/:anoMes/leituras` | `Leituras.tsx` |
| `/competencias/:anoMes/copasa` | `Copasa.tsx` |
| `/competencias/:anoMes/despesas` | `Despesas.tsx` |
| `/competencias/:anoMes/conferencia` | `Conferencia.tsx` |
| `/competencias/:anoMes/pagamentos` | `Pagamentos.tsx` |
| `/historico` | `Historico.tsx` |
| `/configuracoes` | `Configuracoes.tsx` |

### Componentes principais

`Sidebar`, `MobileHeader`, `BottomNav`, `AppLayout`, `ThemeToggle`, `MoneyDisplay`, `MeterInput`, `StatusBadge`, `ApartmentBadge`, `CompetenciaCard`

### Tema claro/escuro ✅

- `src/hooks/use-theme.tsx` — Context + localStorage + `prefers-color-scheme`
- `src/components/ThemeToggle.tsx` — `variant="icon"` (mobile) / `variant="labeled"` (desktop)
- Desktop: botão na Sidebar (seção APARÊNCIA)
- Mobile: ícone no MobileHeader entre título e avatar

### Deploy

| Arquivo | Função |
|---|---|
| `Dockerfile` | Multi-stage: Node build → nginx serve |
| `nginx.conf` | SPA fallback + cache de assets |
| `docker-compose.yml` | Label Traefik: `condon.web.riegos.dev` |
| `.github/workflows/deploy.yml` | CI/CD: push → VPS |

---

## FastAPI Backend (`api/`)

### Status: ✅ estrutura criada + router valores_devidos, aguarda schema no Supabase

**Stack:** FastAPI + uvicorn + supabase-py + pydantic-settings

### Estrutura

```
api/
├── supabase_schema.sql      ← EXECUTAR no Supabase SQL Editor
├── requirements.txt
├── .env                     ← gitignored (credenciais reais)
├── .env.example
├── Dockerfile
├── docker-compose.yml       ← Label Traefik: condon.api.riegos.dev
├── .github/workflows/deploy.yml
└── app/
    ├── main.py              ← FastAPI + CORS
    ├── config.py            ← settings via .env
    ├── database.py          ← cliente Supabase singleton
    ├── core/arredondamentos.py
    └── routers/
        ├── competencias.py  ← GET/POST/PATCH
        ├── leituras.py      ← GET/PUT/bulk
        ├── despesas.py        ← GET/POST/DELETE + GET /rateio
        ├── pagamentos.py      ← GET/POST/PATCH recibo-enviado
        ├── copasa.py          ← GET/PUT + GET /historico
        └── valores_devidos.py ← GET/PUT upsert
```

### Variáveis de ambiente (api/.env — não commitar)

```
SUPABASE_URL=https://mgkyqailpawykhzsidxd.supabase.co
SUPABASE_SERVICE_KEY=<service_role key>
ALLOWED_ORIGINS=https://condon.web.riegos.dev,http://localhost:5173
```

---

## Banco de dados Supabase

### Status: ⏳ schema criado, aguarda execução no SQL Editor

**Tabelas definidas em `api/supabase_schema.sql`:**

| Tabela | Conteúdo |
|---|---|
| `apartamentos` | 14 unidades + flags `participa_rateio`, `participa_sindico` |
| `moradores` | Nome, email, telefone, flag síndico |
| `medidores` | Água/gás por AP (AP 201 tem 3 medidores) |
| `competencias` | Mês/ano + status (aberta/conferida/fechada) |
| `leituras` | Anterior + atual + consumo calculado (generated column) |
| `conta_copasa` | Consumo total + valores + custo/m³ |
| `abastecimento_gas` | Compras de gás (kg → m³ calculado) |
| `despesas` | NF, retenção, seguro, síndico, fundo reserva |
| `valores_devidos` | Resultado calculado por AP por competência |
| `pagamentos` | Registro de pagamentos + controle de recibo |
| `fundo_reserva` | Saldo mensal (saldo_final = generated column) |

Dados iniciais já inseridos no schema: 14 apartamentos, moradores, medidores, competência Abril/2026, fundo reserva R$ 40.130,60.

---

## Infraestrutura VPS (`infra/`)

### Status: ⏳ arquivos prontos, aguarda execução na VPS

| Arquivo | Função |
|---|---|
| `infra/docker-compose.yml` | Traefik (:8090 interno) + Portainer (:9000) |
| `infra/traefik.yml` | Config estática: Docker provider, entrypoint web |
| `infra/nginx-condon.conf` | Blocos nginx para os 3 novos subdomínios |
| `infra/setup-vps.sh` | Script único de setup: rede Docker + SSL + nginx |

---

## Bugs corrigidos

### AP 201 — gás piscina

```typescript
// Antes: atual: 870.000 → consumo = 24,78 m³ ❌
// Depois: atual: 845.220 → consumo = 0,000 m³ ✅
```

### Fórmula de rateio em Despesas.tsx

```typescript
// Antes: excluía fundo do total base → ~R$ 292 ❌
// Depois: total inclui tudo ÷ 14, fundo somado no final → R$ 462,74 ✅
const parcial       = +(total / 14).toFixed(2);
const sindico_extra = +(parcial / 13).toFixed(2);
const rateio_final  = +(parcial + sindico_extra + fundoValor).toFixed(2);
```

---

## O que foi feito (Sessão 2 — 27/04/2026)

### ✅ GitHub Secrets configurados
`VPS_HOST`, `VPS_USER`, `VPS_PASSWORD` nos 3 repos (`T-Riego/condon.streamlit`, `condon.web`, `condon.api`).

### ✅ Camada de API React completa (React Query)

**Novos arquivos em `pixel-perfect-replica/src/`:**

| Arquivo | Função |
|---|---|
| `lib/api.ts` | Cliente HTTP com Bearer token Supabase + transform API→domínio |
| `hooks/use-competencias.ts` | `useCompetencias`, `useCompetencia`, `useCreateCompetencia` |
| `hooks/use-leituras.ts` | `useLeituras`, `useUpsertLeitura`, `useBulkUpsertLeituras` |
| `hooks/use-copasa.ts` | `useCopasa`, `useUpsertCopasa` |
| `hooks/use-despesas.ts` | `useDespesas`, `useRateio`, `useCreateDespesa`, `useDeleteDespesa` |
| `hooks/use-pagamentos.ts` | `usePagamentos`, `useRegistrarPagamento`, `useMarcarReciboEnviado` |
| `hooks/use-valores-devidos.ts` | `useValoresDevidos`, `useUpsertValorDevido` |

**Páginas migradas para API real:**
- `Leituras.tsx` → `useLeituras` + `useBulkUpsertLeituras` (botão Salvar conectado)
- `Copasa.tsx` → `useCopasa` + `useUpsertCopasa` (carrega do banco, salva no banco)
- `Despesas.tsx` → `useDespesas` + `useRateio` + `useCreateDespesa` + `useDeleteDespesa`
- `Pagamentos.tsx` → `usePagamentos` + `useValoresDevidos` (fallback mock) + `useRegistrarPagamento`

### ✅ API FastAPI — router valores_devidos
`app/routers/valores_devidos.py`: GET `/valores-devidos/{competencia_id}` e PUT `/valores-devidos/`.

---

## Próximos passos

1. **⚠️ MANUAL — Executar `supabase_schema.sql`** no Supabase SQL Editor:
   - Acesse `supabase.com` → projeto `mgkyqailpawykhzsidxd` → SQL Editor
   - Cole `api/supabase_schema.sql` → Run

2. **⚠️ MANUAL — Setup VPS:**
   ```bash
   # Na VPS como root
   mkdir -p /opt/condon
   git clone https://github.com/T-Riego/condon.streamlit /opt/condon/streamlit
   git clone https://github.com/T-Riego/condon.web       /opt/condon/web
   git clone https://github.com/T-Riego/condon.api       /opt/condon/api
   # Copiar infra/
   scp -r infra/ root@187.55.77.125:/opt/condon/infra
   # Criar .env na api
   cat > /opt/condon/api/.env << EOF
   SUPABASE_URL=https://mgkyqailpawykhzsidxd.supabase.co
   SUPABASE_SERVICE_KEY=<service_role_key>
   ALLOWED_ORIGINS=https://condon.web.riegos.dev,http://localhost:5173
   EOF
   # Setup infra
   bash /opt/condon/infra/setup-vps.sh
   ```

3. **Criar usuário Supabase Auth** `riegosdev@gmail.com` / `Doidos@18` no dashboard
4. **Push main** nos 3 repos → CI/CD deploya automaticamente

---

## Pendências de funcionalidade

- [ ] Executar schema Supabase (manual)
- [ ] Setup VPS (manual)
- [ ] Criar usuário inicial no Supabase Auth
- [ ] SQLite → Supabase: importar histórico Feb/2023 → Mar/2026
- [ ] Geração de PDFs (ReportLab): planilha geral, AP 201, AP 601, 17 recibos
- [ ] Valor por extenso em Python (substitui macro VBA `Extenso()`)
- [ ] Router `valores_devidos` precisa de colunas com `$` no nome — verificar compatibilidade supabase-py
