
# class_7 Cyber Dash

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.x-0f766e?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge" />
  </a>
  <a href="https://dash.plotly.com/">
    <img src="https://img.shields.io/badge/Dash-Plotly-0d9488?style=for-the-badge&logo=plotly&logoColor=white" alt="Dash Badge" />
  </a>
  <a href="https://streamlit.io/">
    <img src="https://img.shields.io/badge/Streamlit-App-14b8a6?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit Badge" />
  </a>
  <a href="https://plotly.com/python/">
    <img src="https://img.shields.io/badge/Plotly-Charts-0ea5a4?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly Badge" />
  </a>
  <a href="https://render.com/">
    <img src="https://img.shields.io/badge/Render-Deploy-134e4a?style=for-the-badge&logo=render&logoColor=white" alt="Render Badge" />
  </a>
  <a href="https://vercel.com/">
    <img src="https://img.shields.io/badge/Vercel-Deploy-111827?style=for-the-badge&logo=vercel&logoColor=white" alt="Vercel Badge" />
  </a>
  <a href="https://react.dev/">
    <img src="https://img.shields.io/badge/React-Future-0ea5a4?style=for-the-badge&logo=react&logoColor=white" alt="React Badge" />
  </a>
  <a href="https://nodejs.org/">
    <img src="https://img.shields.io/badge/Node.js-Future-166534?style=for-the-badge&logo=nodedotjs&logoColor=white" alt="Node Badge" />
  </a>
</p>

<p align="center">
  Interactive dashboards and analytical applications built with Dash, Plotly, Streamlit, Pandas, and future expansion to React + Node.js.
</p>

---

## Table of Contents

