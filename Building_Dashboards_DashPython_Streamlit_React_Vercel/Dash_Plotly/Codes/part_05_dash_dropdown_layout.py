from dash import dcc, html, Input, Output
import dash
import plotly.express as px
import pandas as pd

dados_df=pd.read_excel("BASE01.CREDITO.xlsx")

app = dash.Dash(__name__)

app.layout = html.Div([
    # Cabeçalho
    html.Div([
        html.H1("Dashboard de Crédito"),
        html.P("Análise de dados de crédito dos clientes por REGIÃO")
    ], style={'text-align': 'center', 'padding': '20px', 'backgroundColor': '#ffffff'}),
     html.Div([
    dcc.Dropdown(
        id='regiao-dropdown',
        options=[{'label': regiao, 'value': regiao} for regiao in dados_df['regiao'].unique()],
        value='A'  # Valor inicial
    ),
    dcc.Graph(id='idade-vs-perda-graph')
      ])
])


if __name__ == '__main__':
    app.run(debug=True)
