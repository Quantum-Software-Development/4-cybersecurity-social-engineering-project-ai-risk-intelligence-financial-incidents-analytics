# 🔬 Análise Técnica do Projeto


---

## Organização: .ipynb vs .py

### Onde deve ficar cada arquivo?

```
CORRETA organização do projeto:

ai-finance-incidents/
│
├── notebooks/                   ← TODOS os .ipynb ficam aqui
│   ├── NB1_Exploracao_Preparacao.ipynb
│   ├── NB2_Analise_Estatistica.ipynb
│   ├── NB3_Modelagem_ML.ipynb
│   ├── NB4_API_RESTful.ipynb
│   └── PROJETO_COMPLETO_UNIFICADO.ipynb
│
├── app_api.py                   ← API Flask (RAIZ do projeto)
│
└── dashboard/                   ← Dashboard em subpasta separada
    ├── app.py                   ← Streamlit
    └── .streamlit/config.toml
```

### Por que `app_api.py` fica na RAIZ?

O arquivo da API Flask precisa encontrar:
- `ai_finance_incidents.db` (gerado pelo NB1 na raiz)
- `models/*.pkl` (gerados pelo NB3 na raiz)

Se ficasse em uma subpasta, os caminhos relativos quebrariam:

```python
# app_api.py — funcionaria na raiz
DATABASE    = "ai_finance_incidents.db"       # ✅ encontra
MODELS_PATH = "models"                         # ✅ encontra

# Se estivesse em /api/app.py — quebraria
DATABASE    = "../ai_finance_incidents.db"     # ❌ frágil
MODELS_PATH = "../models"                      # ❌ frágil
```

### Por que `dashboard/app.py` fica em SUBPASTA separada?

**Problema real**: Se ambos os arquivos se chamassem `app.py` e ficassem na mesma pasta, ao executar `streamlit run app.py` o Python poderia importar o errado, causando conflito.

**Solução adotada**: nomear a API como `app_api.py` (ou `api.py`) e o dashboard como `dashboard/app.py`.

```
NUNCA faça:
projeto/
├── app.py   ← API Flask (confunde com o dashboard)
└── app.py   ← Dashboard Streamlit (impossível!)

CORRETO:
projeto/
├── app_api.py          ← API Flask
└── dashboard/app.py    ← Dashboard Streamlit
```

### Notebooks dentro de `notebooks/` (NÃO na raiz)

**Por quê?**
1. Mantém a raiz limpa (só `app_api.py`, `requirements.txt`, `README.md`)
2. Separa análise (notebooks) de produção (código Python)
3. Facilita ignorar notebooks no `.gitignore` de produção

### Como integrar notebooks com .py?

Os notebooks **geram** os artefatos que o código Python **consome**:

```
Notebooks GERAM:                    .py CONSOME:
─────────────────────────────────────────────────────
NB1 → incidents_finance_filtered.csv  → dashboard/app.py (load_csv)
NB1 → ai_finance_incidents.db         → app_api.py (query_db)
NB3 → models/*.pkl                    → app_api.py (joblib.load)
NB3 → models/*.pkl                    → dashboard/app.py (via API)
NB4 → app_api.py                      → arquivo final do projeto
```

O código Python **nunca importa** os notebooks diretamente.

---

## Requirements: Separados ou Unificados?

### Recomendação: UM ÚNICO `requirements.txt` para este projeto

**Justificativa**:

```
CONTEXTO           RECOMENDAÇÃO       POR QUÊ
───────────────────────────────────────────────────────────────
Projeto acadêmico  → Unificado        Simplicidade, manutenção
Portfólio          → Unificado        Menos fricção para avaliadores
Produção startup   → Separados        Deploy em serviços distintos
Microserviços      → Separados        Containers independentes
```

Para um projeto acadêmico de portfólio, requirements separados criam complexidade desnecessária:

```bash
# Com requirements separados — confuso para avaliadores:
pip install -r requirements_api.txt
pip install -r requirements_dashboard.txt
pip install -r requirements_notebooks.txt
# Qual devo usar? Todos? Apenas um?

# Com requirements unificado — simples e direto:
pip install -r requirements.txt
# Funcionou. Próximo passo.
```

### `requirements.txt` Unificado — Versão Final Corrigida

```
# ═══════════════════════════════════════════════════════════
# requirements.txt — AI Incidents in Financial Services
# Python 3.10+ | PUC-SP 2026
# ═══════════════════════════════════════════════════════════

# ── Dados ──────────────────────────────────────────────────
pandas>=2.0.0
numpy>=1.24.0

# ── Visualização ───────────────────────────────────────────
matplotlib>=3.7.0
seaborn>=0.12.0
plotly>=5.18.0

# ── Estatística ────────────────────────────────────────────
scipy>=1.11.0
statsmodels>=0.14.0

# ── Machine Learning ───────────────────────────────────────
scikit-learn>=1.3.0
xgboost>=1.7.0
shap>=0.43.0
joblib>=1.3.0

# ── Notebooks ──────────────────────────────────────────────
jupyter>=1.0.0
ipykernel>=6.25.0
ipywidgets>=8.1.0

# ── API RESTful ────────────────────────────────────────────
flask>=2.3.0
flask-cors>=4.0.0

# ── Dashboard ──────────────────────────────────────────────
streamlit>=1.32.0

# ── HTTP / Integração ──────────────────────────────────────
requests>=2.31.0

# ── Chatbot ────────────────────────────────────────────────
openai>=1.0.0

# ── Utilitários ────────────────────────────────────────────
python-dotenv>=1.0.0
python-dateutil>=2.8.2

# ── Produção (opcional) ────────────────────────────────────
# gunicorn>=21.2.0
```

