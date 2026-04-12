

<br>
 
 \[[🇧🇷 Português](README.pt_BR.md)\] \[**[🇬🇧 English](README.md)**\]
 


<br><br>

# AI Incidents in Financial Services

Análise de Viés Algorítmico, Risco Operacional e Governança de IA em Serviços Financeiros

<br><br>

## Table of Contents

1. Visão Geral do Projeto
1.1 Contexto de Negócio
1.2 Objetivo Geral
1.3 Objetivos Específicos
1.4 Perguntas de Pesquisa
2. Dados e Definição do Problema
2.1 Fonte de Dados: AI Incident Database (AIID)
2.2 Escopo: Recorte de Serviços Financeiros
2.3 Variáveis Brutas Principais
2.4 Conceitos Analíticos Centrais
3. Variáveis Derivadas e Modelo de Dados
3.1 Tipo de Aplicação Financeira (application_type)
3.2 Tipo de Incidente (incident_type)
3.3 Segmento de Cliente (customer_segment)
3.4 Nível de Severidade (severity_level)
3.5 Atributos Complementares
4. Estrutura do Projeto e Notebooks
4.1 Notebook 1 – Preparação de Dados
4.2 Notebook 2 – Análise Exploratória
4.3 Notebook 3 – Feature Engineering e Base Analítica
4.4 Notebook 4 – Consolidação e Reporting
5. Alinhamento com CRISP‑DM
6. Como Executar
7. Código dos Notebooks (com indicação de gráficos)
7.1 Notebook 1 – Data Preparation
7.2 Notebook 2 – Exploratory Analysis
7.3 Notebook 3 – Feature Engineering
7.4 Notebook 4 – Consolidation and Reporting
8. Próximos Passos e Extensões Possíveis
9. Autor e Contexto
10. Tópicos (Tags)

<br><br>

## 1. Visão Geral do Projeto

### 1.1 Contexto de Negócio

Desenvolvemos este projeto sob a perspectiva de uma boutique de consultoria especializada em risco de IA aplicada ao setor financeiro. Nossa proposta é apoiar bancos, fintechs e demais organizações na identificação de padrões de incidente, no mapeamento de vulnerabilidades sistêmicas e na transformação de eventos históricos em inteligência acionável para governança, compliance e mitigação de risco.

O projeto utiliza dados do Artificial Intelligence Incident Database (AIID) para construir uma base analítica focada em serviços financeiros, com ênfase em aplicações como concessão de crédito, detecção de fraude, avaliação de risco, automação bancária, pagamentos, seguros e contextos correlatos. A partir dessa base, estruturamos variáveis analíticas, realizamos exploração descritiva inicial e preparamos o pipeline para análises estatísticas, modelagem preditiva e exposição dos resultados via API ou serviços de dados.

Do ponto de vista de negócio, o problema que endereçamos é a ausência de visibilidade estruturada sobre riscos reais de IA em operações financeiras. Muitas instituições já utilizam modelos algorítmicos em decisões sensíveis, mas ainda carecem de mecanismos robustos para entender onde estão seus maiores riscos, quais aplicações demandam supervisão reforçada, quais grupos podem estar mais expostos a viés e como priorizar controles preventivos com base em evidências.

Nesta fase exploratória, o foco está em organizar a base, criar variáveis derivadas, compreender padrões iniciais e consolidar um pipeline claro, pronto para ser expandido em direção a modelos preditivos, dashboards e APIs.

<br>
