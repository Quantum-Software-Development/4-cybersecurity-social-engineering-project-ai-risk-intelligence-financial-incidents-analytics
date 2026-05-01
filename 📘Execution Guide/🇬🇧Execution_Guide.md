# 🚀 Complete Execution Guide
## AI Incidents in Financial Services · From Zero to Dashboard

**For beginners · VS Code · macOS/Linux/Windows**

---

## Overview

This guide teaches how to run the complete project from scratch: from installing Python to having the dashboard running with the working Groq chatbot.

```
Estimated time for complete execution: 30–45 minutes
Level: Beginner with basic terminal knowledge
```

### What you will have at the end

| Component | URL | Description |
|---|---|---|
| **Flask API** | http://localhost:5000 | Backend with 9 endpoints |
| **Dashboard** | http://localhost:8501 | Interactive visual interface |
| **Groq Chatbot** | (inside the dashboard) | AI for questions about the data |

---

## ✅ Prerequisites

Before starting, confirm that you have:

```
[ ] Python 3.10 or higher
[ ] VS Code installed
[ ] Git installed (optional, but recommended)
[ ] Groq account created (free) — see Section 4
[ ] Kaggle account (to download the dataset) — optional
```

### Check Python version

```bash
python3 --version
# Should show: Python 3.10.x or higher
```

If you don't have Python, download it at: https://python.org/downloads

---

## 📥 1. Get the Project

### Option A — With Git

```bash
git clone https://github.com/your-username/ai-finance-incidents.git
cd ai-finance-incidents
```

### Option B — Manual download

1. Download the repository `.zip`
2. Unzip into a folder of your choice
3. Open the terminal in that folder

### Open in VS Code

```bash
code .
```

Or: `File → Open Folder → select the project folder`

---

## 🔧 2. Environment Setup

### 2.1 Create virtual environment

> **Why?** The virtual environment isolates project dependencies, preventing conflicts with other Python projects on your computer.

```bash
# Create the virtual environment
python3 -m venv .venv

# Activate — macOS/Linux
source .venv/bin/activate

# Activate — Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Activate — Windows (Command Prompt)
.venv\Scripts\activate.bat
```

**How to know it worked?** The terminal will show `(.venv)` before the path:
```
(.venv) user@machine:~/ai-finance-incidents$
```

### 2.2 Install dependencies

```bash
pip install -r requirements.txt
```

> ⏱ This takes 3–8 minutes the first time. It is normal.

### 2.3 Register kernel in Jupyter

> This step is needed only once so that the notebooks recognize the virtual environment.

```bash
python -m ipykernel install --user \
  --name=.venv \
  --display-name "Python (ai-finance)"
```

### 2.4 Verify installation

```bash
python -c "import pandas, streamlit, flask, xgboost; print('✅ All installed!')"
```

---

## 📊 3. Get the Dataset

The project needs the `incidents.csv` file from the AI Incident Database.

### Option A — Kaggle CLI (recommended)

```bash
pip install kaggle

# Configure your credentials (first time only):
# 1. Go to https://kaggle.com/your-account
# 2. Click on "Create New API Token"
# 3. Move the kaggle.json file to ~/.kaggle/

kaggle datasets download konradb/ai-incident-database
unzip ai-incident-database.zip -d data/raw/
```

### Option B — Manual download

1. Go to: https://www.kaggle.com/datasets/konradb/ai-incident-database
2. Click "Download"
3. Extract and place the CSV in `data/raw/incidents.csv`

### Option C — Without dataset (demo data)

If you don't have access, the project works with automatically generated demo data. Just skip to the next step.

---

## 🔑 4. Groq API Configuration

### 4.1 Create account and get key (free, 2 minutes)

1. Go to **https://console.groq.com**
2. Click "Sign Up" and create a free account
3. In the dashboard, go to **"API Keys"**
4. Click **"Create API Key"**
5. Name it `ai-finance-project`
6. **Copy the key** (starts with `gsk_...`) — it only appears once!

### 4.2 Create `.env` file (local execution)

At the root of the project, create a file named `.env`:

```bash
# macOS/Linux — create via terminal
cat > .env << 'EOF'
GROQ_API_KEY=gsk_your_key_here
API_BASE_URL=http://localhost:5000
EOF
```

