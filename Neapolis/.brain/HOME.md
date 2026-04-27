# 🏢 Neápolis — Central do Projeto

> Sistema de administração do Condomínio Residencial Neápolis — BH/MG
> Substituição das planilhas Excel por aplicação web/mobile.

---

## Navegação Rápida

| Área | Nota |
|------|------|
| Visão Geral do Projeto | [[CLAUDE]] |
| Fluxo Mensal (8 etapas) | [[01-Regras/Fluxo-Mensal]] |
| Fórmulas Críticas | [[01-Regras/Formulas-Criticas]] |
| Arredondamentos (CRÍTICO) | [[01-Regras/Arredondamentos]] |
| Casos Especiais (201, 601, 801) | [[01-Regras/Casos-Especiais]] |
| Dados de Teste — Abril/2026 | [[02-Dados/Dados-Teste-Abril2026]] |
| Planilhas Fonte (mapa) | [[02-Dados/Planilhas-Fonte]] |
| Stack Tecnológica | [[03-Tecnico/Stack]] |
| Modelo de Dados | [[03-Tecnico/Modelo-Dados]] |
| Plano de Execução (Sprints) | [[04-Plano/Plano-Execucao]] |
| Critérios de Sucesso | [[04-Plano/Criterios-Sucesso]] |
| Pendências Abertas | [[04-Plano/Pendencias]] |

---

## Status Atual

- **Data**: 26/04/2026
- **Fase**: Planejamento concluído — pronto para Sprint 1
- **Próximo passo**: Iniciar motor de cálculos Python (`calc_agua.py`, `calc_gas.py`, etc.)
- **Stack confirmada**: Streamlit MVP → Next.js produção

---

## Contexto Rápido

- **14 apartamentos**: 201-802 (andares 2 a 8, 2 por andar)
- **Administrador**: Robson (síndico)
- **Desenvolvedor**: Tiago (@tiagoriegos2)
- **Banco**: Inter AG 0001, CC 26620410-4, PIX = CNPJ 09.408.714/0001-08
- **Medidores**: 15 água (AP 201 tem 2) + 15 gás

---

## Instruções para Nova Sessão

Ao iniciar uma nova sessão de trabalho neste projeto:
1. Leia este HOME primeiro
2. Consulte [[04-Plano/Pendencias]] para o que está em aberto
3. Consulte [[04-Plano/Plano-Execucao]] para o sprint atual
4. Use os dados reais de [[02-Dados/Dados-Teste-Abril2026]] para validar cálculos
