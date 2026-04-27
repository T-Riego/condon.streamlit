# Instruções para o Lovable — Sistema ADM Condomínio Neápolis

## Visão Geral do Projeto

Crie um sistema web **mobile-first** para administração do **Condomínio Residencial Neápolis** (BH/MG). O sistema substitui planilhas Excel e deve ser usado principalmente pelo **síndico Robson** no celular Android.

**Idioma**: Português brasileiro em toda a interface.

---

## Stack e Tecnologia

- **React + Vite + TypeScript**
- **Tailwind CSS** + **shadcn/ui** para componentes
- **React Router** para navegação
- **React Hook Form + Zod** para formulários e validação
- **TanStack Query** para estado assíncrono
- **Recharts** para gráficos
- Design **mobile-first**, responsivo para desktop também
- PWA-ready (manifest + service worker básico)

> O backend (FastAPI + PostgreSQL) será desenvolvido separadamente. Por enquanto, use **dados mockados** em todos os lugares onde haveria chamadas de API.

---

## Entidades de Dados

### Apartamentos (fixos — 14 unidades)
```
201, 202, 301, 302, 401, 402, 501, 502, 601, 602, 701, 702, 801, 802
```

### Casos especiais por apartamento
- **AP 201**: Tem 2 medidores de gás (unidade + piscina). Desconto de internet de R$ 65,00.
- **AP 601**: Pagamento separado — condomínio para um dono, fundo de reserva para outro (Gilberto Augusto Beltrão).
- **AP 801**: Controle de saldo acumulado (Alberto Jacomini de Souza).
- **Síndico**: Recebe rateio dividido entre 13 unidades (não paga para si mesmo). Identificar qual AP é do síndico.

### Modelos de dados principais

```typescript
// Competência mensal
interface Competencia {
  id: string
  ano_mes: string        // "202604"
  data_vencimento: string
  status: "aberta" | "conferida" | "fechada"
  oficio_numero?: string
}

// Leitura de medidor
interface Leitura {
  id: string
  competencia_id: string
  apartamento: string    // "201", "302", etc.
  tipo: "agua" | "gas"
  identificador: string  // "agua_201", "gas_201_apt", "gas_201_piscina"
  leitura_anterior: number
  leitura_atual: number
  consumo: number        // leitura_atual - leitura_anterior
  data_medicao: string
}

// Conta COPASA
interface ContaCopasa {
  id: string
  competencia_id: string
  consumo_total_m3: number
  valor_agua: number
  valor_esgoto: number
  valor_recurso_hidrico: number
  valor_total: number
  custo_por_m3: number
  data_vencimento: string
}

// Despesa mensal
interface Despesa {
  id: string
  competencia_id: string
  descricao: string
  valor: number
  tipo: "NF" | "retencao" | "seguro" | "sindico" | "fundo_reserva" | "outros"
  rateavel: boolean
  base_rateio: 14 | 13
  informar_condominos: boolean
}

// Valor devido por unidade
interface ValorDevido {
  id: string
  competencia_id: string
  apartamento: string
  agua_consumo_m3: number
  agua_esgoto_valor: number
  gas_consumo_m3: number
  gas_valor: number
  rateio_valor: number
  total_exato: number
  total_arredondado: number   // ROUNDUP sem centavos
  observacoes?: string
}

// Pagamento
interface Pagamento {
  id: string
  valor_devido_id: string
  apartamento: string
  competencia_id: string
  valor_pago: number
  data_pagamento: string
  forma_pagamento: "pix" | "boleto" | "dinheiro" | "transferencia"
  numero_recibo?: string
  recibo_enviado: boolean
  nome_pagador: string
  observacoes?: string
}
```

---

## Telas do Sistema

### 1. Dashboard (tela inicial)

**Rota**: `/`

**Conteúdo**:
- Card de destaque mostrando a **competência atual** (mês/ano) e seu status
- Indicador colorido de status: 🟡 Aberta → 🔵 Conferida → 🟢 Fechada
- Cards de resumo rápido:
  - Total arrecadado no mês atual
  - Nº de unidades pagas / pendentes
  - Fundo de reserva (saldo atual: R$ 40.130,60 nos dados mock)
- Lista compacta dos **últimos 3 meses** com link para cada competência
- Botão FAB (floating) "+ Nova Competência" no canto inferior direito

**Dados mock**:
- Competência atual: Abril/2026 (status: "aberta")
- Saldo fundo reserva: R$ 40.130,60
- 5 unidades pagas, 9 pendentes

