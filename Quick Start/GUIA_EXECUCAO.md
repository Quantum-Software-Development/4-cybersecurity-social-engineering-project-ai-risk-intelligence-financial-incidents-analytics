# 🚀 Guia de Execução — Passo a Passo Completo
## AI Incidents in Financial Services

**Para iniciantes · VS Code · Windows / macOS / Linux**

---

## ⚡ Antes de Começar — Checklist

```
[ ] Python 3.10 ou superior instalado
[ ] VS Code instalado
[ ] Terminal / Prompt de comando disponível
[ ] Arquivo incidents.csv baixado (instruções abaixo)
```

---

## PASSO 1 — Baixar e Abrir o Projeto no VS Code

### 1.1 Baixar o projeto

```bash
# Opção A: via Git
git clone https://github.com/seu-usuario/ai-finance-incidents.git
cd ai-finance-incidents

# Opção B: baixar como .zip
# Descompacte o arquivo e anote o caminho da pasta
```

### 1.2 Abrir no VS Code

```bash
# No terminal, dentro da pasta do projeto
code .
```

Ou: Arquivo → Abrir Pasta → selecione a pasta do projeto.

### 1.3 Instalar extensões recomendadas no VS Code

Pressione `Ctrl+Shift+X` e instale:
- **Python** (Microsoft)
- **Pylance**
- **Jupyter** (Microsoft)

---

## PASSO 2 — Criar e Ativar Ambiente Virtual

> **Por que?** Isola as dependências do projeto das do sistema, evitando conflitos.

### 2.1 Criar o ambiente

```bash
# Dentro da pasta do projeto — Terminal do VS Code (Ctrl+`)
python -m venv .venv
```

Você verá uma pasta `.venv/` criada no projeto.

### 2.2 Ativar o ambiente

```bash
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (Prompt de Comando)
.venv\Scripts\activate.bat

# macOS / Linux
source .venv/bin/activate
```

**Como saber se funcionou?**
O terminal mostrará `(.venv)` antes do prompt:
```
(.venv) PS C:\meu-projeto>   # Windows
(.venv) user@machine:~/meu-projeto$   # macOS/Linux
```

### 2.3 Selecionar o interpretador no VS Code

1. Pressione `Ctrl+Shift+P`
2. Digite: `Python: Select Interpreter`
3. Selecione `.venv`

---

## PASSO 3 — Instalar Dependências

```bash
# Verificar que o ambiente está ativo (deve aparecer (.venv))
# Instalar todas as dependências
pip install -r requirements.txt
```

**Tempo estimado**: 3–8 minutos (primeira vez).

### Verificar instalação

```bash
python -c "import pandas, streamlit, flask, xgboost; print('✅ Tudo instalado!')"
```

### Erros comuns nesta etapa

```
ERRO: Microsoft Visual C++ 14.0 is required (Windows)
SOLUÇÃO: Baixe "Build Tools for Visual Studio" em visualstudio.microsoft.com/downloads/

ERRO: error: command 'gcc' failed
SOLUÇÃO (Linux): sudo apt-get install python3-dev build-essential

ERRO: pip não encontrado
SOLUÇÃO: python -m pip install --upgrade pip
```

---

## PASSO 4 — Baixar o Dataset AIID

```bash
# Opção A: Kaggle CLI
pip install kaggle
# Configure: https://www.kaggle.com/docs/api
kaggle datasets download konradb/ai-incident-database
unzip ai-incident-database.zip
mv *.csv data/incidents.csv   # renomear para incidents.csv

# Opção B: Manual
# 1. Acesse: https://www.kaggle.com/datasets/konradb/ai-incident-database
# 2. Clique em "Download"
# 3. Extraia e coloque o CSV como: data/incidents.csv
# (ou na raiz do projeto como incidents.csv)
```

---

## PASSO 5 — Executar os Notebooks (ordem obrigatória!)

### 5.1 Registrar o ambiente virtual no Jupyter

```bash
python -m ipykernel install --user --name=.venv --display-name "Python (ai-finance)"
```

### 5.2 Abrir o Jupyter

```bash
# Opção A: Via VS Code
# Clique duplo em qualquer .ipynb → VS Code abre com Jupyter integrado

