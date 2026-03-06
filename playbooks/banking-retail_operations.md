# Banking (Retail) × Operations Playbook

## Visão Geral
Em bancos de varejo no Brasil, Operações é o motor que sustenta abertura de contas, onboarding, pagamentos, PIX, cartões, crédito, prevenção a fraude, backoffice regulatório e atendimento de exceções. A operação normalmente é distribuída entre centrais (matriz), polos regionais e células especializadas, com alta dependência de SLAs, filas, reconciliação e controles de risco.

O ambiente regulatório (BACEN, LGPD, regras de PLD/FT, auditoria interna e externa) exige rastreabilidade total, trilha de aprovação e evidências confiáveis. Ao mesmo tempo, a pressão competitiva de bancos digitais e fintechs obriga ganhos de velocidade e redução de custo operacional sem ampliar headcount no mesmo ritmo.

Nesse contexto, a monday.com AI Work Platform permite unificar contexto operacional (mondayDB), reduzir handoffs entre áreas e criar fluxos com automações, dashboards e copiloto (Sidekick). A camada de agentes (monday AI Agents, em breve) habilita operações semi-autônomas para triagem, priorização, investigação e escalonamento.

## Mapeamento de Value Drivers

| Value Driver | Aderência em Banking (Retail) × Operations | Por quê |
|---|---|---|
| 1) Substituir/Aumentar Headcount com AI | Alta | Grande volume de tarefas repetitivas (triagem, reconciliação, tratamento de exceções) permite automação e copiloto operacional. |
| 2) Consolidar stack com AI | Alta | Operações costuma usar várias planilhas + e-mail + sistemas legados; unificação reduz retrabalho e perda de contexto. |
| 3) Escalar impacto sem overhead | Muito Alta | Crescimento de transações (PIX/cartões) exige escala com controle de risco e compliance sem crescer times proporcionalmente. |

## Casos de Uso Priorizados

---

### Caso de Uso 1: Torre de Controle de Exceções Operacionais (PIX, TED, Boleto, Cartões)

**Relevância:** Alta  
**Value Driver:** 3) Escalar impacto sem overhead

#### A Dor
Exceções de liquidação e falhas de processamento chegam por múltiplos canais e times. Falta priorização única por risco/impacto, gerando atrasos de SLA, retrabalho e aumento de reclamações (incluindo Bacen/Consumidor.gov).

#### A Solução
Centralizar exceções em um board de Operações com tipificação, criticidade, dono, prazo regulatório e causa-raiz; automações para roteamento por tipo de ocorrência; dashboards executivos por fila/SLA/reincidência; integrações para alertas em Slack/Teams/e-mail.

#### O Resultado
Redução de 25–40% no tempo médio de resolução (TMR), queda de 20–30% em violações de SLA e melhora de NPS operacional em jornadas críticas.

#### Perguntas de Descoberta
- Quais tipos de exceção mais estouram SLA hoje (PIX devolução, chargeback, liquidação)?
- Onde vocês perdem mais tempo: triagem inicial, coleta de evidências ou aprovação?
- Qual percentual de casos retorna para retrabalho por falta de dados?
- Como vocês priorizam eventos com risco regulatório versus impacto financeiro?
- Quais filas dependem de planilhas/e-mail para seguir?

#### Contexto da Indústria
Em varejo bancário brasileiro, eventos de alto volume (PIX e cartões) amplificam gargalos de operação. Exceções precisam de trilha auditável e priorização baseada em risco, não apenas ordem de chegada.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Crie um app de Torre de Controle de Exceções Operacionais para banco de varejo no Brasil. Board principal chamado 'Exceções Operacionais'. Colunas: ID da Ocorrência (texto), Tipo de Exceção (dropdown: PIX, TED, Boleto, Cartão, Cadastro, Crédito), Criticidade (status: Baixa, Média, Alta, Crítica), Valor Financeiro (número BRL), Cliente Impactado (texto), Canal de Origem (dropdown), Data/Hora de Abertura (data e hora), SLA Limite (data e hora), Dono da Resolução (pessoas), Squad Responsável (dropdown), Status (status: Novo, Em Triagem, Em Investigação, Aguardando Evidência, Em Aprovação, Resolvido, Encerrado), Causa Raiz (dropdown), Ação Corretiva (texto longo), Regulatório Sensível (checkbox), Escalação Necessária (checkbox). Automations: 1) Quando Criticidade mudar para Crítica, notificar gestor e criar item em board 'Escalações'. 2) Quando Tipo de Exceção for PIX e Valor Financeiro > 100000, marcar Escalação Necessária. 3) Quando estiver a 2 horas do SLA Limite e Status não for Resolvido/Encerrado, alertar dono no Slack. 4) Quando Status mudar para Resolvido, solicitar validação de QA Operacional. Views: Kanban por Status, Tabela por Squad, Dashboard com TMR, % SLA cumprido, Top Causas Raiz e Valor em Risco." 

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Agente de Priorização de Exceções