**Windows** — create the file manually with Notepad:
```
GROQ_API_KEY=gsk_your_key_here
API_BASE_URL=http://localhost:5000
```
Save as `.env` (without `.txt` extension) at the root of the project.

### 4.3 Verify the file

```bash
cat .env
# Should show:
# GROQ_API_KEY=gsk_...
# API_BASE_URL=http://localhost:5000
```

> ⚠️ **Never commit the `.env` file to Git!** It is already in `.gitignore`.

---

## 📓 5. Run the Notebooks

> **Important rule**: always run in the order NB1 → NB2 → NB3 → NB4. Each notebook generates files that the next one needs.

### 5.1 Start Jupyter

```bash
jupyter notebook notebooks/
```

The browser will open automatically at `http://localhost:8888`.

### 5.2 Select the correct kernel

When opening any notebook:
1. Click on "Kernel" → "Change Kernel"
2. Select **"Python (ai-finance)"**
3. Confirm

### 5.3 Notebook 1 — Exploration and Preparation

**File**: `NB1_Exploracao_Preparacao.ipynb`

```
Click on: Kernel → Restart & Run All
Wait: ~2–5 minutes
```

**What happens**:
- Tries to connect to the AIID GraphQL API
- If offline → uses cache or `incidents.csv`
- Filters financial incidents by keywords
- Creates 8 derived variables (application_type, severity_level, etc.)
- Saves the processed CSV and the SQLite database

**Generated files**:
```
✅ data/incidents_finance_filtered.csv
✅ ai_finance_incidents.db
✅ assets/distribuicao_variaveis.png
```

### 5.4 Notebook 2 — Statistical Analysis

**File**: `NB2_Analise_Estatistica.ipynb`

```
Click on: Kernel → Restart & Run All
Wait: ~1–2 minutes
```

**What happens**:
- Complete descriptive statistics
- H1–H4 tests (chi-square, Spearman, logistic regression)
- Interactive Plotly charts

### 5.5 Notebook 3 — ML Modeling

**File**: `NB3_Modelagem_ML.ipynb`

```
Click on: Kernel → Restart & Run All
Wait: ~3–5 minutes (model training)
```

**Generated files**:
```
✅ models/severity_classifier.pkl
✅ models/investigation_classifier.pkl
✅ models/features_severity.pkl
✅ models/features_investigation.pkl
```

> ℹ️ The models might show F1-Score close to 0. This is expected — the dataset has only ~31 incidents with strong class imbalance. The pipeline is correct; more data is needed for real performance.

### 5.6 Notebook 4 — RESTful API

**File**: `NB4_API_RESTful.ipynb`

```
Click on: Kernel → Restart & Run All
Wait: ~1–2 minutes
```

**Generated file**:
```
✅ api/app_api.py
```

> ⚠️ **Do not run the final cell** that calls `app.run()` inside the notebook — this would freeze the kernel. The API must be started from the terminal (next step).

---

## 🚀 6. Run the Flask API

Open a **new terminal** in VS Code (`Ctrl + Shift + `` ` ``):

```bash
# Activate the virtual environment (if not active)
source .venv/bin/activate

# Start the API
python api/app_api.py
```

**Expected output**:
```
✅ ML Models loaded successfully.
🚀 AI Finance Incidents API — Starting
📡 API available at: http://localhost:5000
 * Running on http://0.0.0.0:5000
```

### Test the API

In another terminal or in the browser:

```bash
# Check status
curl http://localhost:5000/

# List incidents
curl "http://localhost:5000/api/incidents?limit=5"

# Statistics by application
curl http://localhost:5000/api/stats/by-application

# Severity prediction
curl -X POST http://localhost:5000/api/predict/severity \
  -H "Content-Type: application/json" \
  -d '{"application_type":"credit_scoring","incident_type":"algorithmic_bias",
       "customer_segment":"retail","year":2024,"fine_imposed":0,
       "policy_change":0,"third_party_audit":0}'
```

> ✅ If you receive a JSON response, the API is working correctly.

> **Keep this terminal open while using the dashboard.**

---

## 🖥️ 7. Run the Streamlit Dashboard

Open **another terminal** (keeping the API one open):

```bash
# Activate the virtual environment
source .venv/bin/activate

# Start the dashboard
streamlit run dashboard/app.py
```