- [1. Project overview](#1-project-overview)
- [2. Repository structure](#2-repository-structure)
- [3. Technologies used](#3-technologies-used)
- [4. Setup and installation](#4-setup-and-installation)
- [5. Requirements checklist](#5-requirements-checklist)
- [6. Dataset organization](#6-dataset-organization)
- [7. Dash file guide](#7-dash-file-guide)
- [8. Streamlit file guide](#8-streamlit-file-guide)
- [9. Dash examples with explanations](#9-dash-examples-with-explanations)
- [10. Streamlit examples with explanations](#10-streamlit-examples-with-explanations)
- [11. Dash vs Streamlit](#11-dash-vs-streamlit)
- [12. Deployment guide](#12-deployment-guide)
- [13. React and Node.js expansion](#13-react-and-nodejs-expansion)
- [14. Future improvements](#14-future-improvements)

---

## 1. Project overview

This repository was created to study dashboard development with **Dash**, **Plotly**, and **Streamlit**. Dash apps are based on layouts and callbacks, while Streamlit apps follow a direct script-based flow using widgets such as tabs, sliders, select boxes, and metrics. [web:302][web:255]

The project progresses from introductory examples to more complete dashboard interfaces with filtering, data tables, chart updates, summary cards, and deployment preparation. It can also evolve into a larger full-stack project with React and Node.js. [web:302]

---

## 2. Repository structure

```bash
class_7_cyber_dash/
│
├── dash_apps/
│   ├── part_01_basic_dash_app.py
│   ├── part_02_dash_bar_chart.py
│   ├── part_03_basic_dash_callback.py
│   ├── part_04_dash_excel_table.py
│   ├── part_05_dash_dropdown_layout.py
│   ├── part_06_dash_region_bar_callback.py
│   ├── part_07_dash_region_line_callback.py
│   ├── part_08_dash_region_scatter_callback.py
│   ├── part_09_dash_multi_filter_dashboard.py
│   ├── part_10_dash_cards_and_summary.py
│   └── part_11_dash_darkmode_credit_dashboard.py
│
├── streamlit_apps/
│   ├── part_01_streamlit_hello.py
│   ├── part_02_streamlit_layout.py
│   ├── part_03_streamlit_tabs_filters.py
│   ├── part_04a_streamlit_filter_function.py
│   ├── part_04b_streamlit_dashboard_using_filter.py
│   └── part_05_streamlit_darkmode_credit_dashboard.py
│
├── data/
│   ├── BASE01.CREDITO.xlsx
│   ├── BASE_02_Simullacao.xlsx
│   ├── BASE01.CREDITO.csv
│   └── BASE_02_Simullacao.csv
│
├── react-app/
├── node-api/
├── requirements.txt
├── package.json
└── README.md
```


---

## 3. Technologies used

| Technology | Purpose | Notes |
| :-- | :-- | :-- |
| Python | Main language | Base for all current apps |
| Dash | Dashboard framework | Uses layout and callbacks [web:302] |
| Plotly | Interactive charts | Used inside Dash and Streamlit |
| Streamlit | Data apps | Fast dashboard construction [web:255] |
| Pandas | Data analysis | Reads, filters, and transforms data |
| OpenPyXL | Excel support | Needed for `.xlsx` files |
| CSV | Lightweight dataset format | Good for portability |
| Excel | Spreadsheet dataset format | Good for classroom datasets |
| Render | Deployment platform | Useful for Dash and Node apps |
| Vercel | Deployment platform | Useful for React and Python routing |
| React | Future frontend | Richer interface layer |
| Node.js | Future backend | APIs and services |


---

## 4. Setup and installation

A virtual environment keeps project dependencies isolated from the global Python installation.

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```


### macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If `requirements.txt` does not exist yet:

```bash
pip install dash streamlit pandas plotly openpyxl gunicorn
```


---

## 5. Requirements checklist

Python projects typically use `requirements.txt`, while Node.js projects use `package.json`. GitHub recommends relative links in README files because they work better for people browsing the repository or cloning it locally. [web:389][web:394]

### Python checklist

- [ ] Python installed
- [ ] Virtual environment created
- [ ] Virtual environment activated
- [ ] `requirements.txt` created
- [ ] Dash installed
- [ ] Streamlit installed
- [ ] Pandas installed
- [ ] Plotly installed
- [ ] OpenPyXL installed
- [ ] Gunicorn installed


### Suggested `requirements.txt`

```txt
dash
streamlit
pandas
plotly
openpyxl
gunicorn
```


### Node.js checklist

- [ ] Node.js installed
- [ ] npm installed
- [ ] `package.json` created
- [ ] `dependencies` configured
- [ ] `devDependencies` configured
- [ ] `scripts.start` configured
- [ ] `scripts.build` configured
- [ ] `scripts.dev` configured
- [ ] `.gitignore` contains `node_modules/`


### Example `package.json` for React

```json
{
  "name": "class-7-cyber-dash-react",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "start": "vite preview"
  },
  "dependencies": {
    "react": "^18.3.0",
    "react-dom": "^18.3.0"
  },
  "devDependencies": {
    "vite": "^5.4.0"
  }
}
```


### Example `package.json` for Node.js backend

```json
{
  "name": "class-7-cyber-dash-api",
  "version": "1.0.0",
  "type": "module",
  "main": "server.js",
  "scripts": {
    "start": "node server.js",
    "dev": "node server.js"
  },
  "dependencies": {
    "express": "^4.21.0",
    "cors": "^2.8.5"
  }
}
```


---

## 6. Dataset organization

There is no problem in storing the datasets in both **CSV** and **Excel** formats in the same repository. This is actually useful because CSV is lighter for some apps, while Excel preserves the classroom spreadsheet format. [web:389]


| File | Link | Format | Suggested use |
| :-- | :-- | :-- | :-- |
| `BASE01.CREDITO.xlsx` | 📎 [BASE01.CREDITO.xlsx](./data/BASE01.CREDITO.xlsx) | Excel | Original classroom dataset |
| `BASE_02_Simullacao.xlsx` | 📎 [BASE_02_Simullacao.xlsx](./data/BASE_02_Simullacao.xlsx) | Excel | Alternative simulation dataset |
| `BASE01.CREDITO.csv` | 📎 [BASE01.CREDITO.csv](./data/BASE01.CREDITO.csv) | CSV | Lighter and easier for web use |
| `BASE_02_Simullacao.csv` | 📎 [BASE_02_Simullacao.csv](./data/BASE_02_Simullacao.csv) | CSV | Lighter alternative dataset |

### Read Excel with Pandas

```python
import pandas as pd
df = pd.read_excel("data/BASE01.CREDITO.xlsx")
```


### Read CSV with Pandas

```python
import pandas as pd
df = pd.read_csv("data/BASE01.CREDITO.csv")
```


---

## 7. Dash file guide

Dash callbacks are functions executed when component inputs change, and they are the core interaction model in Dash apps. [web:302]


| Order | File | Link | Purpose |
| :-- | :-- | :-- | :-- |
| 1 | `part_01_basic_dash_app.py` | 📎 [part_01_basic_dash_app.py](./dash_apps/part_01_basic_dash_app.py) | First static Dash app |
| 2 | `part_02_dash_bar_chart.py` | 📎 [part_02_dash_bar_chart.py](./dash_apps/part_02_dash_bar_chart.py) | Basic bar chart |
| 3 | `part_03_basic_dash_callback.py` | 📎 [part_03_basic_dash_callback.py](./dash_apps/part_03_basic_dash_callback.py) | First callback |
| 4 | `part_04_dash_excel_table.py` | 📎 [part_04_dash_excel_table.py](./dash_apps/part_04_dash_excel_table.py) | Reads Excel and shows table |
| 5 | `part_05_dash_dropdown_layout.py` | 📎 [part_05_dash_dropdown_layout.py](./dash_apps/part_05_dash_dropdown_layout.py) | Dropdown layout |
| 6 | `part_06_dash_region_bar_callback.py` | 📎 [part_06_dash_region_bar_callback.py](./dash_apps/part_06_dash_region_bar_callback.py) | Dropdown updates bar chart |
| 7 | `part_07_dash_region_line_callback.py` | 📎 [part_07_dash_region_line_callback.py](./dash_apps/part_07_dash_region_line_callback.py) | Dropdown updates line chart |
| 8 | `part_08_dash_region_scatter_callback.py` | 📎 [part_08_dash_region_scatter_callback.py](./dash_apps/part_08_dash_region_scatter_callback.py) | Dropdown updates scatter plot |
| 9 | `part_09_dash_multi_filter_dashboard.py` | 📎 [part_09_dash_multi_filter_dashboard.py](./dash_apps/part_09_dash_multi_filter_dashboard.py) | Multiple filters |
| 10 | `part_10_dash_cards_and_summary.py` | 📎 [part_10_dash_cards_and_summary.py](./dash_apps/part_10_dash_cards_and_summary.py) | KPI cards |
| 11 | `part_11_dash_darkmode_credit_dashboard.py` | 📎 [part_11_dash_darkmode_credit_dashboard.py](./dash_apps/part_11_dash_darkmode_credit_dashboard.py) | Complete dark dashboard |


---

## 8. Streamlit file guide

Streamlit tabs are containers that help organize related content into separate views inside the app. [web:255][web:301]


| Order | File | Link | Purpose |
| :-- | :-- | :-- | :-- |
| 1 | `part_01_streamlit_hello.py` | 📎 [part_01_streamlit_hello.py](./streamlit_apps/part_01_streamlit_hello.py) | First Streamlit app |
| 2 | `part_02_streamlit_layout.py` | 📎 [part_02_streamlit_layout.py](./streamlit_apps/part_02_streamlit_layout.py) | Layout with tabs and columns |
| 3 | `part_03_streamlit_tabs_filters.py` | 📎 [part_03_streamlit_tabs_filters.py](./streamlit_apps/part_03_streamlit_tabs_filters.py) | Widget-based filtering |
| 4 | `part_04a_streamlit_filter_function.py` | 📎 [part_04a_streamlit_filter_function.py](./streamlit_apps/part_04a_streamlit_filter_function.py) | Reusable filter function |
| 5 | `part_04b_streamlit_dashboard_using_filter.py` | 📎 [part_04b_streamlit_dashboard_using_filter.py](./streamlit_apps/part_04b_streamlit_dashboard_using_filter.py) | Dashboard using function |
| 6 | `part_05_streamlit_darkmode_credit_dashboard.py` | 📎 [part_05_streamlit_darkmode_credit_dashboard.py](./streamlit_apps/part_05_streamlit_darkmode_credit_dashboard.py) | Dark dashboard |


---

## 9. Dash examples with explanations

### 9.1. 📎 [part_01_basic_dash_app.py](./dash_apps/part_01_basic_dash_app.py)

This first file shows the minimum Dash structure.

```python
import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("My First Dash App"),
    html.P("Creating a basic layout with Dash")
])

if __name__ == "__main__":
    app.run_server(debug=True)
```

| Code part | Explanation |
| :-- | :-- |
| `dash.Dash(__name__)` | Creates the Dash application |
| `html.Div([...])` | Main container |
| `html.H1()` | Main title |
| `html.P()` | Descriptive paragraph |
| `app.run_server()` | Starts the local server |

### 9.2. 📎 [part_02_dash_bar_chart.py](./dash_apps/part_02_dash_bar_chart.py)

This file introduces a chart inside the Dash layout.

```python
import dash
from dash import html, dcc

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Example Layout with Chart"),
    dcc.Graph(
        id="example-graph",
        figure={
            "data": [
                {"x": , "y": , "type": "bar", "name": "SF"}
            ],
            "layout": {"title": "Simple Chart"}
        }
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
```

| Code part | Explanation |
| :-- | :-- |
| `dcc.Graph()` | Chart component |
| `figure` | Graph structure |
| `"type": "bar"` | Bar chart definition |
| `"layout"` | Visual configuration |

### 9.3. 📎 [part_03_basic_dash_callback.py](./dash_apps/part_03_basic_dash_callback.py)

Callbacks update outputs when inputs change. [web:302]

```python
import dash
from dash import html, dcc, Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Programming the Callback"),
    dcc.Input(id="input-text", value="Type something...", type="text"),
    html.Div(id="output-text")
])

@app.callback(
    Output("output-text", "children"),
    Input("input-text", "value")
)
def update_output(value):
    return f"You wrote: {value}"

if __name__ == "__main__":
    app.run_server(debug=True)
```

| Code part | Explanation |
| :-- | :-- |
| `Input(...)` | Watches a component property |
| `Output(...)` | Target to update |
| `@app.callback` | Connects input and output |
| `update_output()` | Logic executed after change |

### 9.4. 📎 [part_04_dash_excel_table.py](./dash_apps/part_04_dash_excel_table.py)

This file reads Excel data and displays it in a table.

```python
import pandas as pd
import dash
from dash import html, dash_table

dados_df = pd.read_excel("data/BASE01.CREDITO.xlsx")

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H1("Credit Dashboard"),
        html.P("Credit data analysis of customers")
    ], style={"textAlign": "center", "padding": "20px"}),

    html.Div([
        html.H3("Detailed Data"),
        dash_table.DataTable(
            id="table",
            columns=[{"name": i, "id": i} for i in dados_df.columns],
            data=dados_df.head(20).to_dict("records")
        )
    ], style={"padding": "20px"})
])

if __name__ == "__main__":
    app.run_server(debug=True)
```

| Code part | Explanation |
| :-- | :-- |
| `pd.read_excel()` | Reads Excel into DataFrame |
| `dash_table.DataTable()` | Interactive table |
| `columns=[...]` | Defines the table columns |
| `to_dict("records")` | Converts rows into Dash format |

### 9.5. 📎 [part_05_dash_dropdown_layout.py](./dash_apps/part_05_dash_dropdown_layout.py)

This file prepares the interface for region selection.

```python
import pandas as pd
import dash
from dash import html, dcc

dados_df = pd.read_excel("data/BASE01.CREDITO.xlsx")

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Credit Dashboard"),
    dcc.Dropdown(
        id="regiao-dropdown",
        options=[{"label": regiao, "value": regiao} for regiao in dados_df["regiao"].unique()],
        value=dados_df["regiao"].unique()
    ),
    dcc.Graph(id="idade-vs-perda-graph")
])

if __name__ == "__main__":
    app.run_server(debug=True)
```


### 9.6. 📎 [part_06_dash_region_bar_callback.py](./dash_apps/part_06_dash_region_bar_callback.py)

This file connects the dropdown to a bar chart. [web:302]

```python
import pandas as pd
import dash
import plotly.express as px
from dash import html, dcc, Input, Output

dados_df = pd.read_excel("data/BASE01.CREDITO.xlsx")

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id="regiao-dropdown",
        options=[{"label": regiao, "value": regiao} for regiao in dados_df["regiao"].unique()],
        value=dados_df["regiao"].unique()
    ),
    dcc.Graph(id="idade-vs-perda-graph")
])

@app.callback(
    Output("idade-vs-perda-graph", "figure"),
    Input("regiao-dropdown", "value")
)
def update_graph(selected_region):
    filtered_data = dados_df[dados_df["regiao"] == selected_region]
    fig = px.bar(filtered_data, x="idade", y="perda", title=f"Age vs Loss for Region {selected_region}")
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
```


### 9.7. 📎 [part_07_dash_region_line_callback.py](./dash_apps/part_07_dash_region_line_callback.py)

This version keeps the callback logic but uses a line chart.

```python
import pandas as pd
import dash
import plotly.express as px
from dash import html, dcc, Input, Output

df = pd.read_excel("data/BASE01.CREDITO.xlsx")

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id="region-dropdown",
        options=[{"label": r, "value": r} for r in df["regiao"].unique()],
        value=df["regiao"].unique()
    ),
    dcc.Graph(id="line-graph")
])

