# Pendências Abertas

> Itens que precisam ser confirmados com Robson antes ou durante a implementação.

## Prioridade Alta (bloqueiam implementação)

- [ ] **Senha do Adm.xlsx** — Arquivo criptografado AES-256. Pode conter dados relevantes.
- [ ] **Quem são Lucas e Clara?** — Quais APs? O que muda na planilha deles?
- [ ] **Qual AP é do síndico (Robson)?** — Para configurar `participa_rateio_sindico = False`
- [ ] **AP 201 gás: tem medidor de água da piscina também?** — Na planilha só aparece "201 GAS PISC." (gás), mas a reunião menciona "piscina" de forma genérica

## Prioridade Média (podem ser definidos durante Sprint 2)

- [ ] **Nomes completos de todos os 14 moradores** — Para recibos e cadastro
- [ ] **CPFs dos moradores** — Para recibos
- [ ] **Dados completos de pagamento AP 601** — Nome completo do dono (cond) e email
- [ ] **Formato exato do recibo em PDF** — Reproduzir layout ou modernizar?
- [ ] **Regra de crédito AP 801** — Quando se aplica? Sempre tem saldo?

## Prioridade Baixa (Fase 2)

- [ ] **Envio automático por WhatsApp** — Robson quer? Quais APs?
- [ ] **Email dos moradores** — Para envio automático
- [ ] **Outros condomínios** — Pretende expandir o sistema?
- [ ] **Acesso multi-usuário** — Robson admin + Tiago dev + contadora view?
- [ ] **Importação dos dados legados** — Desde quando? Fev/2023 está na planilha histórica
- [ ] **Tarifas COPASA por faixa** — A planilha tem simulação oculta (cols BH-BX). Usar?

## Resolvidas (pela análise)

- [x] Lista exata dos 14 APs → 201-802
- [x] "cg10" → célula CG10, custo/m³ gás
- [x] "f105" → célula F105, rateio final
- [x] Regra centavos → ROUNDUP(total, 0)
- [x] 3 tipos de planilha → geral, 201, 601
- [x] Fórmula síndico → total/14 + (total/14)/13
- [x] Modelo recibo → 17 abas com VBA Extenso()

---
**Tags**: #pendencias #aberto #confirmar
