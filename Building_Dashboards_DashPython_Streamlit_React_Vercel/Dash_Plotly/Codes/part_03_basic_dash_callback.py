from dash import dcc
import dash
from dash import html
from dash import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Programando o Callback"),
    dcc.Input(id="input-text", value="Escreva algo...", type="text"),
    html.Div(id="output-text"),
])


@app.callback(
    Output("output-text", "children"),
    Input("input-text", "value"),
)
def update_output(value):
    return f"Você escreveu: {value}"


if __name__ == "__main__":
    app.run(debug=True)