> **Nota sobre versões**: use `>=` em vez de `==` para maior compatibilidade entre ambientes diferentes. Fixar com `==` é recomendado apenas em produção.

---

## NB5 Unificado vs Notebooks Separados

### Análise Completa

| Critério | NB5 Unificado | NB1–NB4 Separados |
|---|---|---|
| **Reprodutibilidade** | ⚠️ Estado global compartilhado | ✅ Cada NB é isolado |
| **Depuração** | ❌ Difícil localizar erros | ✅ Erro isolado por fase |
| **Apresentação** | ✅ Um arquivo, um clique | ❌ 4 execuções na ordem certa |
| **Colaboração** | ❌ Conflitos de merge | ✅ Trabalho paralelo |
| **Legibilidade** | ⚠️ 71 células, pode confundir | ✅ Foco por fase |
| **Briefing/Avaliação** | ⚠️ Menos estruturado | ✅ Estrutura CRISP-DM clara |
| **Portfólio no GitHub** | ✅ Um arquivo para demonstrar | ✅ Estrutura profissional |
| **Manutenção** | ❌ Editar um NB afeta tudo | ✅ Edições independentes |

### Recomendação Final

> **Use notebooks separados (NB1–NB4) como padrão. Use o NB5 somente para apresentação.**

**Para desenvolvimento e entrega acadêmica**:
```
NB1 → NB2 → NB3 → NB4 (ordem obrigatória)
```
Motivo: alinha com a estrutura CRISP-DM que o briefing exige, e cada notebook tem entregáveis claros.

**Para demonstração rápida**:
```
PROJETO_COMPLETO_UNIFICADO.ipynb (NB5)
→ "Run All" e pronto
```
Motivo: avaliadores e recrutadores precisam de menos fricção.

### Boas Práticas para Ambas as Abordagens

```python
# Sempre começa com "Restart & Clear Output" antes de submeter
# Isso garante reprodutibilidade limpa

# Em notebooks separados: use Path para caminhos relativos
from pathlib import Path
BASE_DIR = Path(__file__).parent.parent  # ou Path.cwd()
CSV_PATH = BASE_DIR / "data" / "incidents_finance_filtered.csv"

# Em vez de hardcode frágil:
CSV_PATH = "/Users/seu_nome/projeto/incidents_finance_filtered.csv"  # ❌
```

---

## QUESTÃO 6 — Data Analysis Report Final

### É possível gerar um relatório consolidado? ✅ SIM

Após executar todos os notebooks, é possível gerar um relatório final que responde todas as questões do projeto. Abaixo está o modelo ideal:

---

### Modelo Ideal do Relatório Final

```markdown
# 📊 Data Analysis Report
## AI Incidents in Financial Services
**Data**: [DATA]  |  **Autor**: [NOME]  |  **PUC-SP 2026**

---

## 1. Sumário Executivo
- Total de incidentes analisados: X
- Período: AAAA–AAAA
- Hipóteses confirmadas: X de 4
- Melhor modelo: XGBoost (F1: X.XX)

## 2. Dados e Metodologia
- Fonte: AIID — CC BY-SA 4.0
- Pipeline: Coleta → Filtragem → Feature Engineering → Análise → ML → API → Dashboard
- Ferramentas: Python · SQLite · Flask · Streamlit · XGBoost · SHAP

## 3. Feature Engineering
- Variáveis derivadas criadas: 8
- Tabela com distribuição de cada variável
- Gráfico: painel 2×2 de distribuições

## 4. Testes de Hipóteses
### H1 — Concentração por Aplicação
- Teste: Qui-quadrado de aderência
- χ² = X.XX  |  p = X.XXXX
- Decisão: [Rejeita / Não rejeita] H₀
- Implicação: [interpretação]

### H2 — Viés por Segmento
### H3 — Severidade e Investigação
### H4 — Tendência Temporal

## 5. Modelos de Machine Learning
| Modelo | F1-Score | ROC-AUC | Aplicação |
|---|---|---|---|
| LR (baseline) | X.XX | X.XX | Referência |
| Random Forest | X.XX | X.XX | Ensemble |
| XGBoost ✅ | X.XX | X.XX | Produção |

- Feature Importance: tabela top 10
- Validação cruzada: F1 médio X.XX ± X.XX

## 6. API RESTful
- Endpoints: 9
- Testes automatizados: todos ✅
- Exemplo de predição: [JSON]

## 7. Dashboard
- Páginas: 7
- Integração com API: ✅ confirmada
- Dark/Light mode: ✅

## 8. Conclusões
- H1, H3 e H4 confirmadas com p < 0,05
- XGBoost como melhor modelo preditivo
- Recomendações para gestores de risco
- Limitações e trabalhos futuros

## 9. Referências
[lista de referências]
```