@app.callback(
    Output("line-graph", "figure"),
    Input("region-dropdown", "value")
)
def update_line_chart(selected_region):
    filtered = df[df["regiao"] == selected_region]
    fig = px.line(filtered, x="idade", y="perda", title=f"Loss trend by age - {selected_region}")
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
```


### 9.8. 📎 [part_08_dash_region_scatter_callback.py](./dash_apps/part_08_dash_region_scatter_callback.py)

This file compares variables with a scatter plot.

```python
import pandas as pd
import dash
import plotly.express as px
from dash import html, dcc, Input, Output

dados_df = pd.read_excel("data/BASE01.CREDITO.xlsx")

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id="region-dropdown",
        options=[{"label": region, "value": region} for region in dados_df["regiao"].unique()],
        value=dados_df["regiao"].unique()
    ),
    dcc.Graph(id="credito-vs-perda-graph")
])

@app.callback(
    Output("credito-vs-perda-graph", "figure"),
    Input("region-dropdown", "value")
)
def update_graph(selected_region):
    filtered_data = dados_df[dados_df["regiao"] == selected_region]
    fig = px.scatter(
        filtered_data,
        x="valorcredito",
        y="perda",
        title=f"Credit vs Loss for Region {selected_region}"
    )
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
```


### 9.9. 📎 [part_09_dash_multi_filter_dashboard.py](./dash_apps/part_09_dash_multi_filter_dashboard.py)

This version combines multiple filters in the same dashboard.

```python
import pandas as pd
import dash
import plotly.express as px
from dash import html, dcc, Input, Output

