
# 🚀 API - Análise de Incidentes de IA em Serviços Financeiros

API RESTful para análise e predição de incidentes de sistemas de IA no setor financeiro.

## 📋 Sobre

Esta API foi desenvolvida como parte do Projeto Integrador utilizando a metodologia CRISP-DM.
Oferece endpoints para:
- Consultar incidentes históricos
- Obter estatísticas agregadas
- Fazer predições com ML sobre severidade e investigações regulatórias

## 🛠️ Tecnologias

- **Flask**: Framework web Python
- **SQLite**: Banco de dados relacional
- **XGBoost/Scikit-learn**: Modelos de Machine Learning
- **Pandas**: Manipulação de dados

## 📦 Instalação

```bash
# Clonar repositório
git clone <repo-url>
cd ai-finance-incidents-api

# Instalar dependências
pip install -r requirements.txt

# Executar API
python app.py
```

## 🔗 Endpoints

### Consulta de Dados

#### `GET /api/incidents`
Lista incidentes com filtros opcionais.

**Query Parameters**:
- `application_type` (opcional): Filtrar por tipo de aplicação
- `severity_level` (opcional): Filtrar por severidade
- `year` (opcional): Filtrar por ano
- `limit` (opcional): Número máximo de resultados (default: 50)

**Exemplo**:
```bash
curl http://localhost:5000/api/incidents?application_type=credit_scoring&limit=10
```

#### `GET /api/incidents/{id}`
Retorna detalhes completos de um incidente.

**Exemplo**:
```bash
curl http://localhost:5000/api/incidents/10
```

### Estatísticas

#### `GET /api/stats/by-application`
Estatísticas agregadas por tipo de aplicação de IA.

#### `GET /api/stats/by-segment`
Estatísticas por segmento de cliente.

#### `GET /api/stats/temporal`
Tendência temporal de incidentes.

#### `GET /api/stats/governance`
Estatísticas sobre respostas de governança.

### Predições ML

#### `POST /api/predict/severity`
Prediz a severidade de um novo incidente.

**Request Body**:
```json
{
    "application_type": "credit_scoring",
    "incident_type": "algorithmic_bias",
    "customer_segment": "retail",
    "year": 2024,
    "regulatory_investigation": 0,
    "fine_imposed": 0,
    "policy_change": 0,
    "third_party_audit": 0
}
```

**Response**:
```json
{
    "prediction": "high",
    "probability": 0.78,
    "confidence": "high",
    "interpretation": "Severidade predita: HIGH com high confiança"
}
```

#### `POST /api/predict/investigation`
Prediz probabilidade de investigação regulatória.

## 🧪 Testes

```bash
# Testar endpoint básico
curl http://localhost:5000/

# Testar listagem
curl http://localhost:5000/api/incidents?limit=5

# Testar predição
curl -X POST http://localhost:5000/api/predict/severity   -H "Content-Type: application/json"   -d '{"application_type":"credit_scoring","incident_type":"algorithmic_bias","customer_segment":"retail","year":2024,"regulatory_investigation":0,"fine_imposed":0,"policy_change":0,"third_party_audit":0}'
```

## 📊 Casos de Uso

### Para Gestores de Risco
- Monitorar incidentes históricos
- Identificar padrões de risco
- Priorizar resposta a novos incidentes

### Para Reguladores
- Análise de tendências do setor
- Avaliar eficácia de marcos regulatórios
- Identificar instituições com alto risco

### Para Desenvolvedores
- Integrar com dashboards de BI
- Criar sistemas de alerta
- Alimentar ferramentas de compliance

## 📝 Licença

Projeto acadêmico - PUC-SP

## 👥 Autores

[Seus nomes aqui]
