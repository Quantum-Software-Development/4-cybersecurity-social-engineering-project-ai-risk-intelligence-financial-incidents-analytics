
# API – AI Incident Analysis in Financial Services

A RESTful API for analyzing and predicting AI system incidents in the financial sector.

---

## 📋 About

This API was developed as part of an Integrated Project using the **CRISP-DM methodology**.

It provides endpoints to:

* Query historical incidents
* Retrieve aggregated statistics
* Perform ML-based predictions on severity and regulatory investigations

---

## 🛠️ Technologies

* **Flask**: Python web framework
* **SQLite**: Relational database
* **XGBoost / Random Forest / Logistic Regression / Scikit-learn**: Machine Learning models
* **Pandas**: Data manipulation

---

##  Installation

```bash
# Clone repository
git clone <repo-url>
cd ai-finance-incidents-api

# Install dependencies
pip install -r requirements.txt

# Run API
python app.py
```

---

## 🔗 Endpoints

---

### Data Query

#### `GET /api/incidents`

Lists incidents with optional filters.

**Query Parameters**:

* `application_type` (optional): Filter by application type
* `severity_level` (optional): Filter by severity
* `year` (optional): Filter by year
* `limit` (optional): Maximum number of results (default: 50)

**Example**:

```bash
curl http://localhost:5000/api/incidents?application_type=credit_scoring&limit=10
```

---

#### `GET /api/incidents/{id}`

Returns full details of a specific incident.

**Example**:

```bash
curl http://localhost:5000/api/incidents/10
```

---

### Statistics

#### `GET /api/stats/by-application`

Aggregated statistics by AI application type.

---

#### `GET /api/stats/by-segment`

Statistics by customer segment.

---

#### `GET /api/stats/temporal`

Temporal trends of incidents.

---

#### `GET /api/stats/governance`

Statistics on governance responses.

---

## 🤖 ML Predictions

---

#### `POST /api/predict/severity`

Predicts the severity of a new incident.

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

---

**Response**:

```json
{
    "prediction": "high",
    "probability": 0.78,
    "confidence": "high",
    "interpretation": "Predicted severity: HIGH with high confidence"
}
```

---

#### `POST /api/predict/investigation`

Predicts the probability of a regulatory investigation.

---

## 🧪 Testing

```bash
# Test root endpoint
curl http://localhost:5000/

# Test listing
curl http://localhost:5000/api/incidents?limit=5

# Test prediction
curl -X POST http://localhost:5000/api/predict/severity \
  -H "Content-Type: application/json" \
  -d '{"application_type":"credit_scoring","incident_type":"algorithmic_bias","customer_segment":"retail","year":2024,"regulatory_investigation":0,"fine_imposed":0,"policy_change":0,"third_party_audit":0}'
```

---

## 📊 Use Cases

---

### For Risk Managers

* Monitor historical incidents
* Identify risk patterns
* Prioritize responses to new incidents

---

### For Regulators

* Analyze sector trends
* Evaluate effectiveness of regulatory frameworks
* Identify institutions with elevated risk

---

### For Developers

* Integrate with BI dashboards
* Build alert systems
* Power compliance tools

---

## 📄 Suggested `.md` File Name

**README_API.md** 🚀