df = pd.read_excel("data/BASE01.CREDITO.xlsx")

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id="region-dropdown",
        options=[{"label": r, "value": r} for r in sorted(df["regiao"].unique())],
        value=sorted(df["regiao"].unique())
    ),
    dcc.Dropdown(
        id="gender-dropdown",
        options=[{"label": s, "value": s} for s in sorted(df["sexo"].unique())],
        value=sorted(df["sexo"].unique())
    ),
    dcc.Graph(id="multi-filter-graph")
])

@app.callback(
    Output("multi-filter-graph", "figure"),
    Input("region-dropdown", "value"),
    Input("gender-dropdown", "value")
)
def update_graph(region, gender):
    filtered = df[(df["regiao"] == region) & (df["sexo"] == gender)]
    fig = px.bar(filtered, x="idade", y="valorcredito", title=f"Credit by Age - {region} / {gender}")
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
```


### 9.10. 📎 [part_10_dash_cards_and_summary.py](./dash_apps/part_10_dash_cards_and_summary.py)

This file creates KPI cards for quick summary indicators.

```python
import pandas as pd
import dash
from dash import html

df = pd.read_excel("data/BASE01.CREDITO.xlsx")

total_clients = len(df)
avg_credit = df["valorcredito"].mean()
avg_loss = df["perda"].mean()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Credit Dashboard Summary"),
    html.Div([
        html.Div([html.H3("Clients"), html.P(f"{total_clients}")], style={"padding": "20px", "border": "1px solid #ccc"}),
        html.Div([html.H3("Average Credit"), html.P(f"{avg_credit:.2f}")], style={"padding": "20px", "border": "1px solid #ccc"}),
        html.Div([html.H3("Average Loss"), html.P(f"{avg_loss:.2f}")], style={"padding": "20px", "border": "1px solid #ccc"})
    ], style={"display": "grid", "gridTemplateColumns": "repeat(3, 1fr)", "gap": "16px"})
])

