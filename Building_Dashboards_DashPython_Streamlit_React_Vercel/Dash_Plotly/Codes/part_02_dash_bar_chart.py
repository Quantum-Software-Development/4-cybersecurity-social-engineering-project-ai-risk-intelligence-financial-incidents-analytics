from dash import dcc
import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Exemplo de Layout com Gráfico"),
    dcc.Graph(
        id="example-graph",
        figure={
            "data": [
                {"x": [1, 2, 3], "y": [4, 1, 2], "type": "bar", "name": "SF"}
            ],
            "layout": {"title": "Gráfico Simples"},
        },
    ),
])


if __name__ == "__main__":
    app.run(debug=True)
