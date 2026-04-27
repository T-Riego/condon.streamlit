# Plano Base — App de Gestão de Condomínio

## 1. Contexto

O sistema atual é baseado em planilhas usadas para gestão mensal de um condomínio com **14 unidades habitacionais**, isto é, **14 apartamentos**.

O fluxo atual cobre:

- leitura mensal de medidores de água;
- leitura mensal de medidores de gás;
- cálculo de consumo individual;
- cálculo de consumo condominial;
- cálculo proporcional de água, esgoto e gás;
- rateio de despesas;
- controle de pagamentos;
- geração de recibos;
- manutenção de histórico mensal.

---

## 2. Premissas Gerais

### 2.1 Condomínio

- Total de unidades habitacionais: **14 apartamentos**.
- Os rateios gerais devem considerar as **14 unidades habitacionais**, salvo regras específicas.
- Existe caso especial de rateio parcial do serviço do síndico para **13 unidades**.
- O fundo de reserva atual é de **R$ 150,00**, podendo mudar.

### 2.2 Período de Medição

As medições são feitas mensalmente, geralmente nos dias:

- 27;
- 28;
- 29.

O ciclo pode considerar meses de:

- 30 dias;
- 31 dias.

---

## 3. Entidades Principais do App

## 3.1 Unidade Habitacional

Representa cada apartamento do condomínio.

### Campos sugeridos

- `id`
- `numero_apartamento`
- `morador_responsavel`
- `ativo`
- `participa_rateio_geral`
- `participa_rateio_sindico`
- `observacoes`

### Regra

O sistema deve iniciar com **14 unidades habitacionais cadastradas**.

---

## 3.2 Medidor

Representa os medidores de água e gás vinculados às unidades.

### Tipos

- Água
- Gás

### Observação

Há caso especial citado para o apartamento 201, que possui dois medidores:

- um medidor do apartamento;
- um medidor da piscina.

### Campos sugeridos

- `id`
- `unidade_habitacional_id`
- `tipo`
- `identificador`
- `descricao`
- `ativo`

---

## 3.3 Medição Mensal

Registro das leituras mensais dos medidores.

### Campos sugeridos

- `id`
- `competencia`
- `data_medicao`
- `medidor_id`
- `leitura_anterior`
- `leitura_atual`
- `consumo_calculado`
- `observacoes`

### Regras

- O consumo é calculado pela diferença entre leitura atual e leitura anterior.
- O sistema deve permitir anotações rápidas durante a leitura.
- Os resultados devem ser arredondados quando necessário.
- A conferência deve evitar divergências nos totais.

---

## 4. Fluxo Mensal do Sistema

## 4.1 Etapa 1 — Coleta das Leituras

Atualmente, Robson (usuário inicial Adm) realiza mensalmente a leitura dos medidores de água e gás dos 14 apartamentos.

### No app, essa etapa deve permitir:

- selecionar a competência mensal;
- listar todos os apartamentos;
- registrar leitura atual de água;
- registrar leitura atual de gás;
- consultar leitura anterior automaticamente;
- calcular consumo automaticamente;
- registrar observações durante a medição;
- marcar medição como conferida.

---

## 4.2 Etapa 2 — Tabela 1: Leituras e Consumos

A Tabela 1 representa a base de leitura dos medidores.

### Função

- armazenar leituras atuais;
- recuperar leituras anteriores;
- calcular consumo individual;
- enviar dados consolidados para a Tabela 2.

### Dados

- consumo de água por unidade;
- consumo de gás por unidade;
- total de água individualizado;
- total de gás individualizado.

### Regras

- Consumo = leitura atual - leitura anterior.
- Dados da Tabela 1 alimentam a Tabela 2.
- Deve haver arredondamento para evitar diferenças indevidas.
- Deve haver conferência mensal.

---

## 4.3 Etapa 3 — Cálculo de Água e Copasa

A conta de água deve ser decomposta em itens como:

- abastecimento;
- uso de recurso hídrico;
- esgoto;
- demais componentes da conta, quando existirem.

### Cálculo do custo por metro cúbico

O sistema deve calcular quanto custou o metro cúbico de água no mês.

### Regra geral

```text
custo_m3_agua = valor_total_agua / consumo_total_m3