### Formato Recomendado

| Formato | Quando Usar | Como Gerar |
|---|---|---|
| **Markdown (.md)** | GitHub, portfólio, README | Escrever diretamente |
| **PDF** | Entrega acadêmica formal | `pandoc README.md -o relatorio.pdf` |
| **HTML** | Apresentação web | `jupyter nbconvert --to html NB5.ipynb` |
| **Slides** | Apresentação ao vivo | PowerPoint ou `jupyter nbconvert --to slides` |

### Gerar PDF do Relatório

```bash
# Instalar pandoc
# macOS: brew install pandoc
# Ubuntu: sudo apt-get install pandoc

# Gerar PDF do README
pandoc README.md -o relatorio_final.pdf \
  --pdf-engine=xelatex \
  --variable geometry:margin=2cm \
  --variable fontsize=11pt

# Ou exportar o NB5 como PDF
jupyter nbconvert notebooks/PROJETO_COMPLETO_UNIFICADO.ipynb \
  --to pdf \
  --output relatorio_notebook.pdf
```

---

## Validação Geral do Projeto

### Avaliação por Critério

| Critério | Score | Detalhes |
|---|---|---|
| **Reprodutibilidade** | 🟢 Alto | Fallbacks automáticos · dados demo · requirements.txt |
| **Documentação** | 🟢 Alto | README 862 linhas · guia passo a passo · resumo executivo |
| **Modularidade** | 🟢 Alto | 5 notebooks independentes · API separada do dashboard |
| **Qualidade de código** | 🟢 Alto | Type hints · docstrings · error handling · cache |
| **Análise estatística** | 🟢 Alto | 4 testes · α definido · interpretação gerencial |
| **ML** | 🟢 Alto | 3 algoritmos · SHAP · CV 5-fold · 2 modelos |
| **Visualização** | 🟢 Alto | Plotly interativo · dark mode · KPI cards |
| **Integração API↔Dashboard** | 🟢 Alto | Implementada · fallback · health check |
| **Escalabilidade** | 🟡 Médio | SQLite e Flask bons para protótipo |
| **Segurança** | 🟡 Médio | Sem autenticação (ok para acadêmico) |
| **Testes automatizados** | 🟡 Médio | Apenas API testada (falta unit tests do código Python) |

### Melhorias Claras e Acionáveis

**Prioridade ALTA** (para nível de produção):

```bash
# 1. Renomear o arquivo da API para evitar conflito
mv app.py app_api.py
# Atualizar todas as referências ao nome

# 2. Organizar pastas
mkdir -p notebooks data models dashboard docs
mv *.ipynb notebooks/
mv *.csv data/
mv dashboard/ dashboard/

# 3. Adicionar .gitignore
cat > .gitignore << EOF
.venv/
__pycache__/
*.pyc
.env
*.db          # não versionar o banco
models/*.pkl  # não versionar modelos grandes
data/*.csv    # não versionar dados brutos
EOF
```

**Prioridade MÉDIA** (para portfólio completo):

```python
# 1. Adicionar pytest para testes unitários
# tests/test_api.py
def test_stats_by_application():
    resp = client.get("/api/stats/by-application")
    assert resp.status_code == 200
    assert "statistics_by_application" in resp.json()

# 2. Adicionar variável de ambiente para API_BASE no dashboard
import os
API_BASE = os.getenv("API_BASE_URL", "http://localhost:5000")

# 3. Consumir API também nas páginas Explorer e Statistics
# (atualmente usam CSV diretamente)
```

**Prioridade BAIXA** (para produção real):

```yaml
# docker-compose.yml
services:
  api:
    build: .
    command: gunicorn app_api:app -w 4 -b 0.0.0.0:5000
    ports: ["5000:5000"]

  dashboard:
    build: .
    command: streamlit run dashboard/app.py --server.port 8501
    ports: ["8501:8501"]
    environment:
      - API_BASE_URL=http://api:5000
    depends_on: [api]
```

### Conclusão da Validação

**O projeto está pronto para portfólio profissional e apresentação acadêmica.**

Pontos fortes que se destacam para recrutadores:
1. Pipeline completo de ponta a ponta (dados → análise → ML → API → dashboard)
2. Integração real API↔Dashboard (não apenas fictícia)
3. Chatbot com OpenAI integrado
4. Dark mode funcional
5. Fallbacks automáticos (nunca quebra na demonstração)
6. Documentação profissional com 860+ linhas

Para atingir nível de produção: containerizar com Docker e adicionar autenticação na API.

---

*PUC-SP · Projeto Integrador · 2026*
