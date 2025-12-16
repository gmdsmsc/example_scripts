import dash
from dash import dcc, html, Output, Input
import time

# Initialize the app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.Button("Load Data", id="load-button"),
    dcc.Loading(
        id="loading-spinner",
        type="circle",  # Options: 'circle', 'dot', 'default'
        children=html.Div(id="loading-output")
    )
])

@app.callback(
    Output("loading-output", "children"),
    Input("load-button", "n_clicks")
)
def load_data(n_clicks):
    if not n_clicks:
        return "Click the button to load data"
    
    # Simulate a long computation
    time.sleep(3)
    
    return "Data loaded successfully!"

if __name__ == "__main__":
    app.run(debug=True)
