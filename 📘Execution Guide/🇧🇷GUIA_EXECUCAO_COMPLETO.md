# 🚀 Guia de Execução Completo
## AI Incidents in Financial Services · Do Zero ao Dashboard

**Para iniciantes · VS Code · macOS/Linux/Windows**

---

## Visão Geral

Este guia ensina como executar o projeto completo do zero: desde instalar o Python até ter o dashboard rodando com o chatbot Groq funcionando.

```
Tempo estimado para execução completa: 30–45 minutos
Nível: Iniciante com conhecimento básico de terminal
```

### O que você vai ter ao final

| Componente | URL | Descrição |
|---|---|---|
| **API Flask** | http://localhost:5000 | Backend com 9 endpoints |
| **Dashboard** | http://localhost:8501 | Interface visual interativa |
| **Chatbot Groq** | (dentro do dashboard) | IA para perguntas sobre os dados |

---

## ✅ Pré-requisitos

Antes de começar, confirme que você tem:

```
[ ] Python 3.10 ou superior
[ ] VS Code instalado
[ ] Git instalado (opcional, mas recomendado)
[ ] Conta Groq criada (gratuita) — ver Seção 4
[ ] Conta Kaggle (para baixar o dataset) — opcional
```

### Verificar versão do Python

```bash
python3 --version
# Deve mostrar: Python 3.10.x ou superior
```

Se não tiver Python, baixe em: https://python.org/downloads

---

## 📥 1. Obter o Projeto

### Opção A — Com Git

```bash
git clone https://github.com/seu-usuario/ai-finance-incidents.git
cd ai-finance-incidents
```

### Opção B — Download manual

1. Baixe o `.zip` do repositório
2. Descompacte em uma pasta de sua escolha
3. Abra o terminal nessa pasta

### Abrir no VS Code

```bash
code .
```

Ou: `File → Open Folder → selecione a pasta do projeto`

---

## 🔧 2. Instalação do Ambiente

### 2.1 Criar ambiente virtual

> **Por que?** O ambiente virtual isola as dependências do projeto, evitando conflitos com outros projetos Python no seu computador.

```bash
# Criar o ambiente virtual
python3 -m venv .venv

# Ativar — macOS/Linux
source .venv/bin/activate

# Ativar — Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Ativar — Windows (Prompt de Comando)
.venv\Scripts\activate.bat
```

**Como saber que funcionou?** O terminal mostrará `(.venv)` antes do caminho:
```
(.venv) usuario@maquina:~/ai-finance-incidents$
```

### 2.2 Instalar dependências

```bash
pip install -r requirements.txt
```

> ⏱ Isso leva 3–8 minutos na primeira vez. É normal.

### 2.3 Registrar kernel no Jupyter

> Esse passo é necessário uma única vez para que os notebooks reconheçam o ambiente virtual.

```bash
python -m ipykernel install --user \
  --name=.venv \
  --display-name "Python (ai-finance)"
```

### 2.4 Verificar instalação

```bash
python -c "import pandas, streamlit, flask, xgboost; print('✅ Tudo instalado!')"
```

---

## 📊 3. Obter o Dataset

O projeto precisa do arquivo `incidents.csv` da AI Incident Database.

### Opção A — Kaggle CLI (recomendado)

```bash
pip install kaggle

# Configure suas credenciais (só na primeira vez):
# 1. Acesse https://kaggle.com/your-account
# 2. Clique em "Create New API Token"
# 3. Mova o arquivo kaggle.json para ~/.kaggle/

kaggle datasets download konradb/ai-incident-database
unzip ai-incident-database.zip -d data/raw/
```

### Opção B — Download manual

1. Acesse: https://www.kaggle.com/datasets/konradb/ai-incident-database
2. Clique em "Download"
3. Extraia e coloque o CSV em `data/raw/incidents.csv`

### Opção C — Sem dataset (dados demo)

Se não tiver acesso, o projeto funciona com dados de demonstração gerados automaticamente. Apenas avance para o próximo passo.

---

## 🔑 4. Configuração da API Groq

### 4.1 Criar conta e obter chave (gratuito, 2 minutos)

1. Acesse **https://console.groq.com**
2. Clique em "Sign Up" e crie uma conta gratuita
3. No painel, vá em **"API Keys"**
4. Clique em **"Create API Key"**
5. Nomeie como `ai-finance-project`
6. **Copie a chave** (começa com `gsk_...`) — ela aparece apenas uma vez!

### 4.2 Criar arquivo `.env` (execução local)

Na raiz do projeto, crie um arquivo chamado `.env`:

```bash
# macOS/Linux — criar pelo terminal
cat > .env << 'EOF'
GROQ_API_KEY=gsk_sua_chave_aqui
API_BASE_URL=http://localhost:5000
EOF
```

