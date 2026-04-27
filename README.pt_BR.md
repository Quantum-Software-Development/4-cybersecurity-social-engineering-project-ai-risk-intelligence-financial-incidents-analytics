<!-- ======================================= ⚡️ Start DEFAULT HEADER ===========================================  -->


<!-- ========= START LANGUAGE BUTTON ========= -->
<br>

**\[[🇧🇷 Português](README.pt_BR.md)\] \[**[🇬🇧 English](README.md)**\]**

<br><br>
<!-- ========= END LANGUAGE BUTTON ========= -->



<!-- ========= START REPO TITLE ========= -->
# <p align="center"> 🔐 [Incidentes de IA em Bancos, Serviços Financeiros e Fintechs]()

### <p align="center"> Uma Análise de Viés Algorítmico, Risco Operacional e Governança para Conformidade Regulatória


<br><br><br><br>
<!-- ========= END REPO TITLE ========= -->




<p align="center">
  <a href="https://ai-incidents-financial-services.streamlit.app/">
    <img 
      src="https://img.shields.io/badge/AI_Incident_Risk_Dashboard_Banking_and_Financial_Services-Streamlit-brightgreen?logo=streamlit&logoColor=white&style=flat-square" 
      alt="AI Incident Risk Dashboard – Banking & Financial Services"
      style="height: 30px; width: auto;"
    />
  </a>
</p>




<br><br><br><br>

<a href="SEU-LINK-AQUI" target="_blank" rel="noopener noreferrer">
  View Presentation
</a>







<!-- ========= START Institucional INFO ========= -->



<br>

[**Projeto Integrador — 5º Semestre | PUC-SP**]()
[**Institution:**]() Pontifical Catholic University of São Paulo  – Humanistic AI & Data Science 
[**Disciplina**:]()  Segurança Cibernética e Engenharia Social · Sistemas Distribuídos e Aprendizagem de Máquina  
[**Course Repo:**]() INTEGRATED PROJECT: Cybersecurity and Social Engineering
[**Metodologia**:]()  CRISP-DM · **Fonte de Dados**: AI Incident Database (AIID)
[**Professor:**]()  [✨ Eduardo Savino Gomes]()

<br><br>

#

<br><br>
<!-- ========= END Institucional INFO ========= -->

<!-- ========= START BADGES ========= -->

<p align="center">
  <img src="https://img.shields.io/badge/Python-Data%20Science-0fb9b1?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-14b8a6?logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/API-REST-0ea5a4?logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/Machine%20Learning-AI-2dd4bf" />
  <img src="https://img.shields.io/badge/Database-SQL-5eead4?logo=postgresql&logoColor=black" />
</p>

<br><br>
<!-- ========= END START BADGES ========= -->




##  [Visão executiva]()

Este projeto consolida uma visão ponta a ponta sobre incidentes de IA em serviços financeiros, conectando dados públicos do AI Incident Database (AIID) a um pipeline completo de análise, modelagem e exposição via API e dashboard. Do ponto de vista executivo, o trabalho mostra como incidentes dispersos podem ser transformados em indicadores estruturados de risco, com foco em viés algorítmico, risco operacional e respostas de governança, consumidos por um dashboard interativo que lê diretamente a API.

A solução é organizada segundo o referencial **CRISP‑DM**, tratado aqui como modelo de projeto de negócio baseado em dados: partimos de *Business Understanding* (problema, escopo financeiro e questões de risco/compliance), passamos por *Data Understanding* e *Data Preparation* (construção da base temática de incidentes), avançamos para *Modeling* e *Evaluation* (modelos supervisionados e testes de hipóteses) e chegamos ao *Deployment* em uma arquitetura com banco relacional, API RESTful e camada de apresentação.

Além da camada analítica tradicional, o projeto foi desenhado para incorporar uma interface conversacional integrada a modelos da OpenAI/ChatGPT, permitindo que usuários não técnicos interajam com os resultados por meio de linguagem natural, façam perguntas sobre os incidentes e explorem os dados sem precisar conhecer detalhes de SQL, estatística ou machine learning.

A principal contribuição está menos em um modelo “pronto para produção” e mais na arquitetura analítica integrada: da aquisição dos dados à disponibilização de endpoints RESTful e de uma camada de visualização e interação, respeitando limitações da base e deixando claro que, nas condições atuais, os modelos devem ser tratados como prova de conceito, não como ferramenta decisória final.