if __name__ == "__main__":
    app.run_server(debug=True)
```


### 9.11. 📎 [part_11_dash_darkmode_credit_dashboard.py](./dash_apps/part_11_dash_darkmode_credit_dashboard.py)

This is the most complete Dash example in the project.

```python
import pandas as pd
import dash
import plotly.express as px
from dash import html, dcc, Input, Output

df = pd.read_excel("data/BASE01.CREDITO.xlsx")

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("Cyber Credit Dashboard", style={"color": "#38d9d9"}),
    dcc.Dropdown(
        id="region-dropdown",
        options=[{"label": r, "value": r} for r in sorted(df["regiao"].unique())],
        value=sorted(df["regiao"].unique())
    ),
    dcc.Graph(id="dark-graph")
], style={"backgroundColor": "#07141d", "padding": "20px", "minHeight": "100vh"})

@app.callback(
    Output("dark-graph", "figure"),
    Input("region-dropdown", "value")
)
def update_graph(region):
    filtered = df[df["regiao"] == region]
    fig = px.scatter(filtered, x="valorcredito", y="perda", color="sexo", title=f"Credit vs Loss - {region}")
    fig.update_layout(template="plotly_dark")
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
```


---

## 10. Streamlit examples with explanations

### 10.1. 📎 [part_01_streamlit_hello.py](./streamlit_apps/part_01_streamlit_hello.py)

This first file demonstrates the simplest Streamlit structure.

```python
import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello, Streamlit")
st.write("This is the first Streamlit example.")

