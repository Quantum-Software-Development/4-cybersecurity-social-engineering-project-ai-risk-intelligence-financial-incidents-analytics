import pandas as pd
from dash import dcc, html, Input, Output
import dash
import plotly.express as px


dados_df=pd.read_excel("BASE01.CREDITO.xlsx")

suppress_callback_exceptions=True
app = dash.Dash(__name__)


# Layout principal
app.layout = html.Div([
    html.H1("Dashboard com Abas"),
    
    # Componente de Abas
    dcc.Tabs(id="tabs-exemplo", value='aba-1', children=[
        dcc.Tab(label='ABA 1', value='aba-1'),
        dcc.Tab(label='ABA 2', value='aba-2'),
    ]),
    
    # Div onde o conteúdo das abas será renderizado
    html.Div(id='conteudo-aba')
])
# Callback para gerenciar a troca de abas
@app.callback(Output('conteudo-aba', 'children'),
              Input('tabs-exemplo', 'value'))
def render_content(tab):
    if tab == 'aba-1':
        return ABA1()
    elif tab == 'aba-2':
        return ABA2()

def ABA1():
    # Layout do cockpit
    return html.Div([
    #html.H1("4 Gráficos com Filtros Independente"),
    # Gráfico 1: Valor de Crédito vs Perda com filtro por Região
    html.Div([
             dcc.Dropdown(
            id='regiao-dropdown',
            options=[{'label': regiao, 'value': regiao} for regiao in dados_df['regiao'].unique()],
            value='A',
            placeholder="Selecione a Região"
        ),
        dcc.Graph(id='credito-vs-perda-graph')
    ], style={'width': '45%', 'display': 'inline-block', 'padding': '20px'}),
    # Gráfico 2: Gastos com Cartão vs Idade com filtro por Faixa Etária
    html.Div([
        dcc.RangeSlider(
            id='idade-slider',
            min=dados_df['idade'].min(),
            max=dados_df['idade'].max(),
            value=[dados_df['idade'].min(), dados_df['idade'].max()],
            marks={i: str(i) for i in range(dados_df['idade'].min(), dados_df['idade'].max(), 5)},
            step=1
        ),
        dcc.Graph(id='gastos-vs-idade-graph')
    ], style={'width': '45%', 'display': 'inline-block', 'padding': '20px'})
    ])
    
def ABA2():
    # Gráfico 3: Perda vs Número de Filhos com filtro por Estado Civil
    return html.Div([
          
           # Gráfico 4: Valor de Crédito vs Renda com filtro por Sexo
        html.Div(
            [
            dcc.Dropdown(
            id='sexo-radio',
            options=[{'label': 'Masculino', 'value': 'masculino'}, {'label': 'Feminino', 'value': 'feminino'}],
            value='masculino',
            #inline=True,
                        ),
                dcc.Graph(id='credito-vs-renda-graph')
            ], style={'width': '40%', 'display': 'inline-block', 'padding': '10px'}),
            html.Div(
               [
                dcc.Dropdown(
                id='estadocivil-dropdown',
                options=[{'label': 'Solteiro', 'value': 0}, {'label': 'Casado', 'value': 1}],
                value=0,
                #placeholder="Estado Civil"
                ),
                dcc.Graph(id='perda-vs-filhos-graph'),
            ], style={'width': '40%', 'display': 'inline-block', 'padding': '10px'}
           )
    ])


# Callbacks independentes para cada gráfico

# Gráfico 1: Valor de Crédito vs Perda por Região
@app.callback(
    Output('credito-vs-perda-graph', 'figure'),
    Input('regiao-dropdown', 'value')
)
def update_credit_vs_perda(selected_region):
    filtered_data = dados_df[dados_df['regiao'] == selected_region]
    fig = px.scatter(filtered_data, x='valorcredito', y='perda',
                     title=f'Crédito vs Perda para Região {selected_region}')
    return fig

# Gráfico 2: Gastos com Cartão vs Idade por Faixa Etária
@app.callback(
    Output('gastos-vs-idade-graph', 'figure'),
    Input('idade-slider', 'value')
)
def update_gastos_vs_idade(age_range):
    filtered_data = dados_df[(dados_df['idade'] >= age_range[0]) & (dados_df['idade'] <= age_range[1])]
    fig = px.scatter(filtered_data, x='idade', y='gastoscartao',
                     title=f'Gastos com Cartão para Idades {age_range[0]} - {age_range[1]}')
    return fig

# Gráfico 3: Perda vs Número de Filhos por Estado Civil
@app.callback(
    Output('perda-vs-filhos-graph', 'figure'),
    Input('estadocivil-dropdown', 'value')
)
def update_perda_vs_filhos(civil_status):
    filtered_data = dados_df[dados_df['estadocivil'] == civil_status]
    fig = px.bar(filtered_data, x='numfilhos', y='perda',
                 title=f'Perda vs Número de Filhos para Estado Civil {"Solteiro" if civil_status == 0 else "Casado"}')
    return fig

# Gráfico 4: Valor de Crédito vs Renda por Sexo
@app.callback(
    Output('credito-vs-renda-graph', 'figure'),
    Input('sexo-radio', 'value')
)
def update_credito_vs_renda(selected_gender):
    filtered_data = dados_df[dados_df['sexo'] == selected_gender]
    fig = px.scatter(filtered_data, x='valorcredito', y='renda',
                     title=f'Crédito x Renda para Sexo {selected_gender.capitalize()}')
    return fig

if __name__ == '__main__':
    app.run(debug=True)