---

### 2. Competência — Detalhes

**Rota**: `/competencias/:anoMes`

**Conteúdo** (abas ou seções com scroll):

#### Aba "Resumo"
- Status atual com botão para avançar status (Aberta → Conferida → Fechada)
- Tabela com todos os 14 apartamentos:
  - Colunas: AP | Água m³ | Água/Esgoto R$ | Gás m³ | Gás R$ | Rateio R$ | **Total R$** | Status pagt.
  - Linha de total geral
  - Badge colorido de pagamento: ✅ Pago / ⏳ Pendente / ❌ Atrasado
- Cards de totais: Total despesas | Rateio/unidade | Fundo reserva

#### Aba "Leituras"
- Ver tela 3 (Entrada de Leituras)

#### Aba "Despesas"
- Ver tela 5 (Lançamento de Despesas)

#### Aba "Conferência"
- Ver tela 6 (Checklist)

---

### 3. Entrada de Leituras (tela mobile principal)

**Rota**: `/competencias/:anoMes/leituras`

Esta é a **tela mais importante para uso mobile em campo** (Robson usa no celular enquanto caminha pelo condomínio lendo os medidores).

**Layout**:
- Título: "Leituras — [mês/ano]"
- Progresso: "8 de 15 medidores registrados" com barra de progresso
- Lista de cartões, um por medidor, agrupados por apartamento (201 → 802)
- Cada cartão mostra:
  - Identificador do medidor (ex: "Água — AP 201", "Gás — AP 201 (Piscina)")
  - Leitura anterior (cinza, somente leitura)
  - Campo de input numérico grande (para digitar com polegar) com teclado numérico
  - Consumo calculado em tempo real: `leitura_atual - leitura_anterior` (aparece ao digitar)
  - Indicador ✅ salvo / 📝 pendente
- Botão fixo no rodapé: "Salvar Todas as Leituras"

**UX importante**:
- Inputs grandes (mínimo 48px altura) para uso com polegar
- Foco automático no próximo campo ao confirmar
- Consumo negativo deve mostrar alerta vermelho (erro de leitura)
- AP 201 deve mostrar **3 campos**: Água, Gás Apt, Gás Piscina

**Dados mock — Abril/2026** (leituras já salvas para mostrar na tela):
```
AP    | Água m³  | Gás m³
201   | 21,886   | 0,000 (gás 0 = só piscina)
202   | 16,763   | 2,741
301   | 19,759   | 4,059
302   | 19,988   | 2,429
401   | 25,559   | 1,414
402   | 23,777   | 4,820
501   | 25,421   | 1,213
502   | 13,441   | 1,029
601   |  3,979   | 0,582
602   |  0,682   | 0,130
701   | 13,458   | 0,785
702   |  7,190   | 3,761
801   |  4,531   | 0,423
802   | 14,109   | 2,440
COND  | 18,457   | —     (consumo condominial residual — calculado)
```

---

### 4. Conta COPASA

**Rota**: `/competencias/:anoMes/copasa`

**Formulário**:
- Consumo total m³
- Valor água (R$)
- Valor esgoto (R$)
- Valor recurso hídrico (R$)
- Valor total (R$) — calculado automaticamente
- Custo/m³ calculado em tempo real (valor_total / consumo_total)
- Data de vencimento
- Upload de foto da conta (campo opcional, só UI)

**Dados mock — Abril/2026**:
- Consumo total: 214,543 m³
- Valor total: R$ 2.757,65 (incluindo água + esgoto + recurso hídrico)

---

### 5. Lançamento de Despesas

**Rota**: `/competencias/:anoMes/despesas`

**Layout**:
- Lista de despesas já lançadas com total acumulado
- Botão "+ Adicionar Despesa"
- Modal/drawer para nova despesa:
  - Descrição (texto livre)
  - Valor R$
  - Tipo (select): NF | Retenção | Seguro | Síndico | Fundo Reserva | Outros
  - Rateável? (toggle) — se sim, dividir entre 14 ou 13 unidades
  - Informar condôminos? (toggle)
- Resumo do rateio ao vivo:
  - Total despesas: R$ X
  - Rateio parcial (÷14): R$ X
  - Síndico (÷13): R$ X
  - Fundo reserva: R$ 150,00
  - **Rateio final por unidade: R$ X**

