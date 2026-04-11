import pandas as pd
from dash import dcc, html, Input, Output
import dash
import plotly.express as px


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

# Callback para atualizar o gráfico com base na seleção de região
@app.callback(
    Output('idade-vs-perda-graph', 'figure'),  # Saída é o gráfico
    Input('regiao-dropdown', 'value')  # Entrada é o valor selecionado no dropdown
)
def update_graph(selected_region):
    # Filtra os dados pela região selecionada
    filtered_data = dados_df[dados_df['regiao'] == selected_region]
    # Cria um gráfico de barra de sexo vs perda
    fig = px.bar(filtered_data, x='idade', y='perda',
                     title=f'Idade vs Perda para Região {selected_region}')
    return fig


if __name__ == '__main__':
    app.run(debug=True)