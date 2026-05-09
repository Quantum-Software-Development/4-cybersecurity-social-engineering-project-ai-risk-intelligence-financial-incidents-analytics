# 🚀 Complete Execution and Deployment Guide
## AI Finance Incidents — From Scratch to Live

> **Who this guide is for:**  
> ✅ Beginners — every step explained from scratch  
> ✅ Professionals — quick reference with all commands  

---

## 📋 Table of Contents

1. [Prerequisites](#1-prerequisites)
2. [Clone and configure the project locally](#2-clone-and-configure-the-project-locally)
3. [Configure environment variables](#3-configure-environment-variables)
4. [Prepare data and models](#4-prepare-data-and-models)
5. [Run locally](#5-run-locally)
6. [Test the API locally](#6-test-the-api-locally)
7. [Publish to GitHub](#7-publish-to-github)
8. [Deploy the API on Render](#8-deploy-the-api-on-render)
9. [Deploy the Dashboard on Streamlit Cloud](#9-deploy-the-dashboard-on-streamlit-cloud)
10. [Connect Dashboard to the API in production](#10-connect-dashboard-to-the-api-in-production)
11. [Configure the Groq key](#11-configure-the-groq-key)
12. [Final validation](#12-final-validation)
13. [Common errors and solutions](#13-common-errors-and-solutions)

---

## 1. Prerequisites

### What you need installed

| Tool | How to check | How to install |
|---|---|---|
| Python 3.10+ | `python --version` | https://python.org/downloads |
| Git | `git --version` | https://git-scm.com |
| VS Code (recommended) | — | https://code.visualstudio.com |

### Required accounts (all free)

| Platform | For what | Link |
|---|---|---|
| GitHub | Code repository | https://github.com |
| Render | Host the Flask API | https://render.com |
| Streamlit Cloud | Host the dashboard | https://share.streamlit.io |
| Groq | Chatbot API | https://console.groq.com |

---

## 2. Clone and Configure the Project Locally

### 2.1 Open the terminal

- **Windows:** `Win + R` → type `cmd` → Enter  
- **Mac:** `Cmd + Space` → type `Terminal` → Enter  
- **VS Code:** `Terminal` Menu → `New Terminal`

### 2.2 Navigate to where you want to save the project

```bash
# Example: go to the Documents folder
cd ~/Documents   # Mac/Linux
cd %USERPROFILE%\Documents   # Windows
```

### 2.3 Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/ai-finance-incidents.git
cd ai-finance-incidents
```

> **If you don't have a GitHub repository yet**, create a local folder:
> ```bash
> mkdir ai-finance-incidents
> cd ai-finance-incidents
> ```

### 2.4 Create the Python virtual environment

```bash
# Create
python -m venv .venv

# Activate — Mac/Linux
source .venv/bin/activate

# Activate — Windows PowerShell
.venv\Scripts\Activate.ps1

# Activate — Windows CMD
.venv\Scripts\activate.bat
```

> 💡 **How to know if it worked?** The terminal will show `(.venv)` before the cursor.

### 2.5 Install dependencies

```bash
pip install -r requirements.txt
```

> ⏱ This takes 2–5 minutes the first time. This is normal.

---

## 3. Configure Environment Variables

### 3.1 Create the `.env` file

```bash
# Mac/Linux
cp .env.example .env

# Windows
copy .env.example .env
```

### 3.2 Edit `.env`

Open the `.env` file in VS Code or any text editor and fill it out:

```env
# ─── Flask API ────────────────────────────────────────────
PORT=5000

# ─── Dashboard ────────────────────────────────────────────
# In production: paste the Render URL after deployment
API_BASE_URL=http://localhost:5000

# ─── Groq Chatbot ─────────────────────────────────────────
# Get it at: https://console.groq.com/keys
GROQ_API_KEY=your_groq_api_key_here
```

### 3.3 Get the Groq key (free)

1. Go to https://console.groq.com
2. Create an account (you can use Google or email)
3. Click on **"API Keys"** in the sidebar
4. Click on **"Create API Key"**
5. Give it a name (e.g., `ai-finance-local`)
6. **Copy the key** — it only appears once!
7. Paste it into `.env` replacing `your_groq_api_key_here`

> ⚠️ **NEVER commit the `.env` file to Git.** It is already in `.gitignore`.

---

## 4. Prepare Data and Models

### 4.1 Required folder structure

Create the folders if they don't exist:

```bash
mkdir -p database models
touch database/.gitkeep models/.gitkeep
```

### 4.2 Execute the notebooks to generate data

> Execute in this exact order. Each notebook generates files used by the next.

```bash
# Register the virtual environment kernel in Jupyter
python -m ipykernel install --user --name=.venv --display-name "AI Finance"

# Open Jupyter
jupyter notebook
```

In the browser that opens:

| Order | Notebook | What it generates |
|---|---|---|
| 1st | `NB1_Exploration_Preparation.ipynb` | `incidents_finance_filtered.csv` + SQLite database |
| 2nd | `NB2_Statistical_Analysis.ipynb` | statistical analyses |
| 3rd | `NB3_ML_Modeling.ipynb` | `models/*.pkl` (trained models) |
| 4th | `NB4_RESTful_API.ipynb` | (optional — API documentation) |

> 💡 **Tip:** In VS Code, you can open notebooks directly without needing the browser.

---

## 5. Run Locally

You need **two terminals open at the same time**.

### Terminal 1 — Flask API

```bash
# With (.venv) active
python app_api.py
```

Expected output:
```
============================================================
🚀 API running at http://localhost:5000
============================================================
 * Serving Flask app 'app_api'
 * Running on http://0.0.0.0:5000
```

### Terminal 2 — Streamlit Dashboard

```bash
# With (.venv) active (open a new terminal)
streamlit run app.py
```

Expected output:
```
  You can now view your Streamlit app in your browser.
  Local URL: http://localhost:8501
```

The browser will automatically open to `http://localhost:8501`.

---

## 6. Test the API Locally

### Quick test in the browser

Open: http://localhost:5000

A JSON with the API documentation should appear.

### Tests with curl (terminal)

```bash
# API Status
curl http://localhost:5000/

# List incidents
curl "http://localhost:5000/api/incidents?limit=5"

# Statistics by application
curl http://localhost:5000/api/stats/by-application

# Severity prediction
curl -X POST http://localhost:5000/api/predict/severity \
  -H "Content-Type: application/json" \
  -d '{"application_type":"credit_scoring","incident_type":"algorithmic_bias","customer_segment":"retail","year":2024}'
```

### Test with Python

```python
import requests

# Ping
r = requests.get("http://localhost:5000/")
print(r.json())

# Prediction
payload = {
    "application_type": "credit_scoring",
    "incident_type": "algorithmic_bias",
    "customer_segment": "retail",
    "year": 2024
}
r = requests.post("http://localhost:5000/api/predict/severity", json=payload)
print(r.json())
# Expected: {"prediction": 0 or 1, "probability": 0.xx}
```

---

## 7. Publish to GitHub

### 7.1 Create repository on GitHub

1. Go to https://github.com → click on **"New repository"**
2. Name: `ai-finance-incidents`
3. Leave it **Private** (recommended while in development)
4. **DO NOT** check "Initialize with README" (you already have one)
5. Click on **"Create repository"**

### 7.2 Initialize Git locally

```bash
git init
git add .
git commit -m "feat: initial commit — Secured API + Dashboard"
```

### 7.3 Connect and push to GitHub

```bash
# Replace YOUR-USERNAME with your GitHub username
git remote add origin https://github.com/YOUR-USERNAME/ai-finance-incidents.git
git branch -M main
git push -u origin main
```

### 7.4 Check what was pushed

Go to https://github.com/YOUR-USERNAME/ai-finance-incidents and confirm:

- ✅ `.env` DOES NOT appear (it's in .gitignore)
- ✅ `models/` DOES NOT appear with .pkl files
- ✅ `database/` DOES NOT appear with the .db file
- ✅ `.gitignore` appears
- ✅ `requirements.txt` appears
- ✅ `app.py` and `app_api.py` appear

> ⚠️ If `.env` or `.db` appear on GitHub, **remove them immediately**:
> ```bash
> git rm --cached .env
> git commit -m "fix: remove .env from tracking"
> git push
> ```

---

## 8. Deploy the API on Render

### 8.1 What is Render

Render is a cloud hosting platform with a free plan. The Flask API will be available on a public URL like `https://ai-finance-api.onrender.com`.

### 8.2 Prepare deployment files

Create the `Procfile` at the root of the project:

```bash
echo "web: gunicorn app_api:app --workers 2 --bind 0.0.0.0:\$PORT" > Procfile
```

Create the `render.yaml` file at the root:

```yaml
services:
  - type: web
    name: ai-finance-api
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app_api:app --workers 2 --bind 0.0.0.0:$PORT
    envVars:
      - key: PORT
        value: 5000
      - key: PYTHON_VERSION
        value: 3.11.0
```

Commit these files:

```bash
git add Procfile render.yaml
git commit -m "feat: add Render deploy config"
git push
```

### 8.3 Create the service on Render

1. Go to https://render.com and click **"Sign Up"**
2. Log in with your GitHub account (facilitates integration)
3. In the dashboard, click on **"New +"** → **"Web Service"**
4. Select **"Connect a repository"**
5. Choose the repository `ai-finance-incidents`
6. Configure:

| Field | Value |
|---|---|
| **Name** | `ai-finance-api` |
| **Region** | Oregon (US West) — free |
| **Branch** | `main` |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app_api:app --workers 2 --bind 0.0.0.0:$PORT` |
| **Instance Type** | Free |

### 8.4 Configure environment variables on Render

On the same configuration screen, click on **"Environment Variables"** and add:

| Key | Value |
|---|---|
| `PORT` | `5000` |
| `PYTHON_VERSION` | `3.11.0` |

> ⚠️ **Important note about data:** Render Free does not persist files between deployments. The `.db` database and `.pkl` models must be **included in the repository** or loaded from external storage. For academic purposes, include them in the commit:
> ```bash
> # Remove the database/ and models/ lines from .gitignore
> # Then:
> git add database/ models/
> git commit -m "feat: include database and models for Render deploy"
> git push
> ```

### 8.5 Start the deployment

Click on **"Create Web Service"**. Render will:

1. Clone your repository
2. Run `pip install -r requirements.txt`
3. Start with Gunicorn

Follow the logs in real-time on the **"Logs"** tab.

### 8.6 Verify the deployment

After ~2-3 minutes, the URL will appear at the top of the page. Test it:

```bash
curl https://ai-finance-api.onrender.com/
```

> 💡 **Free plan:** The API "sleeps" after 15 minutes of inactivity. The first request will take ~30 seconds to "wake it up". This is normal on the free plan.

---

## 9. Deploy the Dashboard on Streamlit Cloud

### 9.1 Access Streamlit Community Cloud

1. Go to https://share.streamlit.io
2. Click on **"Sign in with GitHub"**

### 9.2 Create the app

1. Click on **"New app"**
2. Configure:

| Field | Value |
|---|---|
| **Repository** | `YOUR-USERNAME/ai-finance-incidents` |
| **Branch** | `main` |
| **Main file path** | `app.py` |
| **App URL** | Choose a name (e.g., `ai-finance-dashboard`) |

### 9.3 Configure Streamlit secrets

Before clicking Deploy, click on **"Advanced settings"** and then **"Secrets"**.

Paste the content below (replacing with real values):

```toml
# .streamlit/secrets.toml — configured in the Streamlit Cloud interface
GROQ_API_KEY = "gsk_YOUR_REAL_GROQ_KEY_HERE"
API_BASE_URL = "https://ai-finance-api.onrender.com"
```

> ⚠️ This content is saved encrypted on Streamlit Cloud. **Never** create the `.streamlit/secrets.toml` file locally or commit it to GitHub.

### 9.4 Deploy

Click on **"Deploy!"**. The process takes 2-4 minutes.

The final URL will be something like:  
`https://YOUR-USERNAME-ai-finance-dashboard.streamlit.app`

---

## 10. Connect Dashboard to the API in Production

`app.py` already resolves the URL automatically in the following order:

```
1. st.secrets["API_BASE_URL"]  → Streamlit Cloud (configured in step 9.3)
2. os.environ["API_BASE_URL"]  → local with .env
3. "http://localhost:5000"      → local fallback
```

**There is nothing to edit in the code.** Just ensure that the `API_BASE_URL` secret is configured in Streamlit Cloud with the Render URL.

To verify that the connection works, open the dashboard, go to the sidebar and confirm that it shows:

```
🟢 API online
```

If it shows `🔴 API offline`:
- Check if the API on Render is running (access the URL directly)
- Check if the `API_BASE_URL` in the Streamlit Cloud secrets is correct (without a trailing `/`)

---

## 11. Configure the Groq Key

### In production (Streamlit Cloud)

Already configured in step 9.3. `app.py` reads automatically from `st.secrets["GROQ_API_KEY"]`.

### In local development

In the `.env` file:
```env
GROQ_API_KEY=gsk_your_real_value_here
```

`app.py` reads from `os.environ.get("GROQ_API_KEY")` automatically.

### Manual fallback (without .env)

If you prefer not to use `.env`, the dashboard displays an input field on the **💬 AI Assistant** page where you can paste the key. It remains only for the current session, without being saved.

---

## 12. Final Validation

Execute this checklist before considering the deployment complete:

### Local

```
[ ] python app_api.py → starts without errors
[ ] streamlit run app.py → opens in browser
[ ] curl localhost:5000/ → returns JSON
[ ] curl localhost:5000/api/stats/by-application → returns data
[ ] Prediction via POST works and returns probability between 0 and 1
[ ] Dashboard shows "🟢 API online"
[ ] Chatbot answers a question (with Groq key configured)
```

### GitHub

```
[ ] .env does not appear in the repository
[ ] models/*.pkl are in the repository (if needed for Render)
[ ] database/*.db is in the repository (if needed for Render)
[ ] .gitignore is in the repository
[ ] requirements.txt is in the repository
[ ] Procfile is in the repository
```

### Render (API)

```
[ ] Deployment completed without errors in logs
[ ] GET https://your-api.onrender.com/ returns JSON
[ ] GET https://your-api.onrender.com/api/incidents returns list
[ ] POST https://your-api.onrender.com/api/predict/severity returns prediction
```

### Streamlit Cloud (Dashboard)

```
[ ] App opens without 500 error
[ ] API_BASE_URL secret configured with Render URL
[ ] GROQ_API_KEY secret configured
[ ] Sidebar shows "🟢 API online"
[ ] "🎯 Risk Predictor" page works end-to-end
[ ] Chatbot answers questions about the data
```

---

## 13. Common Errors and Solutions

| Error | Cause | Solution |
|---|---|---|
| `ModuleNotFoundError: No module named 'groq'` | Dependency not installed | `pip install groq` |
| `sqlite3.OperationalError: no such table` | Notebooks not executed | Execute NB1 first |
| `FileNotFoundError: models/severity_classifier.pkl` | Models not generated | Execute NB3 |
| `KeyError: 'GROQ_API_KEY'` in st.secrets | Secret not configured on Streamlit Cloud | Add it in the Secrets section |
| API returns `503 Models not loaded` | .pkl is not on Render | Include models/ in git commit |
| Dashboard shows `🔴 API offline` | Wrong URL or sleeping API | Check API_BASE_URL and access the Render URL directly |
| Render: `Build failed` | Missing dependency | Check requirements.txt |
| `Port already in use` | Another instance running | `pkill -f app_api.py` or restart terminal |

---

## Quick Summary (for pros)

```bash
# Setup
git clone <repo> && cd <repo>
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env && nano .env   # fill in GROQ_API_KEY

# Run locally
python app_api.py &
streamlit run app.py

# Deploy
git add . && git commit -m "deploy" && git push
# → Render: auto-deploy via GitHub integration
# → Streamlit Cloud: auto-deploy via GitHub integration
# Configure secrets on both platforms with GROQ_API_KEY and API_BASE_URL
```

---

*PUC-SP · Capstone Project · 2026*
