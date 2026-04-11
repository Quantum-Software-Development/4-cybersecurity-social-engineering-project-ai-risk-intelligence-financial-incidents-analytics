import pandas as pd
from dash import dcc, html, Input, Output
import dash
import plotly.express as px


dados_df=pd.read_excel("BASE01.CREDITO.xlsx")

app = dash.Dash(__name__)

# Layout do dashboard
app.layout = html.Div([
    dcc.Dropdown(
        id='region-dropdown',
        options=[{'label': region, 'value': region} for region in dados_df['regiao'].unique()],
        value='A'  # Valor inicial
    ),
    dcc.Graph(id='credito-vs-perda-graph')
])

# Callback para atualizar o gráfico com base na seleção de região
@app.callback(
    Output('credito-vs-perda-graph', 'figure'),  # Saída é o gráfico
    Input('region-dropdown', 'value')  # Entrada é o valor selecionado no dropdown
)
def update_graph(selected_region):
    # Filtra os dados pela região selecionada
    filtered_data = dados_df[dados_df['regiao'] == selected_region]

    # Cria um gráfico de dispersão de valor de crédito vs perda
    fig = px.scatter(filtered_data, x='valorcredito', y='perda',
                     title=f'Crédito vs Perda para Região {selected_region}')
    return fig

if __name__ == '__main__':
    app.run(debug=True)
