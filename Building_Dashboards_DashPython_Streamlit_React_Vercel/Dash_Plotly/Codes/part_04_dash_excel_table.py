import pandas as pd
import dash
from dash import dcc, html

dados_df=pd.read_excel("BASE01.CREDITO.xlsx")
app = dash.Dash(__name__)

app.layout = html.Div([
    # Cabeçalho
    html.Div([
        html.H1("Dashboard de Crédito"),
        html.P("Análise de dados de crédito dos clientes")
    ], style={'text-align': 'center', 'padding': '20px', 'backgroundColor': '#ffffff'}),


    # Tabela de Dados
    html.Div([
        html.H3("Dados Detalhados"),
        dash.dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in dados_df.columns],
            data=dados_df.head(20).to_dict('records')
        )
    ], style={'padding': '20px'})
])


if __name__ == '__main__':
    app.run(debug=True)