**Windows** — crie o arquivo manualmente com Bloco de Notas:
```
GROQ_API_KEY=gsk_sua_chave_aqui
API_BASE_URL=http://localhost:5000
```
Salve como `.env` (sem extensão `.txt`) na raiz do projeto.

### 4.3 Verificar o arquivo

```bash
cat .env
# Deve mostrar:
# GROQ_API_KEY=gsk_...
# API_BASE_URL=http://localhost:5000
```

> ⚠️ **Nunca commite o arquivo `.env` para o Git!** Ele já está no `.gitignore`.

---

## 📓 5. Executar os Notebooks

> **Regra importante**: sempre execute na ordem NB1 → NB2 → NB3 → NB4. Cada notebook gera arquivos que o próximo precisa.

### 5.1 Iniciar o Jupyter

```bash
jupyter notebook notebooks/
```

O navegador abrirá automaticamente em `http://localhost:8888`.

### 5.2 Selecionar o kernel correto

Ao abrir qualquer notebook:
1. Clique em "Kernel" → "Change Kernel"
2. Selecione **"Python (ai-finance)"**
3. Confirme

### 5.3 Notebook 1 — Exploração e Preparação

**Arquivo**: `NB1_Exploracao_Preparacao.ipynb`

```
Clique em: Kernel → Restart & Run All
Aguarde: ~2–5 minutos
```

**O que acontece**:
- Tenta conectar à API AIID GraphQL
- Se offline → usa cache ou `incidents.csv`
- Filtra incidentes financeiros por palavras-chave
- Cria 8 variáveis derivadas (application_type, severity_level, etc.)
- Salva o CSV processado e o banco SQLite

**Arquivos gerados**:
```
✅ data/incidents_finance_filtered.csv
✅ ai_finance_incidents.db
✅ assets/distribuicao_variaveis.png
```

### 5.4 Notebook 2 — Análise Estatística

**Arquivo**: `NB2_Analise_Estatistica.ipynb`

```
Clique em: Kernel → Restart & Run All
Aguarde: ~1–2 minutos
```

**O que acontece**:
- Estatística descritiva completa
- Testes H1–H4 (qui-quadrado, Spearman, regressão logística)
- Gráficos interativos Plotly

### 5.5 Notebook 3 — Modelagem de ML

**Arquivo**: `NB3_Modelagem_ML.ipynb`

```
Clique em: Kernel → Restart & Run All
Aguarde: ~3–5 minutos (treinamento dos modelos)
```

**Arquivos gerados**:
```
✅ models/severity_classifier.pkl
✅ models/investigation_classifier.pkl
✅ models/features_severity.pkl
✅ models/features_investigation.pkl
```

> ℹ️ Os modelos podem mostrar F1-Score próximo de 0. Isso é esperado — a base tem apenas ~31 incidentes com forte desbalanceamento de classes. O pipeline está correto; faltam mais dados para performance real.

### 5.6 Notebook 4 — API RESTful

**Arquivo**: `NB4_API_RESTful.ipynb`

```
Clique em: Kernel → Restart & Run All
Aguarde: ~1–2 minutos
```

**Arquivo gerado**:
```
✅ api/app_api.py
```

> ⚠️ **Não execute a célula final** que chama `app.run()` dentro do notebook — isso travaria o kernel. A API deve ser iniciada pelo terminal (próximo passo).

---

## 🚀 6. Executar a API Flask

Abra um **novo terminal** no VS Code (`Ctrl + Shift + `` ` ``):

```bash
# Ativar o ambiente virtual (se não estiver ativo)
source .venv/bin/activate

# Iniciar a API
python api/app_api.py
```

**Saída esperada**:
```
✅ Modelos ML carregados com sucesso.
🚀 AI Finance Incidents API — Iniciando
📡 API disponível em: http://localhost:5000
 * Running on http://0.0.0.0:5000
```

### Testar a API

Em outro terminal ou no navegador:

```bash
# Verificar status
curl http://localhost:5000/

# Listar incidentes
curl "http://localhost:5000/api/incidents?limit=5"

# Estatísticas por aplicação
curl http://localhost:5000/api/stats/by-application

# Predição de severidade
curl -X POST http://localhost:5000/api/predict/severity \
  -H "Content-Type: application/json" \
  -d '{"application_type":"credit_scoring","incident_type":"algorithmic_bias",
       "customer_segment":"retail","year":2024,"fine_imposed":0,
       "policy_change":0,"third_party_audit":0}'
```

> ✅ Se receber um JSON de resposta, a API está funcionando corretamente.

> **Mantenha este terminal aberto enquanto usa o dashboard.**

---

## 🖥️ 7. Executar o Dashboard Streamlit

Abra **outro terminal** (mantendo o da API aberto):