**Expected output**:
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

The browser will open automatically. If it doesn't, go to: **http://localhost:8501**

---

## 💬 8. Test the Chatbot

### 8.1 Access the chatbot page

In the dashboard, click on **"💬 AI Assistant"** in the left sidebar.

### 8.2 Verify key configuration

The dashboard reads the Groq key automatically from the `.env` file. You will see:

```
✅ Groq configured via environment variable · model: llama-3.1-8b-instant
```

If it doesn't appear, configure manually:
1. Expand the panel **"⚙️ Configure Groq API (free)"**
2. Paste your key `gsk_...`
3. Click outside the field

### 8.3 Questions to test

Click on the suggestions or type:
- *"Which application has the most incidents?"*
- *"Explain hypothesis tests H1 to H4"*
- *"How was XGBoost used in the project?"*
- *"Which segments are most affected by bias?"*

### 8.4 Offline mode (without key)

Without a configured Groq key, the chatbot responds based on local keywords — it works for the main questions about the project.

---

## ⚠️ 9. Common Errors and Solutions

| Error | Probable cause | Solution |
|---|---|---|
| `ModuleNotFoundError: No module named 'X'` | Dependency not installed | `pip install -r requirements.txt` |
| `(.venv)` does not appear in terminal | Environment not activated | Run the command `source .venv/bin/activate` again |
| `FileNotFoundError: incidents.csv` | Dataset not downloaded | Follow Section 3 |
| `FileNotFoundError: ai_finance_incidents.db` | NB1 was not run | Run Notebook 1 first |
| `FileNotFoundError: models/severity_classifier.pkl` | NB3 was not run | Run Notebook 3 first |
| API offline in the dashboard | Terminal with API was closed | Open new terminal and run `python api/app_api.py` |
| `Address already in use (port 5000)` | Another instance of the API running | Run: `lsof -ti:5000 \| xargs kill` (macOS/Linux) |
| `Address already in use (port 8501)` | Another dashboard running | `streamlit run dashboard/app.py --server.port 8502` |
| Kernel not found in Jupyter | `.venv` not registered | `python -m ipykernel install --user --name=.venv` |
| Chatbot does not respond (Groq) | Invalid key or no internet | Check the key at console.groq.com |
| Dashboard opens but no data | CSV not found | Check if NB1 generated `incidents_finance_filtered.csv` |

---

## ✅ 10. Final Checklist

Run this checklist to confirm that everything is working:

### Environment
```
[ ] Python 3.10+ installed
[ ] Virtual environment (.venv) created and activated
[ ] requirements.txt installed without errors
[ ] Jupyter kernel registered
```

### Data and models
```
[ ] data/incidents_finance_filtered.csv exists
[ ] ai_finance_incidents.db exists
[ ] models/severity_classifier.pkl exists
[ ] models/investigation_classifier.pkl exists
[ ] models/features_severity.pkl exists
[ ] models/features_investigation.pkl exists
```

### API
```
[ ] Terminal 1: python api/app_api.py is running
[ ] curl http://localhost:5000/ returns JSON
[ ] Prediction endpoint responds without error
```

### Dashboard
```
[ ] Terminal 2: streamlit run dashboard/app.py is running
[ ] http://localhost:8501 opens in browser
[ ] Sidebar shows "🟢 API online"
[ ] Overview page shows KPIs
[ ] API Explorer page shows API status
[ ] Chatbot responds (Groq or offline mode)
```

### Groq
```
[ ] .env file created with GROQ_API_KEY
[ ] Dashboard shows "✅ Groq configured via environment variable"
[ ] Chatbot answers questions about the data
```

---

## 📌 Quick Summary (for those who already know the project)

```bash
# 1. Environment
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 2. Dataset
# Place incidents.csv in data/raw/

# 3. Notebooks (Jupyter or VS Code)
# Run: NB1 → NB2 → NB3 → NB4

# 4. API (Terminal 1)
python api/app_api.py

# 5. Dashboard (Terminal 2)
streamlit run dashboard/app.py

# 6. Configure Groq
echo "GROQ_API_KEY=gsk_..." >> .env
```

---

*PUC-SP · Integrative Project · 5th Semester · 2026*
