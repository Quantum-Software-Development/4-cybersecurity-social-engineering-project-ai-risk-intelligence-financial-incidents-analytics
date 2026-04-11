import pandas as pd
from dash import dcc, html, Input, Output
import dash
import plotly.express as px


dados_df=pd.read_excel("BASE01.CREDITO.xlsx")

app = dash.Dash(__name__)

app.layout = html.Div([
    # Cabeçalho
    html.Div([
        html.H1("Dashboard de Crédito - COM 2 FILTROS"),
        html.P("Análise de dados de crédito dos clientes")
    ], style={'text-align': 'center', 'padding': '20px', 'backgroundColor': '#f8f9fa'}),

    # Filtros e Controles
    html.Div([
        html.Label("Selecione a Região:"),
        dcc.Dropdown(
            id='regiao-dropdown',
            options=[{'label': regiao, 'value': regiao} for regiao in dados_df['regiao'].unique()],
            value='A'  # Valor inicial
        ),
        html.Label("Idade"),
        dcc.RangeSlider(
            id='age-slider',
            min=dados_df['idade'].min(),
            max=dados_df['idade'].max(),
            value=[dados_df['idade'].min(), dados_df['idade'].max()],
            marks={i: f'{i}' for i in range(dados_df['idade'].min(), dados_df['idade'].max(), 5)}
        )
    ], style={'padding': '20px', 'backgroundColor': '#e9ecef'}),

    # Gráficos
    html.Div([
        html.Div([
            dcc.Graph(id='idade-vs-perda-graph'),
        ], style={'width': '80%', 'display': 'inline-block', 'padding': '20px'})
    ])
])


# Callback para atualizar o gráfico com base na seleção de região
@app.callback(
    Output('idade-vs-perda-graph', 'figure'),  # Saída é o gráfico
    [ Input('regiao-dropdown', 'value'),  # Entrada é o valor selecionado no dropdown
      Input('age-slider', 'value')]
      )


def update_graph(selected_region,range):
    # Filtra os dados pela região selecionada
    filtered_data = dados_df[dados_df['regiao'] == selected_region]
    filtered_data = filtered_data[(filtered_data['idade'] >= range[0]) & (filtered_data['idade'] <= range[1])]
    # Cria um gráfico de barra de sexo vs perda
    fig = px.scatter(filtered_data, x='idade', y='perda',
                     title=f'Idade vs Perda para Região {selected_region}')
    return fig



if __name__ == '__main__':
    app.run(debug=True)