**Agent Purpose:**  
Priorizar automaticamente exceções por risco operacional, regulatório e financeiro.

**Triggers:**
- Novo item criado em Exceções Operacionais
- Mudança de Criticidade para Alta/Crítica
- SLA próximo do vencimento
- Campo Regulatório Sensível marcado
- Atualização de Valor Financeiro

**Actions:**
- Classificar risco composto (SLA + valor + regulatório)
- Sugerir fila e dono ideais
- Recomendar pacote mínimo de evidências
- Disparar alerta de escalonamento quando necessário
- Gerar resumo executivo do caso para liderança

**Data Required:**
- Campos do board de Exceções
- Histórico de resolução por tipo/causa
- Regras internas de SLA e alçadas
- Integração com canal de alertas

**Autonomy Level:** Human-in-the-Loop  
O agente prioriza e recomenda; o supervisor confirma decisões de escalonamento crítico.

**Example Interaction:**
> Uma ocorrência de PIX de alto valor entra com dados incompletos. O agente identifica risco alto por valor e proximidade de SLA, classifica como prioridade P1 e recomenda dono da célula de pagamentos em tempo real.
>
> Em seguida, ele gera checklist de evidências faltantes (comprovante de liquidação, logs transacionais, validação antifraude) e notifica o gestor de plantão. Com isso, o time evita atraso regulatório e reduz o tempo de triagem inicial.

#### 🧠 AGENT INSTRUCTION CARD (v3)

```json
{
  "role": "Agente de Priorização de Exceções",
  "roleDescription": "Prioriza automaticamente exceções por risco operacional, regulatório e financeiro.",
  "goal": "Reduzir TMR e violações de SLA em exceções críticas.",
  "tools": ["mondayDB", "automações de status", "dashboards", "integrações de notificação"],
  "triggers": ["novo item", "criticidade alta/crítica", "SLA próximo", "regulatório sensível", "valor atualizado"],
  "user_prompt": "Atue como analista de operações bancárias, classifique risco em tempo real, recomende dono e próximos passos, e escale somente quando critérios de risco forem atendidos."
}
```

---

### Caso de Uso 2: Orquestração de Onboarding e KYC de Conta Pessoa Física

**Relevância:** Alta  
**Value Driver:** 1) Substituir/Aumentar Headcount com AI

#### A Dor
Onboarding costuma ter gargalos de validação documental e checagens KYC, com múltiplas dependências entre operações, risco e compliance. Isso aumenta abandono de abertura de conta e custo por conta ativada.

#### A Solução
Board de jornada KYC com etapas, pendências, SLA e alçadas; automações para pedidos de complemento documental; visão de funil por etapa e motivos de reprovação; templates operacionais por perfil de cliente.

#### O Resultado
Queda de 20–35% no lead time de onboarding e redução de 15–25% no custo operacional por conta aprovada.

#### Perguntas de Descoberta
- Onde está o maior gargalo do onboarding hoje?
- Qual taxa de abandono por etapa de validação?
- Quantos casos ficam parados por documentação incompleta?
- Como vocês registram trilha de decisão para auditoria?