data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

st.line_chart(data)
```


### 10.2. 📎 [part_02_streamlit_layout.py](./streamlit_apps/part_02_streamlit_layout.py)

This file demonstrates page layout with button, tabs, and columns.

```python
import streamlit as st

st.set_page_config(layout="wide")

st.title("Layout Demo")

if st.button("Click me"):
    st.success("The button worked!")

tab1, tab2 = st.tabs(["Overview", "Details"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.write("Left side")
    with col2:
        st.write("Right side")

with tab2:
    st.write("Detailed information goes here.")
```


### 10.3. 📎 [part_03_streamlit_tabs_filters.py](./streamlit_apps/part_03_streamlit_tabs_filters.py)

This example filters a dataset through widgets.

```python
import streamlit as st
import pandas as pd

df = pd.read_csv("data/BASE01.CREDITO.csv")

st.title("Credit Filter App")

region = st.selectbox("Region", sorted(df["regiao"].unique()))
gender = st.selectbox("Gender", sorted(df["sexo"].unique()))
age = st.slider("Age", int(df["idade"].min()), int(df["idade"].max()), int(df["idade"].min()))

filtered = df[
    (df["regiao"] == region) &
    (df["sexo"] == gender) &
    (df["idade"] >= age)
]

st.dataframe(filtered)
```


### 10.4. 📎 [part_04a_streamlit_filter_function.py](./streamlit_apps/part_04a_streamlit_filter_function.py)

This file extracts filter logic into a reusable function.

```python
import pandas as pd

def filtrar_dados(df, regioes=None, sexo=None, idade_min=None, idade_max=None):
    filtered = df.copy()

    if regioes:
        filtered = filtered[filtered["regiao"].isin(regioes)]

    if sexo and sexo != "All":
        filtered = filtered[filtered["sexo"] == sexo]

    if idade_min is not None:
        filtered = filtered[filtered["idade"] >= idade_min]

    if idade_max is not None:
        filtered = filtered[filtered["idade"] <= idade_max]

    return filtered
```


### 10.5. 📎 [part_04b_streamlit_dashboard_using_filter.py](./streamlit_apps/part_04b_streamlit_dashboard_using_filter.py)

This dashboard uses the reusable filter function and Plotly charting.

```python
import streamlit as st
import pandas as pd
import plotly.express as px
from part_04a_streamlit_filter_function import filtrar_dados

st.set_page_config(layout="wide")

df_base1 = pd.read_csv("data/BASE01.CREDITO.csv")
df_base2 = pd.read_csv("data/BASE_02_Simullacao.csv")

st.title("Streamlit Credit Dashboard")

dataset_name = st.sidebar.selectbox("Dataset", ["BASE01", "BASE02"])

df = df_base1 if dataset_name == "BASE01" else df_base2

regioes = st.sidebar.multiselect(
    "Region",
    sorted(df["regiao"].unique()),
    default=list(sorted(df["regiao"].unique()))
)
sexo = st.sidebar.selectbox(
    "Gender",
    ["All"] + list(sorted(df["sexo"].unique()))
)
idade_range = st.sidebar.slider(
    "Age range",
    int(df["idade"].min()),
    int(df["idade"].max()),
    (int(df["idade"].min()), int(df["idade"].max()))
)

filtered = filtrar_dados(
    df,
    regioes=regioes,
    sexo=sexo,
    idade_min=idade_range,
    idade_max=idade_range
)

st.dataframe(filtered)

fig = px.scatter(filtered, x="valorcredito", y="perda", color="sexo", title="Credit vs Loss")
st.plotly_chart(fig, use_container_width=True)
```


### 10.6. 📎 [part_05_streamlit_darkmode_credit_dashboard.py](./streamlit_apps/part_05_streamlit_darkmode_credit_dashboard.py)

This final Streamlit example adds a dark visual style.

```python
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.markdown("""
    <style>
        .stApp {
            background-color: #07141d;
            color: white;
        }
        h1, h2, h3 {
            color: #38d9d9;
        }
    </style>
""", unsafe_allow_html=True)

df = pd.read_csv("data/BASE01.CREDITO.csv")

st.title("Cyber Streamlit Dashboard")

region = st.sidebar.selectbox("Region", sorted(df["regiao"].unique()))
gender = st.sidebar.selectbox("Gender", ["All"] + list(sorted(df["sexo"].unique())))

filtered = df.copy()
if gender != "All":
    filtered = filtered[filtered["sexo"] == gender]
filtered = filtered[filtered["regiao"] == region]

st.dataframe(filtered)

fig = px.scatter(filtered, x="valorcredito", y="perda", color="sexo", title=f"Credit vs Loss - {region}")
st.plotly_chart(fig, use_container_width=True)
```


---

## 11. Dash vs Streamlit

| Feature | Dash | Streamlit |
| :-- | :-- | :-- |
| Architecture | Layout + callbacks [web:302] | Script-based interface [web:255] |
| Best use | Structured analytical apps | Fast prototypes and dashboards |
| Interactivity | Explicit callback system [web:302] | Automatic widget reruns |
| Tables | Dash DataTable | `st.dataframe()` |
| Deployment | Render, Vercel | Streamlit Cloud, Render |
| Learning curve | More advanced | Easier for beginners |


---

## 12. Deployment guide

### 12.1. Streamlit Community Cloud

Streamlit Community Cloud deploys apps directly from GitHub repositories. [web:255]

```bash
git add .
git commit -m "Prepare deployment"
git push origin main
```

Then choose the entry file, for example:

```bash
streamlit_apps/part_05_streamlit_darkmode_credit_dashboard.py
```


### 12.2. Dash on Render

Render is a good deployment option for Dash apps running with Gunicorn.

```python
import dash
from dash import html

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("Dash app on Render")
])

