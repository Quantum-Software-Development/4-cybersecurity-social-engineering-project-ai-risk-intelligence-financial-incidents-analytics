
# [🇧🇷 PORT]

## 🧠 Diagrama DER — AI Finance Incidents

Este diagrama representa a modelagem de dados para o registro e análise de incidentes relacionados ao uso de Inteligência Artificial no setor financeiro.

<br><br>

## 📌 Entidades

- **INCIDENTE**: representa um evento relacionado a falhas, riscos ou problemas envolvendo sistemas de IA.
- **ORGANIZACAO**: entidade que sofreu ou foi impactada por um incidente.
- **CLASSIFICACAO**: detalha a categorização técnica do incidente (tipo de falha, domínio de IA, origem dos dados).

<br><br>

## 🔗 Relacionamentos

- **ORGANIZACAO → INCIDENTE (1:N)**  
  Uma organização pode sofrer vários incidentes, mas cada incidente está associado a uma única organização.

- **INCIDENTE → CLASSIFICACAO (1:N)**  
  Um incidente pode possuir múltiplas classificações, permitindo análise mais granular.


<br><br>


## 💡 Objetivo

Esse modelo facilita:
- Análise de riscos em sistemas de IA
- Auditoria e rastreabilidade de incidentes
- Classificação estruturada para estudos e relatórios


<br><br>

## Importante

Por que CLASSIFICACAO não tem org_id?”

Resposta:
Porque ela depende de INCIDENTE, e não diretamente da organização

<br><br>

## Relembrando 

Entidade → Tabela
Atributo → Coluna
PK → Primary Key
Relacionamento 1:N → Foreign Key
DER → vira SQL


<br><br>

```mermaid
%%{init: {
  "theme": "base",
  "themeVariables": {
    "primaryColor": "#0d1117",
    "primaryTextColor": "#ffffff",
    "primaryBorderColor": "#00b4d8",
    "lineColor": "#00b4d8",
    "background": "#0d1117"
  },
  "themeCSS": "
    .er.relationshipLine path { stroke: #00b4d8 !important; }
    .er.entityBox { stroke: #00b4d8 !important; fill: #0d1117 !important; }
    .er.attributeBoxOdd { fill: #0d1117 !important; }
    .er.attributeBoxEven { fill: #0d1117 !important; }
    .er.entityLabel { fill: #ffffff !important; }
  "
}}%%

erDiagram
    INCIDENTE {
        int incident_id PK
        date data_incidente
        string titulo
        string descricao
        string tipo_risco
        string severidade
    }

    ORGANIZACAO {
        int org_id PK
        string nome_org
        string pais
        string setor
    }

    CLASSIFICACAO {
        int class_id PK
        int incident_id FK
        string dominio_ai
        string tipo_falha
        string origem_dado
    }

    INCIDENTE ||--o{ CLASSIFICACAO : possui
    ORGANIZACAO ||--o{ INCIDENTE : sofre
```

<br>

#

<br>

# [🇺🇸 ENG]

## 🧠 ERD Diagram — AI Finance Incidents

This diagram represents the data modeling for recording and analyzing incidents related to the use of Artificial Intelligence in the financial sector.

<br><br>


## 📌 Entities

- **INCIDENT**: represents an event related to failures, risks, or issues involving AI systems.  
- **ORGANIZATION**: entity that suffered or was impacted by an incident.  
- **CLASSIFICATION**: details the technical categorization of the incident (failure type, AI domain, data source).

<br><br>

## 🔗 Relationships

- **ORGANIZATION → INCIDENT (1:N)**  
  One organization can suffer multiple incidents, but each incident is associated with a single organization.

- **INCIDENT → CLASSIFICATION (1:N)**  
  One incident can have multiple classifications, allowing more granular analysis.

<br><br>

## 💡 Purpose

This model enables:
- Risk analysis in AI systems  
- Incident auditing and traceability  
- Structured classification for studies and reports  

<br><br>

## Important

Why doesn’t CLASSIFICATION have `org_id`?

**Answer:**  
Because it depends on INCIDENT, not directly on the organization.

<br><br>

## Reminder

Entity → Table  
Attribute → Column  
PK → Primary Key  
1:N Relationship → Foreign Key  
ERD → becomes SQL  

<br><br>

```mermaid
%%{init: {
  "theme": "base",
  "themeVariables": {
    "primaryColor": "#0d1117",
    "primaryTextColor": "#ffffff",
    "primaryBorderColor": "#00b4d8",
    "lineColor": "#00b4d8",
    "background": "#0d1117"
  },
  "themeCSS": "
    .er.relationshipLine path { stroke: #00b4d8 !important; }
    .er.entityBox { stroke: #00b4d8 !important; fill: #0d1117 !important; }
    .er.attributeBoxOdd { fill: #0d1117 !important; }
    .er.attributeBoxEven { fill: #0d1117 !important; }
    .er.entityLabel { fill: #ffffff !important; }
  "
}}%%

erDiagram
    INCIDENT {
        int incident_id PK
        date incident_date
        string title
        string description
        string risk_type
        string severity
    }

    ORGANIZATION {
        int org_id PK
        string organization_name
        string country
        string sector
    }

    CLASSIFICATION {
        int class_id PK
        int incident_id FK
        string ai_domain
        string failure_type
        string data_source
    }

    INCIDENT ||--o{ CLASSIFICATION : has
    ORGANIZATION ||--o{ INCIDENT : suffers
```