#### Contexto da Indústria
No Brasil, onboarding precisa equilibrar experiência digital com robustez de compliance (KYC/PLD), mantendo evidências auditáveis.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Crie um app de Onboarding e KYC para banco de varejo brasileiro. Board 'Onboarding PF'. Colunas: Protocolo, CPF, Canal, Etapa KYC, Status, Pendência Documental, SLA Etapa, Analista, Risco Inicial, Decisão Compliance, Motivo Reprovação, Data Aprovação. Automations para: lembrete automático de pendência em 24h, escalonamento se SLA vencer, e solicitação de revisão de compliance para risco alto. Views: funil por etapa, painel de SLA, dashboard de conversão e reprovação." 

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Agente de Triagem KYC

**Agent Purpose:**  
Fazer pré-triagem de dossiês de onboarding e indicar pendências críticas.

**Triggers:**
- Novo dossiê recebido
- Documento anexado
- Mudança de etapa KYC

**Actions:**
- Verificar completude documental
- Sugerir risco inicial
- Priorizar análise por SLA
- Criar tarefas de follow-up

**Data Required:**
- Campos de onboarding/KYC
- Regras internas de documentação
- Histórico de reprovação

**Autonomy Level:** Human-in-the-Loop  
A decisão final permanece com compliance.

**Example Interaction:**
> O agente recebe 300 dossiês no pico da campanha de aquisição. Ele separa automaticamente os casos completos, destaca inconsistências comuns e monta fila de prioridade por prazo.
>
> Analistas passam a atuar só em exceções relevantes, acelerando aprovações sem reduzir controle.

#### 🧠 AGENT INSTRUCTION CARD (v3)

```json
{
  "role": "Agente de Triagem KYC",
  "roleDescription": "Pré-tria dossiês de onboarding e indica pendências críticas.",
  "goal": "Acelerar onboarding com conformidade e menos retrabalho.",
  "tools": ["boards de onboarding", "automações de SLA", "dashboards"],
  "triggers": ["novo dossiê", "documento anexado", "mudança de etapa KYC"],
  "user_prompt": "Classifique rapidamente completude, risco inicial e prioridade de análise; encaminhe exceções para compliance com contexto completo."
}
```

---

### Caso de Uso 3: Gestão de Chargeback e Contestação em Cartões

**Relevância:** Alta  
**Value Driver:** 2) Consolidar stack com AI

#### A Dor
Processos de chargeback se fragmentam entre adquirência, emissor, atendimento e jurídico, com baixa padronização de evidências e perdas evitáveis por prazo perdido.

#### A Solução
Fluxo único de contestação com playbooks por motivo de chargeback, checklist de evidências, calendário de prazos e dashboards por bandeira/motivo/perda evitável.

#### O Resultado
Redução de 10–20% em perdas por chargeback evitável e aumento de produtividade por analista.

#### Perguntas de Descoberta
- Qual taxa de perda por prazo perdido?
- Quais motivos de chargeback mais recorrentes?
- Onde as evidências falham hoje?

#### Contexto da Indústria
Chargeback em varejo bancário exige disciplina de prazo e documentação; ganhos rápidos vêm de padronização e visibilidade ponta a ponta.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Monte um app de Gestão de Chargeback para banco de varejo no Brasil com board principal, checklist de evidências por motivo, prazos por bandeira e dashboard de perdas evitáveis. Inclua automações de alerta D-2 para prazo final e bloqueio de encerramento sem evidência mínima." 

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Agente de Dossiê de Chargeback

**Agent Purpose:**  
Garantir dossiês completos e dentro do prazo de contestação.

**Triggers:**
- Novo caso de chargeback
- Prazo D-2
- Falta de evidência crítica

**Actions:**
- Validar checklist por motivo
- Solicitar anexos faltantes
- Priorizar casos por risco de perda
- Escalar casos de alto valor

**Data Required:**
- Motivo, valor, prazo, bandeira
- Evidências anexadas

**Autonomy Level:** Escalation-Based  
Atua sozinho até limites definidos; escala casos críticos.

**Example Interaction:**
> Ao detectar caso de alto valor com prazo D-2 sem comprovante, o agente abre alerta crítico, aciona responsável e sugere pacote de evidência obrigatório.

#### 🧠 AGENT INSTRUCTION CARD (v3)