**Dados mock — Abril/2026**:
```
Despesas totais: R$ 4.065,65
Rateio parcial: R$ 290,40
Rateio síndico: R$ 22,34
Fundo reserva: R$ 150,00
Rateio final: R$ 462,74
```

---

### 6. Checklist de Conferência

**Rota**: `/competencias/:anoMes/conferencia`

Lista de verificação interativa (checkboxes) que o Robson marca antes de fechar o mês:

```
[ ] Todas as leituras de água registradas (15 medidores)
[ ] Todas as leituras de gás registradas (15 medidores)
[ ] Conta COPASA lançada
[ ] Despesas do mês lançadas
[ ] Cálculos conferidos (soma dos totais bate com total geral)
[ ] Planilhas PDF geradas
[ ] Recibos PDF gerados
[ ] Pagamentos registrados
[ ] Recibos enviados a todos os condôminos
[ ] Competência fechada
```

- Progresso: "7 de 10 itens conferidos"
- Barra de progresso colorida (vermelho → amarelo → verde)
- Botão "Fechar Competência" só aparece quando todos os itens estão marcados

---

### 7. Controle de Pagamentos

**Rota**: `/competencias/:anoMes/pagamentos`

**Layout**:
- Duas abas: "Pendentes" | "Pagos"
- Cada card de apartamento mostra:
  - Número do AP e nome do morador (mock)
  - Valor a pagar (em destaque)
  - Status: ⏳ Pendente / ✅ Pago
  - Se pago: data, forma, nº recibo
- Ao tocar num apartamento pendente: drawer com formulário:
  - Valor pago
  - Data do pagamento
  - Forma de pagamento (PIX | Boleto | Dinheiro | Transferência)
  - Nº do recibo
  - Nome do pagador
  - Toggle "Recibo enviado"

**Resumo no topo**:
- Barra: "5 pagos / 9 pendentes"
- Total recebido: R$ X.XXX,00
- Total pendente: R$ X.XXX,00

---

### 8. Histórico de Competências

**Rota**: `/historico`

- Lista de todas as competências processadas (do mais recente para o mais antigo)
- Cada item: mês/ano | status | total arrecadado | nº unidades pagas
- Filtro por ano
- Link para detalhes de cada competência
- Gráfico de barras (últimos 12 meses): total arrecadado por mês

---

### 9. Configurações / Perfil

**Rota**: `/configuracoes`

- Informações do condomínio (somente leitura):
  - Nome: Residencial Neápolis
  - CNPJ: 09.408.714/0001-08
  - Banco Inter, AG 0001, CC 26620410-4
  - PIX: CNPJ
- Usuário logado: Robson (Síndico)
- Botão de logout (só UI)

---

## Navegação

### Bottom navigation bar (mobile) — sempre visível:
```
🏠 Dashboard  |  📅 Competência  |  💧 Leituras  |  💰 Pagamentos  |  ☰ Mais
```

### Sidebar (desktop):
- Dashboard
- Competência Atual
  - Leituras
  - Conta COPASA
  - Despesas
  - Conferência
  - Pagamentos
- Histórico
- Configurações

---

## Design System

### Cores
- **Primária**: Azul escuro `#1E3A5F` (confiança, seriedade)
- **Secundária**: Azul médio `#2E86AB`
- **Sucesso**: Verde `#27AE60`
- **Alerta**: Amarelo âmbar `#F39C12`
- **Erro**: Vermelho `#E74C3C`
- **Background**: Cinza claro `#F5F7FA`
- **Card**: Branco `#FFFFFF`
- **Texto primário**: `#1A1A2E`
- **Texto secundário**: `#6B7280`

### Tipografia
- Fonte principal: Inter (Google Fonts)
- Títulos: 700 weight
- Corpo: 400 weight
- Valores monetários: **negrito**, sempre com 2 casas decimais formatadas em pt-BR (ex: R$ 1.234,56)

### Componentes reutilizáveis necessários
1. `MoneyDisplay` — exibe valor em R$ com formatação pt-BR
2. `ApartmentBadge` — badge colorido com número do AP
3. `StatusBadge` — badge de status (aberta/conferida/fechada/pago/pendente)
4. `CompetenciaCard` — card compacto de competência para listas
5. `MeterInput` — input numérico grande para leituras em campo (mobile-friendly)
6. `PaymentDrawer` — drawer lateral para registrar pagamento

---

## Dados Mock Completos (Abril/2026)

