<!-- ======================================= ⚡️ Start DEFAULT HEADER ===========================================  -->


<!-- ========= START LANGUAGE BUTTON ========= -->
<br>

**\[[🇧🇷 Português](README.pt_BR.md)\] \[**[🇬🇧 English](README.md)**\]**

<br><br>
<!-- ========= END LANGUAGE BUTTON ========= -->



<!-- ========= START REPO TITLE ========= -->
# <p align="center"> 🔐 [Cybersecurity, Social Engineering and AI Security]()  / [Project 4 – AAI Incidents in Financial Services ]() 
### <p align="center"> Analysis of Algorithmic Bias • Operational Risk • AI Governance Responses in Financial Services 



<br><br>
<!-- ========= END REPO TITLE ========= -->


<!-- ========= START Institucional INFO ========= -->
## [Cybersecurity and Social Engineering Integrated Project - PUC-SP 5th Semester (2026)]()


<br>

[**Institution:**]() Pontifical Catholic University of São Paulo (PUC‑SP – Humanistic AI & Data Science • 5º Semester • 2026)  <br>
[**School:**]() FACEI – Faculty of Interdisciplinary Studies  <br>
[**Course Repo:**]() INTEGRATED PROJECT: Cybersecurity and Social Engineering – 108 Hours  <br>
**Professor:** [✨ Eduardo Savino Gomes]()  <br>
[**Extensionist Activities:**]() Extension projects and workshops using open‑source software and data‑driven consulting to support the community, aligned with the 20 official extension hours of the course.

<br><br>

#

<br><br>
<!-- ========= END Institucional INFO ========= -->

<!-- ========= START BADGES ========= -->

<p align="center"> 
  <img src="https://img.shields.io/badge/Python-Data%20Science-007ACC?logo=python&logoColor=ffffff" /> 
  <img src="https://img.shields.io/badge/API-REST-00A676" /> 
  <img src="https://img.shields.io/badge/Security-Zero%20Trust-008B8B" /> 
  <img src="https://img.shields.io/badge/Machine%20Learning-AI-20B2AA" /> 
  <img src="https://img.shields.io/badge/SQL-Light-40E0D0?logo=postgresql&logoColor=ffffff" />
</p>

<br><br>

#

<br><br>
<!-- ========= END START BADGES ========= -->




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

1. [Project Overview](#project-overview)  
   1.1 [Business Context](#business-context)  
   1.2 [General Objective](#general-objective)  
   1.3 [Specific Objectives](#specific-objectives)  
   1.4 [Research Questions](#research-questions)  

2. [Data and Problem Definition](#data-and-problem-definition)  
   2.1 [Data Source: AI Incident Database (AIID)](#data-source-ai-incident-database-aiid)  
   2.2 [Scope: Financial Services Focus](#scope-financial-services-focus)  
   2.3 [Key Raw Variables](#key-raw-variables)  
   2.4 [Core Analytical Concepts](#core-analytical-concepts)  

3. [Derived Variables and Data Model](#derived-variables-and-data-model)  
   3.1 [Financial Application Type (application_type)](#financial-application-type-application_type)  
   3.2 [Incident Type (incident_type)](#incident-type-incident_type)  
   3.3 [Customer Segment (customer_segment)](#customer-segment-customer_segment)  
   3.4 [Severity Level (severity_level)](#severity-level-severity_level)  
   3.5 [Additional Attributes](#additional-attributes)  

4. [Project Structure and Notebooks](#project-structure-and-notebooks)  
   4.1 [Notebook 1 – Data Preparation](#notebook-1--data-preparation)  
   4.2 [Notebook 2 – Exploratory Analysis](#notebook-2--exploratory-analysis)  
   4.3 [Notebook 3 – Feature Engineering and Analytical Base](#notebook-3--feature-engineering-and-analytical-base)  
   4.4 [Notebook 4 – Consolidation and Reporting](#notebook-4--consolidation-and-reporting)  

5. [CRISP-DM Alignment](#crisp-dm-alignment)  

6. [How to Run](#how-to-run)  

7. [Notebook Code (with Graph References)](#notebook-code-with-graph-references)  
   7.1 [Notebook 1 – Data Preparation](#notebook-1--data-preparation-1)  
   7.2 [Notebook 2 – Exploratory Analysis](#notebook-2--exploratory-analysis-1)  
   7.3 [Notebook 3 – Feature Engineering](#notebook-3--feature-engineering-1)  
   7.4 [Notebook 4 – Consolidation and Reporting](#notebook-4--consolidation-and-reporting-1)  

8. [Next Steps and Possible Extensions](#next-steps-and-possible-extensions)  

9. [Author and Context](#author-and-context)  

10. [Topics (Tags)](#topics-tags)


<br><br>

## 1. Visão Geral do Projeto

### 1.1 Contexto de Negócio

Desenvolvemos este projeto sob a perspectiva de uma boutique de consultoria especializada em risco de IA aplicada ao setor financeiro. Nossa proposta é apoiar bancos, fintechs e demais organizações na identificação de padrões de incidente, no mapeamento de vulnerabilidades sistêmicas e na transformação de eventos históricos em inteligência acionável para governança, compliance e mitigação de risco.

O projeto utiliza dados do Artificial Intelligence Incident Database (AIID) para construir uma base analítica focada em serviços financeiros, com ênfase em aplicações como concessão de crédito, detecção de fraude, avaliação de risco, automação bancária, pagamentos, seguros e contextos correlatos. A partir dessa base, estruturamos variáveis analíticas, realizamos exploração descritiva inicial e preparamos o pipeline para análises estatísticas, modelagem preditiva e exposição dos resultados via API ou serviços de dados.

Do ponto de vista de negócio, o problema que endereçamos é a ausência de visibilidade estruturada sobre riscos reais de IA em operações financeiras. Muitas instituições já utilizam modelos algorítmicos em decisões sensíveis, mas ainda carecem de mecanismos robustos para entender onde estão seus maiores riscos, quais aplicações demandam supervisão reforçada, quais grupos podem estar mais expostos a viés e como priorizar controles preventivos com base em evidências.

Nesta fase exploratória, o foco está em organizar a base, criar variáveis derivadas, compreender padrões iniciais e consolidar um pipeline claro, pronto para ser expandido em direção a modelos preditivos, dashboards e APIs.

<br>


















































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