```json
{
  "role": "Agente de Dossiê de Chargeback",
  "roleDescription": "Garante dossiês completos e dentro do prazo.",
  "goal": "Reduzir perdas evitáveis em chargeback.",
  "tools": ["board de chargeback", "checklists", "automações de alerta"],
  "triggers": ["novo caso", "prazo D-2", "evidência faltante"],
  "user_prompt": "Monitore prazos e completude documental, priorize por risco financeiro e escale casos críticos cedo."
}
```

---

### Caso de Uso 4: Reconciliação Diária de Liquidação e Quebras

**Relevância:** Alta  
**Value Driver:** 1) Substituir/Aumentar Headcount com AI

#### A Dor
Reconciliação diária entre sistemas gera alto trabalho manual, atrasos de fechamento e risco de quebra não tratada dentro da janela operacional.

#### A Solução
Workflow de reconciliação com filas por criticidade, trilha de investigação e playbook de tratamento por tipo de quebra.

#### O Resultado
Redução de 30–50% no esforço manual de reconciliação e menor exposição a perdas por quebra aberta.

#### Perguntas de Descoberta
- Quantas quebras ficam abertas além de D+1?
- Quais tipos de divergência são mais recorrentes?
- Quanto tempo da equipe vai para reconciliação manual?

#### Contexto da Indústria
Liquidação e reconciliação em bancos de varejo têm alto impacto em risco operacional e fechamento financeiro diário.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Crie um app de Reconciliação Diária para operações bancárias, com board de quebras, classificação por origem e criticidade, automações de escalonamento para quebras acima de R$ 50 mil e dashboard de aging de quebras." 

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Agente de Investigação de Quebras

**Agent Purpose:**  
Ajudar a priorizar e orientar investigação de divergências de reconciliação.

**Triggers:**
- Nova quebra registrada
- Quebra acima de limite de valor
- Aging acima de 24h

**Actions:**
- Classificar severidade
- Sugerir hipóteses de causa-raiz
- Recomendar trilha de investigação
- Escalar para gestor de risco operacional

**Data Required:**
- Valor da quebra, sistema origem, aging
- Histórico de causas e resolução

**Autonomy Level:** Human-in-the-Loop

**Example Interaction:**
> O agente detecta quebra acima de R$ 80 mil e aging de 18h. Ele sugere investigação prioritária no sistema de origem, indica causa provável com base em histórico e dispara alerta para liderança.

#### 🧠 AGENT INSTRUCTION CARD (v3)

```json
{
  "role": "Agente de Investigação de Quebras",
  "roleDescription": "Prioriza e orienta investigação de divergências de reconciliação.",
  "goal": "Reduzir aging de quebras e risco operacional.",
  "tools": ["board de reconciliação", "dashboards de aging", "automações de escalonamento"],
  "triggers": ["nova quebra", "valor alto", "aging > 24h"],
  "user_prompt": "Identifique rapidamente as quebras críticas, sugira hipóteses de causa e conduza a equipe para resolução dentro da janela operacional."
}
```

---

### Caso de Uso 5: Monitoramento de SLAs Operacionais e Alertas Proativos

**Relevância:** Média-Alta  
**Value Driver:** 3) Escalar impacto sem overhead

#### A Dor
Sem visibilidade em tempo real de SLAs por fila, equipes descobrem violações tarde e reagem de forma manual.

#### A Solução
Cockpit de SLAs com semáforos por processo, alertas preditivos e rituais operacionais diários orientados por dados.

#### O Resultado
Redução de incidentes de SLA, maior previsibilidade e melhor capacidade de gestão por exceção.

#### Perguntas de Descoberta
- Quais SLAs são mais críticos para negócio e regulador?
- Vocês atuam preventivamente ou só após ruptura?
- Quanto tempo líderes gastam consolidando status manualmente?

#### Contexto da Indústria
Em operações bancárias, a confiabilidade operacional é diferencial competitivo e mitigador de risco reputacional.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Crie um cockpit de SLAs Operacionais para banco de varejo no Brasil, com board de processos críticos, metas de SLA por processo, alertas automáticos de risco de ruptura e dashboard executivo por regional e squad." 

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Agente Guardião de SLA

**Agent Purpose:**  
Antecipar risco de ruptura de SLA e recomendar ações preventivas.