if __name__ == "__main__":
    app.run_server(debug=True)
```

Build command:

```bash
pip install -r requirements.txt
```

Start command:

```bash
gunicorn dash_apps.part_11_dash_darkmode_credit_dashboard:server
```


### 12.3. React on Vercel

Vercel is commonly used for React deployment.

```bash
npm install -g vercel
vercel
```


### 12.4. Python on Vercel

A Python entrypoint can be exposed through `api/index.py`.

`api/index.py`

```python
import dash
from dash import html

dash_app = dash.Dash(__name__)
server = dash_app.server
app = server

dash_app.layout = html.Div([
    html.H1("Dash app running on Vercel")
])
```

`vercel.json`

```json
{
  "routes": [
    {
      "src": "/(.*)",
      "dest": "api/index.py"
    }
  ]
}
```


---

## 13. React and Node.js expansion

This repository can later become a full-stack data application.


| Layer | Technology | Purpose |
| :-- | :-- | :-- |
| Frontend | React | Interactive user interface |
| Backend | Node.js + Express | API services |
| Data apps | Dash / Streamlit | Analytics dashboards |
| Data source | CSV / Excel / Database | Structured data |


---

## 14. Future improvements

- Add authentication
- Add file upload support
- Add AI-generated insights
- Add better responsive layout
- Add PDF and Excel exports
- Add React frontend
- Add Node.js API
- Add database integration

```

