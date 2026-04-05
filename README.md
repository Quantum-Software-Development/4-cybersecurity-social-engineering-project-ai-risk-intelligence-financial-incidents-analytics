<!-- ======================================= ⚡️ Start DEFAULT HEADER ===========================================  -->


<!-- ========= START LANGUAGE BUTTON ========= -->
<br>

**\[[🇧🇷 Português](README.pt_BR.md)\] \[**[🇬🇧 English](README.md)**\]**

<br><br>
<!-- ========= END LANGUAGE BUTTON ========= -->




<!-- ========= START REPO TITLE ========= -->
# <p align="center"> 🔐 [Cybersecurity, Social Engineering and AI Security]()  / [Project 4 – AI Finance Incident Risk & Governance Analysis ]() 
### <p align="center"> Analysis of Algorithmic Bias • Operational Risk • AI Governance Responses in Financial Services 



<br><br>
<!-- ========= START REPO TITLE ========= -->


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



## Table of Contents

1. [Project Overview](#project-overview)  
   1.1 [Business Context](#business-context)  
   1.2 [General Objective](#general-objective)  
   1.3 [Specific Objectives](#specific-objectives)  
   1.4 [Research Questions](#research-questions)


2. [Data and Problem Definition](#data-and-problem-definition)  
   2.1 [Source Data: AI Incident Database (AIID)](#source-data-ai-incident-database-aiid)  
   2.2 [Scope: Financial Services Subset](#scope-financial-services-subset)  
   2.3 [Key Raw Variables](#key-raw-variables)  
   2.4 [Core Analytical Concepts and Definitions](#core-analytical-concepts-and-definitions)


3. [Derived Variables and Data Model](#derived-variables-and-data-model)  
   3.1 [Financial Application Type](#financial-application-type)  
   3.2 [Customer Segment](#customer-segment)  
   3.3 [Incident Type](#incident-type)  
   3.4 [Severity and Financial Loss](#severity-and-financial-loss)  
   3.5 [Governance and Regulatory Response](#governance-and-regulatory-response)  
   3.6 [Temporal and Geographic Dimensions](#temporal-and-geographic-dimensions)  
   3.7 [Relational Data Model (SQLite)](#relational-data-model-sqlite)


4. [Exploratory Analysis and Statistical Hypotheses](#exploratory-analysis-and-statistical-hypotheses)  
   4.1 [Descriptive Questions](#descriptive-questions)  
   4.2 [Hypothesis 1 – Concentration by Application Type](#hypothesis-1--concentration-by-application-type)  
   4.3 [Hypothesis 2 – Bias by Customer Segment](#hypothesis-2--bias-by-customer-segment)  
   4.4 [Hypothesis 3 – Severity and Regulatory Response](#hypothesis-3--severity-and-regulatory-response)  
   4.5 [Hypothesis 4 – Temporal Trends and Regulation](#hypothesis-4--temporal-trends-and-regulation)


5. [Machine Learning and Statistical Techniques](#machine-learning-and-statistical-techniques)  
   5.1 [Predictive Models](#predictive-models)  
   5.2 [Text Mining and NLP](#text-mining-and-nlp)  
   5.3 [Statistical Methods](#statistical-methods)  
   5.4 [Visual Analytics](#visual-analytics)


6. [Project Structure and Notebooks](#project-structure-and-notebooks)  
   6.1 [Phase 1 – Exploratory & Data Preparation](#phase-1--exploratory--data-preparation)  
   6.2 [Phase 2 – Statistical Analysis & Hypothesis Testing](#phase-2--statistical-analysis--hypothesis-testing)  
   6.3 [Phase 3 – Predictive Modeling & REST API](#phase-3--predictive-modeling--rest-api)  
   6.4 [Final Consolidated Pipeline Notebook](#final-consolidated-pipeline-notebook)


7. [CRISP‑DM Methodology Alignment](#crisp-dm-methodology-alignment) <br>
   7.0 [CRISP‑DM Methodology Diagram](#crisp‑dm-methodology-diagram) <br>
   7.1 [Business Understanding](#business-understanding)  
   7.2 [Data Understanding](#data-understanding)  
   7.3 [Data Preparation](#data-preparation)  
   7.4 [Modeling](#modeling)  
   7.5 [Evaluation](#evaluation)  
   7.6 [Deployment](#deployment)


9. [How to Run](#how-to-run)  
   8.1 [Repository and Environment](#repository-and-environment)  
   8.2 [Notebook Execution Order](#notebook-execution-order)  
   8.3 [Starting the API](#starting-the-api)


10. [Dataset Access](#dataset-access)  


11. [Author](#author)  


12. [Topics](#topics)  


13. [Final Note](#final-note)



<br><br>


## 1. [Project Overview]()


### [1.1]()- ***Business Context***



The financial sector has rapidly adopted AI systems across areas such as credit scoring, fraud detection, algorithmic trading, customer service, and process automation. While these technologies create significant value, they also introduce new forms of operational risk, algorithmic bias, and regulatory exposure, including fines, investigations, and reputational damage.

This project analyzes documented incidents involving Artificial Intelligence (AI) in financial services, with a focus on algorithmic bias, operational risk, and governance responses in banks and fintechs. The analysis is based on data from the AI Incident Database (AIID), accessed via [Kaggle](https://www.kaggle.com/datasets/konradb/ai-incident-database) or the [Official Platform](https://incidentdatabase.ai). Following the CRISP-DM methodology, the project combines structured data analysis, statistical techniques, and simple predictive models to generate insights that support risk management and AI governance in the financial sector.

In this context, the project adopts the perspective of a specialized AI risk and incident analytics consultancy working with banks and fintechs. The objective is to help organizations identify patterns of AI-related incidents, map systemic vulnerabilities, and prevent future occurrences, with a strong emphasis on protecting customers from algorithmic bias, operational failures, and financially harmful AI-driven decisions.

By transforming historical incident data into a structured and analysis-ready dataset, and applying both statistical methods and machine learning techniques, the project aims to deliver decision-ready insights for risk management, compliance, and AI governance teams. Ultimately, it supports more informed decisions on where to invest in controls, how to prioritize remediation efforts, and which AI use cases in financial services require stricter oversight.



<br><br>