<br><br>






<!-- ========= START Confidentiality statement ========= -->

> [!IMPORTANT]
> 
> ⚠️ Heads Up
>
> * Projects and deliverables may be made [publicly available]() whenever possible.
>   
> * The course emphasizes [**practical, hands-on experience**]() with real datasets to simulate professional consulting scenarios in the fields of **Machine Learning and Neural Networks** for partner organizations and institutions affiliated with the university.
>   
> * All activities comply with the [**academic and ethical guidelines of PUC-SP**]().
>   
> * Any content not authorized for public disclosure will remain [**confidential**]() and securely stored in [private repositories]().  
> <br>
>
>

<br><br> 

#

<br><br>
<!-- ========= END Confidentiality statement  ========= -->



<!-- ========= START Main Repo REFERENCE  ========= -->
> [!TIP]
>
> This repository is part of the flagship project:
> **🔐 Cybersecurity, Social Engineering & AI Security — Main Hub**
>
> Explore the complete ecosystem of materials, analyses, and notebooks in the central repository:
>
> * 🔗 **[Cybersecurity, Social Engineering & AI Security — Main Hub Repository](https://github.com/Quantum-Software-Development/1-Cybersecurity-SocialEngineering_Main_Hub_Repository-PUCSP)**
>
> *Part of the Humanistic AI Data Modeling Series — where data connects with human insight… and occasionally gets socially engineered. ⚡️

<br><br><br><br>
<!-- ========= END Main Repo REFERENCE  ========= -->


<!-- ======================================= END DEFAULT HEADER ⚡️ ===========================================  -->



<br><br>

## Table of Contents

1. [Introdução](#1-introdução)
2. [Objetivos e Questões de Pesquisa](#2-objetivos-e-questões-de-pesquisa)
3. [Fundamentação e Contexto de Dados](#3-fundamentação-e-contexto-de-dados)
4. [Metodologia — CRISP-DM](#4-metodologia--crisp-dm)
5. [Dados Utilizados e Preparação](#5-dados-utilizados-e-preparação)
6. [Variáveis Analíticas e Hipóteses](#6-variáveis-analíticas-e-hipóteses)
7. [Técnicas Estatísticas e de IA/ML](#7-técnicas-estatísticas-e-de-iaml)
8. [Estrutura Técnica — 5 Notebooks](#8-estrutura-técnica--5-notebooks)
9. [Banco de Dados Relacional e API RESTful](#9-banco-de-dados-relacional-e-api-restful)
10. [Resultados Obtidos](#10-resultados-obtidos)
11. [Cronograma, Entregáveis e Alinhamento ao Briefing](#11-cronograma-entregáveis-e-alinhamento-ao-briefing)
12. [Guia de Instalação e Execução](#12-guia-de-instalação-e-execução)
13. [Estrutura de Arquivos do Projeto](#13-estrutura-de-arquivos-do-projeto)
14. [Limitações, Riscos e Cuidados Metodológicos](#14-limitações-riscos-e-cuidados-metodológicos)
15. [Considerações Finais e Próximos Passos](#15-considerações-finais-e-próximos-passos)
16. [Referências](#16-referências)


<br><br>

## 1. [Introdução]()

<br>

### [1.1]() ***Contextualização do tema***

O uso de sistemas de Inteligência Artificial (IA) no setor financeiro cresceu de forma acelerada em aplicações como concessão de crédito, detecção de fraude, *trading* algorítmico, avaliação de risco e automação de atendimento. Esse avanço cria oportunidades de eficiência e inovação, mas também amplia superfícies de **risco operacional**, **viés algorítmico** e **falhas de governança** em ambientes altamente regulados.

Este projeto parte de incidentes reais de IA documentados em diferentes organizações para construir uma visão estruturada de como esses riscos se manifestam em serviços financeiros, com foco em **viés algorítmico**, **risco operacional** e **respostas de governança** em bancos e fintechs.

<br>

### [1.2]() ***Problema de pesquisa***

Dado um conjunto de incidentes de IA registrados em múltiplos setores e filtrados para o domínio financeiro, o problema central é avaliar se:

- existem **padrões sistemáticos** de viés e risco associados a certos tipos de aplicação de IA (crédito, fraude, *trading*);
- determinados **segmentos de clientes** são desproporcionalmente afetados;
- **respostas de governança** e de reguladores acompanham adequadamente a gravidade dos incidentes.

<br>

### [1.3]() ***Relevância para o setor financeiro e para a governança de IA***

<br>

| [Stakeholder]() | [Benefício Direto]() |
|---|---|
| [**Bancos e Fintechs**]() | Aprimorar gestão de risco operacional e reputacional |
| [**Reguladores**]() | Supervisão baseada em dados e evidências quantitativas |
| [**Gestores de Risco**]() | Ferramentas para avaliar exposição a incidentes de IA |
| [**Compliance**]() | Identificar lacunas regulatórias e priorizar auditorias |
| [**Investidores**]() | Entender impacto de incidentes de IA no valor de instituições |


<br><br>

> [!TIP]
>
> Para a [**governança de IA**](), o projeto ilustra como dados de incidentes podem ser transformados em indicadores, modelos preditivos e APIs, viabilizando monitoramento contínuo e respostas estruturadas a riscos.
>
> <br>

<br><br>


# Sistema de Inteligência de Incidentes Financeiros com IA  
## Arquitetura do Sistema (Design MLOps)

<br>

```mermaid
flowchart TB

subgraph FONTES_DE_DADOS
    A1[Dataset Kaggle - Incidentes Financeiros]
    A2[APIs Externas - Base de Incidentes]
end

subgraph CAMADA_DE_DADOS
    B1[Armazenamento de Dados Brutos]
    B2[Pipeline de Limpeza de Dados]
    B3[Dataset Processado]
end

subgraph ENGENHARIA_DE_FEATURES
    C1[Extração de Features]
    C2[Transformação e Codificação]
    C3[Feature Store Versionada]
end

subgraph PIPELINE_DE_ML
    D1[Treinamento de Modelos]
    D2[Avaliação de Modelos]
    D3[Registro de Modelos]
end

subgraph ARMAZENAMENTO
    E1[(Banco de Dados SQLite)]
    E2[(Modelos Serializados)]
end

subgraph APLICACAO
    F1[API REST - FastAPI / Flask]
    F2[Dashboard Streamlit]
end

A1 --> B1
A2 --> B1

B1 --> B2 --> B3
B3 --> C1 --> C2 --> C3
C3 --> D1 --> D2 --> D3

D3 --> E2
B3 --> E1

E2 --> F1
E1 --> F1

F1 --> F2

%% =========================
%% ESTILO TURQUESA (COMPATÍVEL GITHUB)
%% =========================

classDef default fill:#0d1117,stroke:#00d1c1,stroke-width:1px,color:#ffffff;
classDef grupo fill:#0d1117,stroke:#00d1c1,stroke-width:2px,color:#ffffff;

class FONTES_DE_DADOS,CAMADA_DE_DADOS,ENGENHARIA_DE_FEATURES,PIPELINE_DE_ML,ARMAZENAMENTO,APLICACAO grupo;
```













































<br><br>
<br><br>
<br><br>
<br><br>
<br><br>
<br><br>



<!-- ======================================= Start DEFAULT Footer ===========================================  -->
<br><br>


## 💌 [Let the data flow... Ping Me !](mailto:fabicampanari@proton.me)

<br>


#### <p align="center">  🛸๋ My Contacts [Hub](https://linktr.ee/fabianacampanari)


<br>

### <p align="center"> <img src="https://github.com/user-attachments/assets/517fc573-7607-4c5d-82a7-38383cc0537d" />


<br><br>

<p align="center">  ────────────── ⊹🔭๋ ──────────────

<!--
<p align="center">  ────────────── 🛸๋*ੈ✩* 🔭*ੈ₊ ──────────────
-->

<br>

<p align="center"> ➣➢➤ <a href="#top">Back to Top </a>
  

  
#
 
##### <p align="center"> Copyright 2026 Quantum Software Development. Code released under the  [MIT license.](https://github.com/Mindful-AI-Assistants/CDIA-Entrepreneurship-Soft-Skills-PUC-SP/blob/21961c2693169d461c6e05900e3d25e28a292297/LICENSE)


