import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Meu Primeiro App Dash"),
    html.P("Criando layout básico com Dash")
])

if __name__ == "__main__":
    app.run(debug=True)
