# 🚀 Guia Completo de Execução e Deploy
## AI Finance Incidents — Do Zero ao Ar

> **Para quem é este guia:**  
> ✅ Iniciantes — cada passo explicado do zero  
> ✅ Profissionais — referência rápida com todos os comandos  

---

## 📋 Índice

1. [Pré-requisitos](#1-pré-requisitos)
2. [Clonar e configurar o projeto localmente](#2-clonar-e-configurar-o-projeto-localmente)
3. [Configurar variáveis de ambiente](#3-configurar-variáveis-de-ambiente)
4. [Preparar dados e modelos](#4-preparar-dados-e-modelos)
5. [Executar localmente](#5-executar-localmente)
6. [Testar a API localmente](#6-testar-a-api-localmente)
7. [Publicar no GitHub](#7-publicar-no-github)
8. [Deploy da API no Render](#8-deploy-da-api-no-render)
9. [Deploy do Dashboard no Streamlit Cloud](#9-deploy-do-dashboard-no-streamlit-cloud)
10. [Conectar Dashboard à API em produção](#10-conectar-dashboard-à-api-em-produção)
11. [Configurar a chave Groq](#11-configurar-a-chave-groq)
12. [Validação final](#12-validação-final)
13. [Erros comuns e soluções](#13-erros-comuns-e-soluções)

---

## 1. Pré-requisitos

### O que você precisa ter instalado

| Ferramenta | Como verificar | Como instalar |
|---|---|---|
| Python 3.10+ | `python --version` | https://python.org/downloads |
| Git | `git --version` | https://git-scm.com |
| VS Code (recomendado) | — | https://code.visualstudio.com |

### Contas necessárias (todas gratuitas)

| Plataforma | Para quê | Link |
|---|---|---|
| GitHub | Repositório do código | https://github.com |
| Render | Hospedar a API Flask | https://render.com |
| Streamlit Cloud | Hospedar o dashboard | https://share.streamlit.io |
| Groq | API do chatbot | https://console.groq.com |

---

## 2. Clonar e Configurar o Projeto Localmente

### 2.1 Abrir o terminal

- **Windows:** `Win + R` → digitar `cmd` → Enter  
- **Mac:** `Cmd + Espaço` → digitar `Terminal` → Enter  
- **VS Code:** Menu `Terminal` → `New Terminal`

### 2.2 Navegar até onde você quer salvar o projeto

```bash
# Exemplo: ir para a pasta Documentos
cd ~/Documents   # Mac/Linux
cd %USERPROFILE%\Documents   # Windows
```

### 2.3 Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/ai-finance-incidents.git
cd ai-finance-incidents
```

> **Se ainda não tem repositório no GitHub**, crie uma pasta local:
> ```bash
> mkdir ai-finance-incidents
> cd ai-finance-incidents
> ```

### 2.4 Criar o ambiente virtual Python

```bash
# Criar
python -m venv .venv

# Ativar — Mac/Linux
source .venv/bin/activate

# Ativar — Windows PowerShell
.venv\Scripts\Activate.ps1

# Ativar — Windows CMD
.venv\Scripts\activate.bat
```

> 💡 **Como saber se funcionou?** O terminal mostrará `(.venv)` antes do cursor.

### 2.5 Instalar dependências

```bash
pip install -r requirements.txt
```

> ⏱ Isso leva 2–5 minutos na primeira vez. É normal.

---

## 3. Configurar Variáveis de Ambiente

### 3.1 Criar o arquivo `.env`

```bash
# Mac/Linux
cp .env.example .env

# Windows
copy .env.example .env
```

### 3.2 Editar o `.env`

Abra o arquivo `.env` no VS Code ou qualquer editor de texto e preencha:

```env
# ─── API Flask ────────────────────────────────────────────
PORT=5000

# ─── Dashboard ────────────────────────────────────────────
# Em produção: cole a URL do Render depois do deploy
API_BASE_URL=http://localhost:5000

# ─── Chatbot Groq ─────────────────────────────────────────
# Obter em: https://console.groq.com/keys
GROQ_API_KEY=your_groq_api_key_here
```

### 3.3 Obter a chave Groq (gratuita)

1. Acesse https://console.groq.com
2. Crie uma conta (pode usar Google ou email)
3. Clique em **"API Keys"** no menu lateral
4. Clique em **"Create API Key"**
5. Dê um nome (ex: `ai-finance-local`)
6. **Copie a chave** — ela só aparece uma vez!
7. Cole no `.env` no lugar de `your_groq_api_key_here`

> ⚠️ **NUNCA commite o arquivo `.env` para o Git.** Ele já está no `.gitignore`.

---

## 4. Preparar Dados e Modelos

### 4.1 Estrutura de pastas necessária

Crie as pastas se não existirem:

```bash
mkdir -p database models
touch database/.gitkeep models/.gitkeep
```

### 4.2 Executar os notebooks para gerar os dados

> Execute nesta ordem exata. Cada notebook gera arquivos usados pelo próximo.

```bash
# Registrar o kernel do ambiente virtual no Jupyter
python -m ipykernel install --user --name=.venv --display-name "AI Finance"

# Abrir Jupyter
jupyter notebook
```

No navegador que abrir:

| Ordem | Notebook | O que gera |
|---|---|---|
| 1º | `NB1_Exploracao_Preparacao.ipynb` | `incidents_finance_filtered.csv` + banco SQLite |
| 2º | `NB2_Analise_Estatistica.ipynb` | análises estatísticas |
| 3º | `NB3_Modelagem_ML.ipynb` | `models/*.pkl` (modelos treinados) |
| 4º | `NB4_API_RESTful.ipynb` | (opcional — documenta a API) |

> 💡 **Dica:** No VS Code, você pode abrir os notebooks direto sem precisar do navegador.

---

## 5. Executar Localmente

Você precisa de **dois terminais abertos ao mesmo tempo**.

### Terminal 1 — API Flask

```bash
# Com (.venv) ativo
python app_api.py
```

Saída esperada:
```
============================================================
🚀 API rodando em http://localhost:5000
============================================================
 * Serving Flask app 'app_api'
 * Running on http://0.0.0.0:5000
```

### Terminal 2 — Dashboard Streamlit

```bash
# Com (.venv) ativo (abra um novo terminal)
streamlit run app.py
```

Saída esperada:
```
  You can now view your Streamlit app in your browser.
  Local URL: http://localhost:8501
```

O navegador abrirá automaticamente em `http://localhost:8501`.

---

## 6. Testar a API Localmente

### Teste rápido no navegador

Abra: http://localhost:5000

Deve aparecer um JSON com a documentação da API.

### Testes com curl (terminal)

```bash
# Status da API
curl http://localhost:5000/

# Listar incidentes
curl "http://localhost:5000/api/incidents?limit=5"

# Estatísticas por aplicação
curl http://localhost:5000/api/stats/by-application

# Predição de severidade
curl -X POST http://localhost:5000/api/predict/severity \
  -H "Content-Type: application/json" \
  -d '{"application_type":"credit_scoring","incident_type":"algorithmic_bias","customer_segment":"retail","year":2024}'
```

### Teste com Python

```python
import requests

# Ping
r = requests.get("http://localhost:5000/")
print(r.json())

# Predição
payload = {
    "application_type": "credit_scoring",
    "incident_type": "algorithmic_bias",
    "customer_segment": "retail",
    "year": 2024
}
r = requests.post("http://localhost:5000/api/predict/severity", json=payload)
print(r.json())
# Esperado: {"prediction": 0 ou 1, "probability": 0.xx}
```

---

## 7. Publicar no GitHub

### 7.1 Criar repositório no GitHub

1. Acesse https://github.com → clique em **"New repository"**
2. Nome: `ai-finance-incidents`
3. Deixe **Private** (recomendado enquanto em desenvolvimento)
4. **NÃO** marque "Initialize with README" (você já tem um)
5. Clique em **"Create repository"**

### 7.2 Inicializar Git localmente

```bash
git init
git add .
git commit -m "feat: initial commit — API + Dashboard securizados"
```

### 7.3 Conectar e enviar ao GitHub

```bash
# Substitua SEU-USUARIO pelo seu usuário GitHub
git remote add origin https://github.com/SEU-USUARIO/ai-finance-incidents.git
git branch -M main
git push -u origin main
```

### 7.4 Verificar o que foi enviado

Acesse https://github.com/SEU-USUARIO/ai-finance-incidents e confirme:

- ✅ `.env` NÃO aparece (está no .gitignore)
- ✅ `models/` NÃO aparece com arquivos .pkl
- ✅ `database/` NÃO aparece com o .db
- ✅ `.gitignore` aparece
- ✅ `requirements.txt` aparece
- ✅ `app.py` e `app_api.py` aparecem

> ⚠️ Se `.env` ou `.db` aparecerem no GitHub, **remova imediatamente**:
> ```bash
> git rm --cached .env
> git commit -m "fix: remove .env from tracking"
> git push
> ```

---

## 8. Deploy da API no Render

### 8.1 O que é o Render

Render é uma plataforma de hospedagem em nuvem com plano gratuito. A API Flask ficará disponível em uma URL pública como `https://ai-finance-api.onrender.com`.

### 8.2 Preparar arquivos de deploy

Crie o arquivo `Procfile` na raiz do projeto:

```bash
echo "web: gunicorn app_api:app --workers 2 --bind 0.0.0.0:\$PORT" > Procfile
```

Crie o arquivo `render.yaml` na raiz:

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

Commite esses arquivos:

```bash
git add Procfile render.yaml
git commit -m "feat: add Render deploy config"
git push
```

### 8.3 Criar o serviço no Render

1. Acesse https://render.com e clique em **"Sign Up"**
2. Faça login com sua conta GitHub (facilita a integração)
3. No dashboard, clique em **"New +"** → **"Web Service"**
4. Selecione **"Connect a repository"**
5. Escolha o repositório `ai-finance-incidents`
6. Configure:

| Campo | Valor |
|---|---|
| **Name** | `ai-finance-api` |
| **Region** | Oregon (US West) — gratuito |
| **Branch** | `main` |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app_api:app --workers 2 --bind 0.0.0.0:$PORT` |
| **Instance Type** | Free |

### 8.4 Configurar variáveis de ambiente no Render

Na mesma tela de configuração, clique em **"Environment Variables"** e adicione:

| Key | Value |
|---|---|
| `PORT` | `5000` |
| `PYTHON_VERSION` | `3.11.0` |

> ⚠️ **Importante sobre dados:** O Render Free não persiste arquivos entre deploys. O banco `.db` e os modelos `.pkl` precisam ser **incluídos no repositório** ou carregados de um storage externo. Para fins acadêmicos, inclua-os no commit:
> ```bash
> # Remova as linhas de database/ e models/ do .gitignore
> # Depois:
> git add database/ models/
> git commit -m "feat: include database and models for Render deploy"
> git push
> ```

### 8.5 Iniciar o deploy

Clique em **"Create Web Service"**. O Render irá:

1. Clonar seu repositório
2. Executar `pip install -r requirements.txt`
3. Iniciar com Gunicorn

Acompanhe os logs em tempo real na aba **"Logs"**.

### 8.6 Verificar o deploy

Após ~2-3 minutos, a URL aparecerá no topo da página. Teste:

```bash
curl https://ai-finance-api.onrender.com/
```

> 💡 **Plano gratuito:** A API "adormece" após 15 minutos sem uso. A primeira requisição demora ~30 segundos para "acordar". Isso é normal no plano gratuito.

---

## 9. Deploy do Dashboard no Streamlit Cloud

### 9.1 Acessar o Streamlit Community Cloud

1. Acesse https://share.streamlit.io
2. Clique em **"Sign in with GitHub"**

### 9.2 Criar o app

1. Clique em **"New app"**
2. Configure:

| Campo | Valor |
|---|---|
| **Repository** | `SEU-USUARIO/ai-finance-incidents` |
| **Branch** | `main` |
| **Main file path** | `app.py` |
| **App URL** | Escolha um nome (ex: `ai-finance-dashboard`) |

### 9.3 Configurar secrets do Streamlit

Antes de clicar em Deploy, clique em **"Advanced settings"** e depois em **"Secrets"**.

Cole o conteúdo abaixo (substituindo pelos valores reais):

```toml
# .streamlit/secrets.toml — configurado na interface do Streamlit Cloud
GROQ_API_KEY = "gsk_SEU_GROQ_KEY_REAL_AQUI"
API_BASE_URL = "https://ai-finance-api.onrender.com"
```

> ⚠️ Este conteúdo é salvo de forma criptografada no Streamlit Cloud. **Nunca** crie o arquivo `.streamlit/secrets.toml` localmente nem commite ao GitHub.

### 9.4 Deploy

Clique em **"Deploy!"**. O processo leva 2-4 minutos.

A URL final será algo como:  
`https://SEU-USUARIO-ai-finance-dashboard.streamlit.app`

---

## 10. Conectar Dashboard à API em Produção

O `app.py` já resolve a URL automaticamente na seguinte ordem:

```
1. st.secrets["API_BASE_URL"]  → Streamlit Cloud (configurado no passo 9.3)
2. os.environ["API_BASE_URL"]  → local com .env
3. "http://localhost:5000"      → fallback local
```

**Não há nada para editar no código.** Basta garantir que o secret `API_BASE_URL` está configurado no Streamlit Cloud com a URL do Render.

Para verificar que a conexão funciona, abra o dashboard, vá na barra lateral e confirme que aparece:

```
🟢 API online
```

Se aparecer `🔴 API offline`:
- Verifique se a API no Render está rodando (acesse a URL direto)
- Verifique se o `API_BASE_URL` nos secrets do Streamlit Cloud está correto (sem `/` no final)

---

## 11. Configurar a Chave Groq

### Em produção (Streamlit Cloud)

Já configurado no passo 9.3. O `app.py` lê automaticamente de `st.secrets["GROQ_API_KEY"]`.

### Em desenvolvimento local

No arquivo `.env`:
```env
GROQ_API_KEY=gsk_seu_valor_real_aqui
```

O `app.py` lê de `os.environ.get("GROQ_API_KEY")` automaticamente.

### Fallback manual (sem .env)

Se preferir não usar `.env`, o dashboard exibe um campo de input na página **💬 Assistente IA** onde você pode colar a chave. Ela fica apenas na sessão atual, sem ser salva.

---

## 12. Validação Final

Execute este checklist antes de considerar o deploy concluído:

### Local

```
[ ] python app_api.py → inicia sem erros
[ ] streamlit run app.py → abre no navegador
[ ] curl localhost:5000/ → retorna JSON
[ ] curl localhost:5000/api/stats/by-application → retorna dados
[ ] Predição via POST funciona e retorna probabilidade entre 0 e 1
[ ] Dashboard mostra "🟢 API online"
[ ] Chatbot responde uma pergunta (com chave Groq configurada)
```

### GitHub

```
[ ] .env não aparece no repositório
[ ] models/*.pkl estão no repositório (se necessário para Render)
[ ] database/*.db está no repositório (se necessário para Render)
[ ] .gitignore está no repositório
[ ] requirements.txt está no repositório
[ ] Procfile está no repositório
```

### Render (API)

```
[ ] Deploy concluído sem erros nos logs
[ ] GET https://sua-api.onrender.com/ retorna JSON
[ ] GET https://sua-api.onrender.com/api/incidents retorna lista
[ ] POST https://sua-api.onrender.com/api/predict/severity retorna predição
```

### Streamlit Cloud (Dashboard)

```
[ ] App abre sem erro 500
[ ] API_BASE_URL secret configurado com URL do Render
[ ] GROQ_API_KEY secret configurado
[ ] Sidebar mostra "🟢 API online"
[ ] Página "🎯 Preditor de Risco" funciona end-to-end
[ ] Chatbot responde perguntas sobre os dados
```

---

## 13. Erros Comuns e Soluções

| Erro | Causa | Solução |
|---|---|---|
| `ModuleNotFoundError: No module named 'groq'` | Dependência não instalada | `pip install groq` |
| `sqlite3.OperationalError: no such table` | Notebooks não executados | Execute NB1 primeiro |
| `FileNotFoundError: models/severity_classifier.pkl` | Modelos não gerados | Execute NB3 |
| `KeyError: 'GROQ_API_KEY'` em st.secrets | Secret não configurado no Streamlit Cloud | Adicionar na seção Secrets |
| API retorna `503 Modelos não carregados` | .pkl não está no Render | Incluir models/ no git commit |
| Dashboard mostra `🔴 API offline` | URL errada ou API adormecida | Verificar API_BASE_URL e acessar a URL do Render diretamente |
| Render: `Build failed` | Dependência faltando | Verificar requirements.txt |
| `Port already in use` | Outra instância rodando | `pkill -f app_api.py` ou reiniciar terminal |

---

## Resumo Rápido (para pros)

```bash
# Setup
git clone <repo> && cd <repo>
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env && nano .env   # preencher GROQ_API_KEY

# Rodar local
python app_api.py &
streamlit run app.py

# Deploy
git add . && git commit -m "deploy" && git push
# → Render: auto-deploy via GitHub integration
# → Streamlit Cloud: auto-deploy via GitHub integration
# Configurar secrets nas duas plataformas com GROQ_API_KEY e API_BASE_URL
```

---

*PUC-SP · Projeto Integrador · 2026*
