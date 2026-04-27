### Consumo condominial

O consumo condominial é a diferença entre o consumo total da conta e a soma dos consumos individualizados dos apartamentos.

consumo_condominial = consumo_total_conta - soma_consumo_individual

### Rateio do consumo condominial

O consumo condominial pode incluir, por exemplo:

- água usada pela faxineira;
- consumo comum do condomínio.

Esse valor deve ser rateado entre as **14 unidades habitacionais**.

rateio_consumo_condominial_por_unidade = valor_consumo_condominial / 14

---

## 4.4 Etapa 4 — Taxa de Esgoto

A taxa de esgoto deve ser proporcional ao consumo individual de água.

### Regra

O uso de esgoto deve seguir uma regra de três simples, considerando o consumo de água individualizado.

percentual_consumo_unidade = consumo_agua_unidade / soma_consumo_agua_individual  
valor_esgoto_unidade = valor_total_esgoto * percentual_consumo_unidade

### Conferência

A soma dos percentuais deve fechar em 100%.

soma_percentuais = 100%

Se não fechar, o sistema deve indicar erro ou necessidade de ajuste por arredondamento.

---

## 4.5 Etapa 5 — Cálculo de Gás

Existe uma tabela específica para gás.

### Dados citados

- abastecimento de dois cilindros grandes;
- exemplo histórico: 320 kg de gás;
- valor de exemplo: R$ 15,14 por kg;
- fator fixo de conversão: 2,5 kg/m³.

### Regra de conversão

volume_m3 = quantidade_kg / 2.5

### Regra de custo

custo_m3_gas = valor_total_gas / volume_m3

### Cálculo por unidade

valor_gas_unidade = consumo_gas_unidade_m3 * custo_m3_gas

---

## 4.6 Etapa 6 — Tabela 2: Consolidação de Água, Esgoto e Gás

A Tabela 2 consolida os dados vindos da Tabela 1.

### Função

- consolidar consumo individual;
- calcular percentuais;
- calcular valores proporcionais;
- calcular consumo condominial;
- preparar dados para a Tabela 3.

### Deve conter

- unidade habitacional;
- consumo de água;
- percentual de consumo de água;
- valor de água;
- valor de esgoto;
- consumo de gás;
- valor de gás;
- rateio de consumo condominial;
- total parcial por unidade.

### Regras

- A soma dos percentuais deve ser 100%.
- O consumo condominial deve ser identificado separadamente.
- Diferenças de centavos devem ser tratadas por ajuste de arredondamento.
- Os dados consolidados alimentam a Tabela 3.

---

## 4.7 Etapa 7 — Lançamento de Despesas

Mensalmente são lançadas despesas do condomínio.

### Exemplos de despesas

- manutenção;
- seguro do prédio;
- honorários da contadora;
- retenções federais;
- retenções municipais;
- manutenção de elevador;
- serviço do síndico;
- fundo de reserva.

### Regras

- O que for rateável deve ser dividido entre as **14 unidades habitacionais**.
- O pagamento do serviço do síndico pode ter regra específica:
    - rateio geral por 14 unidades;
    - rateio parcial por 13 unidades.
- Retenções federais e municipais são responsabilidade do condomínio.
- A contadora gera o DARF para os cálculos finais.

---

## 4.8 Etapa 8 — Tabela 3: Valores Devidos por Unidade

A Tabela 3 é a tabela final de cálculo.

### Função

- consolidar todos os valores devidos por unidade;
- manter fórmulas protegidas;
- validar se os cálculos fecham;
- gerar base para recibos.

### Deve conter

- unidade habitacional;
- valor de água;
- valor de esgoto;
- valor de gás;
- rateios condominiais;
- serviço do síndico;
- fundo de reserva;
- outras despesas;
- total devido;
- status de conferência;
- status de recibo.

### Regra de conferência

A conferência deve resultar em zero.

diferença_conferência = total_a_ratear - soma_valores_calculados

Se o resultado for diferente de zero:

diferença_conferência != 0

então existe erro ou ajuste pendente.

---

## 5. Controle de Pagamentos

A planilha de pagamentos registra os dados reais de pagamento.

### Campos sugeridos

- `id`
- `competencia`
- `unidade_habitacional_id`
- `valor_devido`
- `valor_pago`
- `data_pagamento`
- `forma_pagamento`
- `numero_recibo`
- `recibo_enviado`
- `nome_pagador`
- `documento_pagador`
- `observacoes`