## Ajustes finais que ficaram corretos

- Os links agora mostram **apenas o nome do arquivo**, como `part_01_streamlit_hello.py`, mas continuam apontando para o caminho certo no repositório. Isso segue o comportamento esperado de links relativos em README do GitHub.[^3][^4]
- CSV e Excel podem coexistir no mesmo projeto sem problema, desde que você mantenha nomes consistentes e use a função certa do Pandas em cada app.[^2]
- A parte de Dash ficou coerente com a lógica de **callbacks**, que são disparados quando as propriedades de entrada mudam.[^1]

Quer que eu transforme isso agora em um **arquivo `.md` pronto para download**?
<span style="display:none">[^10][^5][^6][^7][^8][^9]</span>

<div align="center">⁂</div>

[^1]: https://dash.plotly.com/basic-callbacks
[^2]: https://docs.streamlit.io/develop/api-reference/layout/st.tabs
[^3]: https://github.blog/news-insights/product-news/relative-links-in-markup-files/
[^4]: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
[^5]: https://dash.plotly.com/advanced-callbacks
[^6]: https://dash.plotly.com/background-callbacks
[^7]: https://dash-resources.com/tutorial-dash-callbacks-schemas-examples/
[^8]: https://spl.hevs.io/spl-docs/tools/plotly-dash/guidelines.html
[^9]: https://django-plotly-dash.readthedocs.io/en/latest/extended_callbacks.html
[^10]: https://evidence.dev/learn/streamlit-tabs```