Use estes dados para popular toda a aplicação:

```typescript
// Valores por apartamento — Abril/2026
const dadosAbril2026 = [
  { ap: "201", agua_m3: 21.886, agua_r: 281.88, gas_m3: 0.000, gas_r: 0.00,   rateio: 462.74, total: 745  },
  { ap: "202", agua_m3: 16.763, agua_r: 215.24, gas_m3: 2.741, gas_r: 103.82, rateio: 462.74, total: 782  },
  { ap: "301", agua_m3: 19.759, agua_r: 253.65, gas_m3: 4.059, gas_r: 153.73, rateio: 462.74, total: 871  },
  { ap: "302", agua_m3: 19.988, agua_r: 256.59, gas_m3: 2.429, gas_r: 92.00,  rateio: 462.74, total: 812  },
  { ap: "401", agua_m3: 25.559, agua_r: 329.05, gas_m3: 1.414, gas_r: 53.56,  rateio: 462.74, total: 846  },
  { ap: "402", agua_m3: 23.777, agua_r: 305.87, gas_m3: 4.820, gas_r: 182.56, rateio: 462.74, total: 952  },
  { ap: "501", agua_m3: 25.421, agua_r: 326.78, gas_m3: 1.213, gas_r: 45.94,  rateio: 462.74, total: 836  },
  { ap: "502", agua_m3: 13.441, agua_r: 173.17, gas_m3: 1.029, gas_r: 38.97,  rateio: 462.74, total: 675  },
  { ap: "601", agua_m3:  3.979, agua_r:  50.68, gas_m3: 0.582, gas_r: 22.04,  rateio: 462.74, total: 536  },
  { ap: "602", agua_m3:  0.682, agua_r:   8.79, gas_m3: 0.130, gas_r: 4.92,   rateio: 462.74, total: 477  },
  { ap: "701", agua_m3: 13.458, agua_r: 173.29, gas_m3: 0.785, gas_r: 29.73,  rateio: 462.74, total: 666  },
  { ap: "702", agua_m3:  7.190, agua_r:  91.93, gas_m3: 3.761, gas_r: 142.45, rateio: 462.74, total: 698  },
  { ap: "801", agua_m3:  4.531, agua_r:  58.51, gas_m3: 0.423, gas_r: 16.02,  rateio: 462.74, total: 538  },
  { ap: "802", agua_m3: 14.109, agua_r: 181.86, gas_m3: 2.440, gas_r: 92.42,  rateio: 462.74, total: 738  },
]
// COND (condominial): água 18,457 m³ — residual, não cobra

// Totais Abril/2026
// Despesas: R$ 4.065,65
// Rateio parcial (÷14): R$ 290,40
// Rateio síndico (÷13): R$ 22,34
// Fundo reserva: R$ 150,00
// Rateio final por unidade: R$ 462,74
// Fundo de reserva acumulado: R$ 40.130,60
```

---

## Regras de Negócio (para exibição correta na UI)

1. **Totais sem centavos**: O "Total R$" de cada apartamento é sempre número inteiro (ex: R$ 782,00, não R$ 781,93). Isso é intencional — o sistema arredonda para cima.
2. **Consumo condominial**: A linha "COND" na tabela de leituras é o residual (total COPASA menos soma dos apartamentos). Exibir em cinza/itálico.
3. **AP 201 — 2 medidores de gás**: Mostrar sempre dois campos separados na tela de leituras.
4. **AP 601 — pagamento duplo**: Na tela de pagamentos, indicar visualmente que este AP tem dois recebedores diferentes.
5. **Formatação monetária**: Sempre `R$ 1.234,56` (ponto como separador de milhar, vírgula como decimal).
6. **Formatação de m³**: Sempre 3 casas decimais (ex: `21,886 m³`).

---

## O que NÃO incluir nesta versão

- Lógica real de cálculo (apenas exibir dados mock)
- Geração de PDFs (apenas botões de UI com toast "Em breve")
- Envio de WhatsApp/email (apenas botões com toast "Em breve")
- Autenticação real (apenas tela de login mockada, já "logado" como Robson)
- Integração com backend

---

## Entregável esperado

Uma aplicação React funcional e navegável com:
- Todas as 9 telas descritas acima
- Navegação funcional entre telas
- Dados mock de Abril/2026 populando a interface
- Design mobile-first responsivo
- Componentes shadcn/ui com Tailwind CSS
- Formatação monetária em pt-BR
