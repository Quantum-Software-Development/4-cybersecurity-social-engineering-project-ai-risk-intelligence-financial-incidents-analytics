```mermaid
Diagrama MER - AI Finance Incidents

***
config:
  theme: base
  themeVariables:
    primaryColor: "#006d77"
    primaryTextColor: "#ffffff"
    primaryBorderColor: "#00b4d8"
    lineColor: "#ffffff"
    secondaryColor: "#004b5a"
    tertiaryColor: "#00323d"
    fontFamily: "Inter, Arial, sans-serif"
***

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

    INCIDENTE ||--o{ CLASSIFICACAO : "possui"
    ORGANIZACAO ||--o{ INCIDENTE : "sofre"
```