# Opção B: Jupyter clássico no navegador
jupyter notebook notebooks/
# → acesse http://localhost:8888
```

### 5.3 Executar NB1 — Exploração e Preparação

**Arquivo**: `notebooks/NB1_Exploracao_Preparacao.ipynb`

```
1. Abra o notebook
2. Selecione o kernel: "Python (ai-finance)"
3. Clique em "Run All" (ou Kernel → Restart & Run All)
4. Aguarde ~2-5 minutos
```

**O que será gerado:**
```
✅ data/incidents_finance_filtered.csv
✅ ai_finance_incidents.db
✅ distribuicao_variaveis.png
```

> **⚠️ Se a API AIID estiver offline**, o notebook carrega automaticamente o `incidents.csv` local. Isso é esperado.

### 5.4 Executar NB2 — Análise Estatística

**Arquivo**: `notebooks/NB2_Analise_Estatistica.ipynb`

```
Pré-requisito: NB1 executado com sucesso
Tempo estimado: ~1-2 minutos
```

**O que será gerado:**
```
✅ Resultados dos testes H1-H4 nas células de output
✅ Gráficos interativos Plotly
```

### 5.5 Executar NB3 — Modelagem ML

**Arquivo**: `notebooks/NB3_Modelagem_ML.ipynb`

```
Pré-requisito: NB1 executado com sucesso
Tempo estimado: ~5-10 minutos (treinamento dos modelos)
```

**O que será gerado:**
```
✅ models/severity_classifier.pkl
✅ models/investigation_classifier.pkl
✅ models/features_severity.pkl
✅ models/features_investigation.pkl
```

### 5.6 Executar NB4 — API RESTful

**Arquivo**: `notebooks/NB4_API_RESTful.ipynb`

```
Pré-requisito: NB1 + NB3 executados
Tempo estimado: ~1 minuto
```

**O que será gerado:**
```
✅ app_api.py (arquivo da API Flask)
```

> **Atenção**: Execute apenas as células de definição dos endpoints. A célula que chama `app.run()` deve ser executada no Terminal (passo 6), não no notebook.

---

## PASSO 6 — Iniciar a API Flask

**Abra um NOVO terminal** no VS Code (`Ctrl+Shift+5` ou Terminal → New Terminal):

```bash
# Ativar o ambiente virtual (se não estiver ativo)
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate       # Windows

# Iniciar a API
python app_api.py
```

**Saída esperada:**
```
 * Serving Flask app 'app_api'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.1.x:5000
```

**Testar no navegador ou terminal:**
```bash
# Novo terminal (terceiro)
curl http://localhost:5000/
curl http://localhost:5000/api/stats/by-application
```

> **Mantenha este terminal aberto enquanto usa o dashboard.**

---

## PASSO 7 — Iniciar o Dashboard Streamlit

**Abra outro terminal** (mantendo a API rodando no anterior):

```bash
# Ativar o ambiente virtual
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate       # Windows

# Iniciar o dashboard
streamlit run dashboard/app.py
```

**Saída esperada:**
```
  You can now view your Streamlit app in your browser.
  Local URL: http://localhost:8501
  Network URL: http://192.168.1.x:8501
```

O navegador abrirá automaticamente em `http://localhost:8501`.

---

## PASSO 8 — Configurar o Chatbot (opcional)

Para usar o chatbot com OpenAI GPT:

### 8.1 Criar arquivo .env

```bash
cp .env.example .env
```

### 8.2 Editar o .env

```bash
# .env
OPENAI_API_KEY=sk-...sua-chave-aqui...
```

### 8.3 No dashboard

1. Acesse a página **💬 Assistente IA**
2. Expanda "⚙️ Configuração da API OpenAI"
3. Cole sua chave e selecione o modelo

> **Sem chave**: o chatbot funciona em modo offline com respostas baseadas em palavras-chave.

---

## Resumo dos Terminais Necessários

| Terminal | Comando | URL |
|---|---|---|
| **Terminal 1** | `python app_api.py` | http://localhost:5000 |
| **Terminal 2** | `streamlit run dashboard/app.py` | http://localhost:8501 |
| **Terminal 3** | Jupyter (opcional) | http://localhost:8888 |

---

## Alternativa: Executar o NB5 (Pipeline Unificado)

Se preferir executar tudo em um único notebook:

```bash
# Abrir o notebook unificado
jupyter notebook notebooks/PROJETO_COMPLETO_UNIFICADO.ipynb
# → "Run All" executa as 4 fases em sequência
```

> **Recomendação**: prefira os notebooks separados para desenvolvimento. Use o NB5 apenas para demonstração.

---

## Erros Comuns e Soluções

| Erro | Solução |
|---|---|
| `ModuleNotFoundError` | `pip install -r requirements.txt` |
| `FileNotFoundError: incidents.csv` | Baixe o CSV (Passo 4) |
| `FileNotFoundError: ai_finance_incidents.db` | Execute NB1 |
| `FileNotFoundError: models/` | Execute NB3 |
| `API offline no dashboard` | Execute `python app_api.py` no Terminal 1 |
| `Port 5000 already in use` | `fuser -k 5000/tcp` (Linux) ou reinicie o PC |
| `Port 8501 already in use` | `streamlit run dashboard/app.py --server.port 8502` |
| `Kernel not found no Jupyter` | `python -m ipykernel install --user --name=.venv` |
| `(.venv) não aparece no terminal` | Execute o comando de ativação novamente |
| Dashboard não carrega dados | Verifique se NB1 foi executado e o CSV existe |

---

## Estrutura de Terminais Recomendada

```
VS Code com 3 terminais abertos simultaneamente:

┌──────────────────────────────────────────────────────────┐
│ Terminal 1         │ Terminal 2          │ Terminal 3     │
│ python app_api.py  │ streamlit run       │ jupyter        │
│ (API Flask)        │ dashboard/app.py    │ notebook       │
│ → :5000            │ (Dashboard)         │ → :8888        │
│                    │ → :8501             │                │
└──────────────────────────────────────────────────────────┘
```

Para abrir múltiplos terminais no VS Code: `Ctrl+Shift+5` ou clique no ícone `+` no painel de terminais.

---

*PUC-SP · Projeto Integrador · 2026*
