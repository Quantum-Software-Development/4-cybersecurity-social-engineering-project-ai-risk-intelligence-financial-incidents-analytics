# ⚡ Guia Rápido de Início (Quick Start)

## 🚀 Como começar em 5 minutos

### 1. Preparação do Ambiente

```bash
# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou: venv\Scripts\activate  # Windows

# Instalar dependências
pip install -r requirements.txt
```

### 2. Preparar os Dados

**Opção A - Usar dados fornecidos**:
- Arquivos já incluídos: `incidents.csv` e `incidents_finance_filtered.csv`
- Pule para o passo 3

**Opção B - Baixar dados atualizados**:
```python
import kagglehub
path = kagglehub.dataset_download("konradb/ai-incident-database")
print("Path to dataset files:", path)
```

### 3. Executar Notebooks na Ordem

#### 📓 Notebook 1: Exploração e Preparação
```bash
jupyter notebook notebook_1_exploracao_preparacao.ipynb
```

**O que faz**:
- Carrega dataset AIID
- Filtra incidentes do setor financeiro
- Cria variáveis derivadas
- Gera banco SQLite

**Saídas**:
- `incidents_finance_filtered.csv`
- `ai_finance_incidents.db`

**Tempo estimado**: ~5-10 minutos

---

#### 📊 Notebook 2: Análise Estatística
```bash
jupyter notebook notebook_2_analise_estatistica.ipynb
```

**O que faz**:
- Estatísticas descritivas
- 4 testes de hipóteses
- Visualizações

**Pré-requisito**: Notebook 1 completo

**Tempo estimado**: ~3-5 minutos

---

#### 🤖 Notebook 3: Modelagem ML
```bash
jupyter notebook notebook_3_modelagem_ml.ipynb
```

**O que faz**:
- Treina 2 modelos ML
- Avalia performance
- Salva modelos

**Saídas**:
- `models/severity_classifier.pkl`
- `models/investigation_classifier.pkl`

**Pré-requisito**: Notebook 1 completo

**Tempo estimado**: ~10-15 minutos (inclui treinamento)

---

#### 🚀 Notebook 4: API RESTful
```bash
jupyter notebook notebook_4_api_restful.ipynb
```

**O que faz**:
- Define 9 endpoints
- Testa API
- Gera documentação

**Pré-requisitos**: Notebooks 1 e 3 completos

**Tempo estimado**: ~5 minutos

---

### 4. Executar a API

```bash
# Copiar código da API para arquivo standalone
# (ou usar o código do Notebook 4)

python app.py
```

**Testar**:
```bash
# Endpoint raiz
curl http://localhost:5000/

# Listar incidentes
curl http://localhost:5000/api/incidents?limit=5

# Estatísticas
curl http://localhost:5000/api/stats/by-application
```

---

## 🎯 Atalhos para Casos de Uso Comuns

### Caso 1: "Só quero ver os resultados"
1. Execute Notebook 1 (gera dados)
2. Execute Notebook 2 (análises e gráficos)
3. Leia o `RESUMO_EXECUTIVO.md`

### Caso 2: "Quero usar os modelos ML"
1. Execute Notebook 1 (gera dados)
2. Execute Notebook 3 (treina modelos)
3. Use modelos salvos em `models/`

```python
import joblib
modelo = joblib.load('models/severity_classifier.pkl')
# Fazer predições...
```

### Caso 3: "Quero a API funcionando"
1. Execute Notebooks 1 e 3 (dados + modelos)
2. Execute Notebook 4 (define API)
3. Copie código para `app.py` e execute
4. Acesse http://localhost:5000

### Caso 4: "Quero customizar as análises"
1. Execute Notebook 1 (dados base)
2. Crie seu próprio notebook
3. Use `incidents_finance_filtered.csv` e `ai_finance_incidents.db`

---

## 🐛 Resolução de Problemas Comuns

### Problema: ModuleNotFoundError

**Solução**:
```bash
pip install -r requirements.txt
```

### Problema: "Arquivo não encontrado"

**Solução**: 
- Verifique se está no diretório correto
- Execute notebooks na ordem correta
- Verifique se Notebook 1 foi completado

### Problema: Modelos ML não carregam

**Solução**:
1. Execute Notebook 3 completamente
2. Verifique se pasta `models/` existe
3. Confirme arquivos `.pkl` foram criados

### Problema: API retorna erro 500

**Solução**:
1. Verifique se banco `ai_finance_incidents.db` existe
2. Verifique se modelos foram salvos
3. Veja logs no terminal para detalhes

---

## 📁 Estrutura de Arquivos Esperada

Após executar todos os notebooks:

```
projeto/
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
├── RESUMO_EXECUTIVO.md
└── README_API.md
```

---

## ⏱️ Tempo Total Estimado

- **Mínimo** (apenas resultados): ~15-20 minutos
- **Completo** (tudo incluindo API): ~30-40 minutos

---

## 💡 Dicas Pro

1. **Use Google Colab se não tiver ambiente local**:
   - Upload dos notebooks
   - Upload de `incidents.csv`
   - Execute células sequencialmente

2. **Salve trabalho incrementalmente**:
   - Cada notebook gera arquivos intermediários
   - Não precisa refazer tudo se algo der errado

3. **Customize para seu caso**:
   - Todos os notebooks são modularizados
   - Fácil adaptar filtros, features, modelos

4. **Performance**:
   - Notebooks 1-2: Rápidos
   - Notebook 3: Mais demorado (treinamento ML)
   - Notebook 4: Rápido (apenas definição)

---

## 📞 Precisa de Ajuda?

- Verifique `README.md` para documentação completa
- Verifique `RESUMO_EXECUTIVO.md` para entender resultados
- Verifique `README_API.md` para documentação da API
- Revise células de texto nos notebooks para explicações

---

## ✅ Checklist de Validação

Após executar tudo, confirme:

- [ ] `incidents_finance_filtered.csv` foi criado
- [ ] `ai_finance_incidents.db` existe e tem 3 tabelas
- [ ] Pasta `models/` tem 4 arquivos `.pkl`
- [ ] Notebook 2 mostrou 4 testes de hipóteses
- [ ] Notebook 3 mostrou métricas de modelos (F1-Score, etc.)
- [ ] API responde em http://localhost:5000

Se todos ✅, parabéns! Projeto completo e funcional! 🎉

---

**Versão**: 1.0  
**Última atualização**: Abril 2026
