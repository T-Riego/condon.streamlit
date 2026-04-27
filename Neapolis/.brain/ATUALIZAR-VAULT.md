# Instruções para Atualizar o Vault

> Para Claude: use este guia quando o contexto estiver perto de 90% ou ao final de sessões produtivas.

---

## Quando Atualizar

- Contexto da sessão > ~80-85% (para garantir tempo de escrever)
- Ao concluir um sprint ou etapa importante
- Ao descobrir novas regras de negócio das planilhas
- Ao resolver uma pendência

---

## O Que Atualizar

### Sempre verificar:

1. **[[04-Plano/Pendencias]]** — mover resolvidas para a seção "Resolvidas", adicionar novas
2. **[[HOME]]** — atualizar "Status Atual" com fase/sprint correntes
3. **[[04-Plano/Plano-Execucao]]** — marcar tarefas concluídas

### Se houve descoberta técnica:

4. **[[01-Regras/Formulas-Criticas]]** — adicionar fórmula nova ou corrigir existente
5. **[[01-Regras/Arredondamentos]]** — se novos arredondamentos foram identificados
6. **[[01-Regras/Casos-Especiais]]** — se novos casos especiais foram descobertos

### Se houve mudança de plano:

7. **[[03-Tecnico/Stack]]** — se stack mudou
8. **[[03-Tecnico/Modelo-Dados]]** — se modelo foi revisado

---

## Como Reportar para o Usuário

Ao final da atualização, diga:

```
Vault atualizado. Mudanças desta sessão:
- [Pendencia X] marcada como resolvida
- [Nova regra Y] adicionada em [[01-Regras/...]]
- Status em [[HOME]] atualizado para Sprint N
Para continuar em nova sessão: abra .brain no Obsidian e leia HOME.md
```

---

## Estrutura do Vault

```
.brain/
  HOME.md                          ← Índice central + status atual
  CLAUDE.md                        ← Overview técnico do projeto
  ATUALIZAR-VAULT.md               ← Este arquivo

  01-Regras/
    Fluxo-Mensal.md                ← 8 etapas do ciclo mensal
    Formulas-Criticas.md           ← Fórmulas Python exatas
    Arredondamentos.md             ← Mapa de ROUND/ROUNDDOWN/ROUNDUP
    Casos-Especiais.md             ← AP 201, 601, 801, síndico, recibos

  02-Dados/
    Planilhas-Fonte.md             ← Mapa dos 5 arquivos Excel
    Dados-Teste-Abril2026.md       ← Dados reais para testes de regressão

  03-Tecnico/
    Stack.md                       ← Decisão de stack + estrutura de pastas
    Modelo-Dados.md                ← Entidades e relacionamentos

  04-Plano/
    Plano-Execucao.md              ← Sprints 1-3 (Fase 1) + Fase 2
    Criterios-Sucesso.md           ← 8 critérios de aceitação + testes
    Pendencias.md                  ← Bloqueantes e pendências abertas
```
