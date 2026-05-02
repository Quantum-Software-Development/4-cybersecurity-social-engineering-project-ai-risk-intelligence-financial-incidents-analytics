# ⚡ Quick Start Guide

## 🚀 How to Get Started in 5 Minutes

### 1. Environment Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or: venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

---

### 2. Prepare the Data

**Option A — Use provided data**:

* Included files: `incidents.csv` and `incidents_finance_filtered.csv`
* Skip to step 3

**Option B — Download updated data**:

```python
import kagglehub
path = kagglehub.dataset_download("konradb/ai-incident-database")
print("Path to dataset files:", path)
```

---

### 3. Run the Notebooks in Order

#### 📓 Notebook 1: Exploration and Preparation

```bash
jupyter notebook notebook_1_exploracao_preparacao.ipynb
```

**What it does**:

* Loads the AIID dataset
* Filters financial sector incidents
* Creates derived variables
* Generates SQLite database

**Outputs**:

* `incidents_finance_filtered.csv`
* `ai_finance_incidents.db`

**Estimated time**: ~5–10 minutes

---

#### 📊 Notebook 2: Statistical Analysis

```bash
jupyter notebook notebook_2_analise_estatistica.ipynb
```

**What it does**:

* Descriptive statistics
* 4 hypothesis tests
* Visualizations

**Prerequisite**: Notebook 1 completed

**Estimated time**: ~3–5 minutes

---

#### 🤖 Notebook 3: ML Modeling

```bash
jupyter notebook notebook_3_modelagem_ml.ipynb
```

**What it does**:

* Trains 2 ML models
* Evaluates performance
* Saves trained models

**Outputs**:

* `models/severity_classifier.pkl`
* `models/investigation_classifier.pkl`

**Prerequisite**: Notebook 1 completed

**Estimated time**: ~10–15 minutes (includes training)

---

#### 🚀 Notebook 4: RESTful API

```bash
jupyter notebook notebook_4_api_restful.ipynb
```

**What it does**:

* Defines 9 endpoints
* Tests API
* Generates documentation

**Prerequisites**: Notebooks 1 and 3 completed

**Estimated time**: ~5 minutes

---

### 4. Run the API

```bash
# Copy API code into a standalone file
# (or use the code from Notebook 4)

python app.py
```

**Test it**:

```bash
# Root endpoint
curl http://localhost:5000/

# List incidents
curl http://localhost:5000/api/incidents?limit=5

# Statistics
curl http://localhost:5000/api/stats/by-application
```

---

# 🎯 Shortcuts for Common Use Cases

### Case 1: “I just want to see the results”

1. Run Notebook 1 (generate data)
2. Run Notebook 2 (analysis and charts)
3. Read `RESUMO_EXECUTIVO.md`

---

### Case 2: “I want to use the ML models”

1. Run Notebook 1 (generate data)
2. Run Notebook 3 (train models)
3. Use saved models in `models/`

```python
import joblib
model = joblib.load('models/severity_classifier.pkl')
# Make predictions...
```

---

### Case 3: “I want the API working”

1. Run Notebooks 1 and 3 (data + models)
2. Run Notebook 4 (API definition)
3. Copy code into `app.py` and run it
4. Access `http://localhost:5000`

---

### Case 4: “I want to customize the analyses”

1. Run Notebook 1 (base data)
2. Create your own notebook
3. Use `incidents_finance_filtered.csv` and `ai_finance_incidents.db`

---

# 🐛 Troubleshooting Common Issues

### Problem: `ModuleNotFoundError`

**Solution**:

```bash
pip install -r requirements.txt
```

---

### Problem: “File not found”

**Solution**:

* Make sure you are in the correct directory
* Run notebooks in the correct order
* Confirm Notebook 1 was fully completed

---

### Problem: ML models do not load

**Solution**:

1. Run Notebook 3 completely
2. Check if the `models/` folder exists
3. Confirm `.pkl` files were created

---

### Problem: API returns error 500

**Solution**:

1. Check if `ai_finance_incidents.db` exists
2. Check if models were saved
3. Review terminal logs for details

---

# 📁 Expected File Structure

After running all notebooks:

```plaintext
project/
├── notebook_1_exploracao_preparacao.ipynb
├── notebook_2_analise_estatistica.ipynb
├── notebook_3_modelagem_ml.ipynb
├── notebook_4_api_restful.ipynb
├── incidents.csv
├── incidents_finance_filtered.csv
├── ai_finance_incidents.db
├── models/
│   ├── severity_classifier.pkl
│   ├── investigation_classifier.pkl
│   ├── features_severity.pkl
│   └── features_investigation.pkl
├── app.py
├── requirements.txt
├── README.md
├── EXECUTIVE_SUMMARY.md
└── README_API.md
```

---

# ⏱️ Estimated Total Time

* **Minimum** (results only): ~15–20 minutes
* **Complete** (including API): ~30–40 minutes

---

# 💡 Pro Tips

1. **Use Google Colab if you do not have a local environment**:

   * Upload notebooks
   * Upload `incidents.csv`
   * Execute cells sequentially

2. **Save work incrementally**:

   * Each notebook generates intermediate files
   * No need to redo everything if something fails

3. **Customize for your use case**:

   * All notebooks are modularized
   * Easy to adapt filters, features, and models

4. **Performance**:

   * Notebooks 1–2: Fast
   * Notebook 3: Slower (ML training)
   * Notebook 4: Fast (API setup only)

---

# 📞 Need Help?

* Check `README.md` for complete documentation
* Check `RESUMO_EXECUTIVO.md` to understand results
* Check `README_API.md` for API documentation
* Review notebook text cells for explanations

---

# ✅ Validation Checklist

After execution, confirm:

* [ ] `incidents_finance_filtered.csv` was created
* [ ] `ai_finance_incidents.db` exists and has 3 tables
* [ ] `models/` folder contains 4 `.pkl` files
* [ ] Notebook 2 displayed 4 hypothesis tests
* [ ] Notebook 3 displayed model metrics (F1-Score, etc.)
* [ ] API responds at `http://localhost:5000`

If all are ✅, congratulations! Your project is complete and fully functional! 🎉

---

**Version**: 1.0
**Last Updated**: April 2026 🚀