```bash
# Ativar o ambiente virtual
source .venv/bin/activate

# Iniciar o dashboard
streamlit run dashboard/app.py
```

**Saída esperada**:
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

O navegador abrirá automaticamente. Se não abrir, acesse: **http://localhost:8501**

---

## 💬 8. Testar o Chatbot

### 8.1 Acessar a página do chatbot

No dashboard, clique em **"💬 Assistente IA"** na sidebar esquerda.

### 8.2 Verificar configuração da chave

O dashboard lê a chave Groq automaticamente do arquivo `.env`. Você verá:

```
✅ Groq configurada via variável de ambiente · modelo: llama-3.1-8b-instant
```

Se não aparecer, configure manualmente:
1. Expanda o painel **"⚙️ Configurar API Groq (gratuita)"**
2. Cole sua chave `gsk_...`
3. Clique fora do campo

### 8.3 Perguntas para testar

Clique nas sugestões ou escreva:
- *"Qual aplicação tem mais incidentes?"*
- *"Explique os testes de hipóteses H1 a H4"*
- *"Como o XGBoost foi usado no projeto?"*
- *"Quais segmentos são mais afetados por viés?"*

### 8.4 Modo offline (sem chave)

Sem chave Groq configurada, o chatbot responde com base em palavras-chave locais — funciona para as principais perguntas sobre o projeto.

---

## ⚠️ 9. Erros Comuns e Soluções

| Erro | Causa provável | Solução |
|---|---|---|
| `ModuleNotFoundError: No module named 'X'` | Dependência não instalada | `pip install -r requirements.txt` |
| `(.venv)` não aparece no terminal | Ambiente não ativado | Execute o comando `source .venv/bin/activate` novamente |
| `FileNotFoundError: incidents.csv` | Dataset não baixado | Seguir a Seção 3 |
| `FileNotFoundError: ai_finance_incidents.db` | NB1 não foi executado | Execute o Notebook 1 primeiro |
| `FileNotFoundError: models/severity_classifier.pkl` | NB3 não foi executado | Execute o Notebook 3 primeiro |
| API offline no dashboard | Terminal com a API foi fechado | Abra novo terminal e execute `python api/app_api.py` |
| `Address already in use (port 5000)` | Outra instância da API rodando | Execute: `lsof -ti:5000 \| xargs kill` (macOS/Linux) |
| `Address already in use (port 8501)` | Outro dashboard rodando | `streamlit run dashboard/app.py --server.port 8502` |
| Kernel não encontrado no Jupyter | `.venv` não registrado | `python -m ipykernel install --user --name=.venv` |
| Chatbot não responde (Groq) | Chave inválida ou sem internet | Verifique a chave em console.groq.com |
| Dashboard abre mas sem dados | CSV não encontrado | Verifique se NB1 gerou `incidents_finance_filtered.csv` |

---

## ✅ 10. Checklist Final

Execute este checklist para confirmar que tudo está funcionando:

### Ambiente
```
[ ] Python 3.10+ instalado
[ ] Ambiente virtual (.venv) criado e ativado
[ ] requirements.txt instalado sem erros
[ ] Kernel Jupyter registrado
```

### Dados e modelos
```
[ ] data/incidents_finance_filtered.csv existe
[ ] ai_finance_incidents.db existe
[ ] models/severity_classifier.pkl existe
[ ] models/investigation_classifier.pkl existe
[ ] models/features_severity.pkl existe
[ ] models/features_investigation.pkl existe
```

### API
```
[ ] Terminal 1: python api/app_api.py está rodando
[ ] curl http://localhost:5000/ retorna JSON
[ ] Endpoint de predição responde sem erro
```

### Dashboard
```
[ ] Terminal 2: streamlit run dashboard/app.py está rodando
[ ] http://localhost:8501 abre no navegador
[ ] Sidebar mostra "🟢 API online"
[ ] Página Visão Geral mostra KPIs
[ ] Página API Explorer mostra status da API
[ ] Chatbot responde (modo Groq ou offline)
```

### Groq
```
[ ] Arquivo .env criado com GROQ_API_KEY
[ ] Dashboard mostra "✅ Groq configurada via variável de ambiente"
[ ] Chatbot responde perguntas sobre os dados
```

---

## 📌 Resumo Rápido (para quem já conhece o projeto)

```bash
# 1. Ambiente
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 2. Dataset
# Coloque incidents.csv em data/raw/

# 3. Notebooks (Jupyter ou VS Code)
# Execute: NB1 → NB2 → NB3 → NB4

# 4. API (Terminal 1)
python api/app_api.py

# 5. Dashboard (Terminal 2)
streamlit run dashboard/app.py

# 6. Configurar Groq
echo "GROQ_API_KEY=gsk_..." >> .env
```

---

*PUC-SP · Projeto Integrador · 5º Semestre · 2026*