### Observação

O recibo pode receber dados de quem efetivamente pagou.

Exemplo citado:

- a filha de Paulo pode pagar por ele;
- nesse caso, os dados do pagador precisam ser inseridos manualmente.

---

## 6. Recibos

## 6.1 Geração de Recibo

O sistema atual gera recibos a partir das planilhas mensais.

### No app, o recibo deve ser gerado com base em:

- competência;
- unidade habitacional;
- valores calculados;
- dados do responsável;
- dados do pagador, quando diferente;
- número do recibo;
- data de pagamento;
- forma de pagamento.

### Saída

- PDF final.

---

## 6.2 Envio de Recibo

O sistema deve permitir marcar:

- recibo gerado;
- recibo enviado;
- data de envio;
- observações.

---

## 7. Histórico

## 7.1 Histórico de Medições e Copasa

Atualmente, Tiago copia mensalmente a última linha da planilha de cálculos para um arquivo de armazenamento.

### No app, deve existir histórico mensal para:

- leituras;
- consumos;
- valores de água;
- valores de esgoto;
- valores de gás;
- despesas;
- rateios;
- pagamentos;
- recibos.

### Regra

O histórico deve permitir recuperar dados de meses anteriores.

---

## 7.2 Banco de Dados Legado

Existe necessidade de manter dados históricos vindos das planilhas.

### No app, deve haver:

- importação manual ou assistida;
- preservação dos dados antigos;
- possibilidade de consulta por competência;
- possibilidade de auditoria.

---

## 8. Conferência Mensal

Existe uma área chamada “Orientações e Conf”, com função de orientar e confirmar se o processo mensal foi feito.

### O app deve ter checklist mensal.

## 8.1 Checklist sugerido

- Medições realizadas.
- Leituras conferidas.
- Consumo de água calculado.
- Consumo de gás calculado.
- Conta Copasa lançada.
- Custo por m³ calculado.
- Taxa de esgoto calculada.
- Consumo condominial calculado.
- Despesas lançadas.
- Retenções lançadas.
- DARF informado pela contadora, quando aplicável.
- Fundo de reserva conferido.
- Rateio calculado.
- Tabela final conferida.
- Diferença de conferência igual a zero.
- Recibos gerados.
- Recibos enviados.
- Histórico mensal salvo.

---

## 9. Módulos do App

## 9.1 Cadastro

### Funcionalidades

- cadastrar unidades habitacionais;
- cadastrar moradores;
- cadastrar medidores;
- configurar participação em rateios;
- configurar casos especiais.

---

## 9.2 Medições

### Funcionalidades

- criar competência mensal;
- registrar leituras;
- calcular consumos;
- permitir anotações;
- conferir leituras;
- bloquear edição após fechamento, se necessário.

---

## 9.3 Água e Copasa

### Funcionalidades

- lançar conta de água;
- lançar consumo total da conta;
- calcular custo por m³;
- calcular consumo condominial;
- calcular valor de água por unidade;
- calcular esgoto proporcional;
- conferir totais.

---

## 9.4 Gás

### Funcionalidades

- lançar abastecimento de gás;
- registrar quantidade em kg;
- registrar valor total;
- converter kg para m³;
- calcular custo por m³;
- calcular valor por unidade.

---

## 9.5 Despesas e Rateios

### Funcionalidades

- lançar despesas mensais;
- classificar despesa;
- definir se entra no rateio;
- definir base de rateio:
    - 14 unidades;
    - 13 unidades;
    - outro critério configurável;
- lançar retenções;
- lançar fundo de reserva;
- calcular total a ratear.

---

## 9.6 Fechamento Mensal

### Funcionalidades

- consolidar valores por unidade;
- verificar diferenças;
- aplicar arredondamentos;
- travar fechamento;
- gerar resumo final.

---

## 9.7 Pagamentos

### Funcionalidades

- registrar pagamento;
- informar pagador;
- informar forma de pagamento;
- informar data;
- informar número do recibo;
- marcar recibo como enviado.

---

## 9.8 Recibos e PDFs

### Funcionalidades

- gerar recibo individual;
- gerar PDF;
- gerar relatórios mensais;
- exportar arquivos;
- controlar envio.

---

## 9.9 Histórico