**Triggers:**
- Tendência de atraso detectada
- Pico de volume acima do normal
- SLA em risco nas próximas 2 horas

**Actions:**
- Alertar líder com priorização
- Recomendar rebalanceamento de fila
- Abrir plano de contingência
- Registrar lição operacional

**Data Required:**
- Volume por fila
- Capacidade por squad
- Histórico de performance de SLA

**Autonomy Level:** Escalation-Based

**Example Interaction:**
> O agente detecta aumento anormal em exceções de cartões e projeta ruptura de SLA em 90 minutos. Ele recomenda rebalancear analistas, aciona contingência e evita ruptura em janela crítica.

#### 🧠 AGENT INSTRUCTION CARD (v3)

```json
{
  "role": "Agente Guardião de SLA",
  "roleDescription": "Antecipar risco de ruptura de SLA e recomendar ações preventivas.",
  "goal": "Evitar violações de SLA em operações bancárias críticas.",
  "tools": ["dashboards", "automações de alerta", "boards de capacidade"],
  "triggers": ["tendência de atraso", "pico de volume", "SLA em risco"],
  "user_prompt": "Monitore continuamente risco de SLA, recomende ações preventivas práticas e escale cedo para evitar ruptura."
}
```

## Terminologia da Indústria

| Termo | Definição |
|---|---|
| KYC | Know Your Customer; validação de identidade e elegibilidade do cliente. |
| PLD/FT | Prevenção à Lavagem de Dinheiro e Financiamento do Terrorismo. |
| Chargeback | Contestação de transação de cartão com possível estorno. |
| Reconciliação | Conciliação entre registros de sistemas/transações/liquidação. |
| SLA | Acordo de nível de serviço com meta de prazo/qualidade. |
| Backoffice Operacional | Time que trata processamento, exceções e controles transacionais. |

## Papéis Típicos de Stakeholders

| Papel | Responsabilidade | Influência |
|---|---|---|
| Head de Operações | Performance fim a fim, custo e qualidade operacional | Alta |
| Gerente de Backoffice | Gestão de filas, SLA e produtividade | Alta |
| Compliance/PLD | Conformidade regulatória e trilha de auditoria | Alta |
| Risco Operacional | Mitigação de perdas e eventos críticos | Média-Alta |
| TI/Arquitetura | Integrações e governança técnica | Média |

## Departamentos Adjacentes

| Departamento | Conexão | Oportunidade |
|---|---|---|
| Compliance | Regras, auditoria e alçadas | Fluxos auditáveis e evidência automatizada |
| Atendimento | Entrada de incidentes e reclamações | Menos retrabalho e melhor handoff |
| Produto | Mudanças em jornada e processos | Fechar ciclo de melhoria contínua |
| Risco/Fraude | Priorização de eventos sensíveis | Resposta mais rápida a anomalias |

## Panorama Competitivo

| Ferramenta | Posicionamento | Oportunidade de Substituição |
|---|---|---|
| Planilhas + e-mail | Gestão ad-hoc e fragmentada | Unificar contexto, reduzir erros e retrabalho |
| ITSM genérico | Bom para tickets, fraco em contexto de negócio bancário | Personalização rápida com Vibe + mondayDB |
| BPM tradicional | Forte em rigidez processual, lento para adaptar | Iteração rápida e ownership operacional |

## Tratamento de Objeções

| Objeção | Resposta |
|---|---|
| "Já temos sistemas legados para isso" | monday.com não substitui core bancário; orquestra trabalho, exceções e decisão entre sistemas com visibilidade ponta a ponta. |
| "É arriscado mexer em operação crítica" | Começamos por uma fila de alto impacto com governança e trilha de auditoria, medindo SLA/TMR antes de escalar. |
| "Nossa operação é complexa demais" | A complexidade é exatamente onde a unificação de contexto + automação gera mais ganho e menos retrabalho. |

## Provas de Valor
*(A preencher com referências de clientes)*
- Referência de banco digital com melhora de SLA operacional
- Referência de operação com redução de tempo de triagem
- Referência de consolidação de ferramentas em operações críticas

---

*Generated: 2026-03-06 | Version: 3.0 (with Vibe Prompts + Enhanced Agent Instruction Cards)*
