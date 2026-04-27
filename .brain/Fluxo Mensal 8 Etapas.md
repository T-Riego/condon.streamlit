# Fluxo Mensal — 8 Etapas

> Pipeline completo executado todo mês pelo Robson.

## Etapa 1 — Coleta de Leituras (dias 27-29)
- Robson lê medidores de água e gás nos 14 APs
- Usa celular Android com lanterna
- Registra em [[Planilha - AGUA E GAS LEITURAS]]
- AP 201: 2 medidores (unidade + piscina)

## Etapa 2 — Tabela 1: Consumos
- `consumo = leitura_atual - leitura_anterior`
- Detecta anomalias (dupla diferença)
- Totaliza consumo individual e geral
- Planilha: [[Planilha - MEDICOES E TABELAS]] linhas 4-86

## Etapa 3 — Cálculo Água/COPASA
- Lança conta COPASA (abastecimento + recurso hídrico + esgoto)
- Calcula custo/m³: `valor_total / consumo_total`
- Calcula consumo condominial: `total_copasa - soma_individual`
- Planilha: [[Planilha - MEDICOES E TABELAS]] colunas AV-BF

## Etapa 4 — Esgoto Proporcional
- Regra de 3: `%_unidade = consumo_agua / soma_individual`
- Soma dos % deve = 100%
- Se não fechar → ajuste de arredondamento
- Ver [[Formulas e Arredondamentos]]

## Etapa 5 — Cálculo de Gás
- Conversão: `m³ = kg / 2.5`
- Custo/m³: `preço_kg × 2.5`
- Por unidade: `consumo_m3 × custo_m3`
- AP 201 especial: soma gás apt + gás piscina
- Planilha: [[Planilha - MEDICOES E TABELAS]] colunas CA-CG

## Etapa 6 — Tabela 2: Consolidação
- Junta água + esgoto + gás por unidade
- Inclui linha "CONDOMÍNIO" (residual)
- Verificação: soma % = 100%, diferenças = 0
- Planilha: [[Planilha - MEDICOES E TABELAS]] colunas T-AA

## Etapa 7 — Lançamento de Despesas
- NFs mensais (conservadora, elevador, luz, seguro, contadora, internet...)
- Retenções federais/municipais (DARF da contadora)
- Síndico: rateio entre 13 APs
- Fundo reserva: R$150/AP/mês
- Planilha: [[Planilha - LANCTºS]]
- Cálculo rateio: [[Rateio e Despesas]]

## Etapa 8 — Tabela 3: Valores Finais
- Total = `ROUNDUP(água + gás + rateio, 0)` → sem centavos
- Verificação: `total_ratear - soma_calculada = 0`
- Gera 3 PDFs: geral, AP 201, AP 601
- Gera 17 recibos
- Planilha: [[Planilha - MEDICOES E TABELAS]] linhas 145-163
- Saída: [[Planilha - PLAN P COND]]

## Checklist Final (aba ORIENTACOES E CONF.)
7 verificações cruzadas entre abas → CONFERIDO/PENDENTE

---
**Tags**: #fluxo #processo #mensal