### Funcionalidades

- consultar competências anteriores;
- consultar consumo por unidade;
- consultar valores pagos;
- consultar recibos;
- manter base histórica;
- importar dados legados das planilhas.

---

## 10. Regras de Negócio Consolidadas

## 10.1 Quantidade de unidades

total_unidades_habitacionais = 14

## 10.2 Rateio geral

valor_por_unidade = valor_total_rateavel / 14

## 10.3 Rateio parcial do síndico

valor_por_unidade_sindico = valor_total_sindico / 13

## 10.4 Consumo individual

consumo = leitura_atual - leitura_anterior

## 10.5 Consumo condominial de água

consumo_condominial = consumo_total_conta - soma_consumo_individual

## 10.6 Esgoto proporcional

percentual_unidade = consumo_agua_unidade / soma_consumo_agua_individual  
valor_esgoto_unidade = valor_total_esgoto * percentual_unidade

## 10.7 Conversão de gás

gas_m3 = gas_kg / 2.5

## 10.8 Conferência final

diferenca = total_a_ratear - soma_total_por_unidade

A diferença deve ser:

diferenca = 0

Se não for zero, o fechamento não deve ser considerado conferido.

---

## 11. Telas Sugeridas

## 11.1 Dashboard

- competência atual;
- status do fechamento;
- medições pendentes;
- despesas pendentes;
- recibos pendentes;
- diferença de conferência.

## 11.2 Unidades Habitacionais

- lista dos 14 apartamentos;
- moradores;
- medidores vinculados;
- regras especiais.

## 11.3 Medições

- água;
- gás;
- leitura anterior;
- leitura atual;
- consumo calculado;
- observações.

## 11.4 Copasa / Água

- lançamento da conta;
- consumo total;
- valor total;
- custo por m³;
- esgoto;
- consumo condominial;
- rateio.

## 11.5 Gás

- abastecimentos;
- kg;
- m³;
- custo por m³;
- consumo por apartamento.

## 11.6 Despesas

- despesas mensais;
- retenções;
- fundo de reserva;
- serviço do síndico;
- base de rateio.

## 11.7 Fechamento

- valores por unidade;
- total por apartamento;
- conferência;
- ajustes;
- fechamento da competência.

## 11.8 Pagamentos

- valor devido;
- valor pago;
- pagador;
- data;
- forma de pagamento;
- recibo.

## 11.9 Recibos

- gerar PDF;
- visualizar recibo;
- marcar como enviado.

## 11.10 Histórico

- competências anteriores;
- consumo;
- valores;
- pagamentos;
- recibos.

---

## 12. Dados que Precisam Ser Confirmados Depois

Os arquivos indicam pontos ainda incompletos ou que precisam ser detalhados.

### Pendências

- lista exata dos 14 apartamentos;
- identificação de todos os medidores;
- regra completa do apartamento 201 e piscina;
- fórmula final usada para o síndico;
- significado de “cg10”;
- significado de “f105”;
- modelo exato do recibo;
- três tipos de planilhas enviadas aos condôminos;
- regras específicas para Lucas e Clara;
- regra exata para não cobrança de centavos;
- formato desejado do PDF final;
- estrutura do banco de dados legado;
- campos obrigatórios para importação das planilhas antigas.

---

## 13. MVP do App

## 13.1 Primeira versão obrigatória

A primeira versão do app deve permitir:

1. cadastrar 14 unidades habitacionais;
2. cadastrar medidores de água e gás;
3. criar uma competência mensal;
4. lançar leituras;
5. calcular consumo individual;
6. lançar conta de água/Copasa;
7. calcular custo por m³;
8. calcular esgoto proporcional;
9. calcular consumo condominial;
10. lançar consumo e custo de gás;
11. lançar despesas mensais;
12. calcular rateios;
13. gerar total devido por unidade;
14. validar diferença de conferência;
15. registrar pagamento;
16. gerar recibo em PDF;
17. salvar histórico mensal.

---

## 14. Objetivo Final

Criar um app que substitua ou organize o fluxo atual de planilhas, mantendo a lógica já usada por Tiago, mas com:

- menos risco de erro;
- histórico estruturado;
- cálculos automáticos;
- conferência mensal;
- geração de recibos;
- controle de pagamentos;
- preservação das regras específicas do condomínio;
- suporte obrigatório às 14 unidades habitacionais.