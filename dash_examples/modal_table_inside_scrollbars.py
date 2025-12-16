import dash
from dash import Dash, html, dash_table, Input, Output, State
import pandas as pd

# Sample data
data = pd.DataFrame({
    "Column 1": range(50),
    "Column 2": ["Data"]*50,
    "Column 3": ["More Data"]*50,
    "Column 4": ["Even More Data"]*50,
})

app = Dash(__name__)

app.layout = html.Div([
    html.Button("Open Modal", id="open-modal", n_clicks=0),
    
    # Modal overlay
    html.Div(
        id="modal",
        style={
            "display": "none",
            "position": "fixed",
            "top": 0,
            "left": 0,
            "width": "100%",
            "height": "100%",
            "backgroundColor": "rgba(0,0,0,0.5)",
            "zIndex": 1000,
        },
        children=[
            # Modal content
            html.Div(
                style={
                    "position": "absolute",
                    "top": "50%",
                    "left": "50%",
                    "transform": "translate(-50%, -50%)",
                    "width": "80%",
                    "height": "80%",
                    "backgroundColor": "white",
                    "padding": "20px",
                    "boxShadow": "0px 0px 10px rgba(0,0,0,0.25)",
                    "overflow": "hidden",
                    "display": "flex",
                    "flexDirection": "column",
                },
                children=[
                    html.Div(
                        "Scrollable Table Modal",
                        style={"fontSize": "20px", "fontWeight": "bold", "marginBottom": "10px"}
                    ),
                    html.Div(
                        dash_table.DataTable(
                            id='table',
                            columns=[{"name": i, "id": i} for i in data.columns],
                            data=data.to_dict('records'),
                            style_table={
                                'height': '100%',
                                'overflowY': 'auto',
                                'overflowX': 'auto',
                                'minWidth': '100%',
                            },
                            style_cell={
                                'minWidth': '150px', 'width': '150px', 'maxWidth': '150px',
                                'whiteSpace': 'normal'
                            },
                            fixed_rows={'headers': True},
                        ),
                        style={"flex": "1", "overflow": "auto"}  # makes the table scrollable
                    ),
                    html.Button("Close", id="close-modal", n_clicks=0, style={"marginTop": "10px", "alignSelf": "flex-end"})
                ]
            )
        ]
    )
])

@app.callback(
    Output("modal", "style"),
    [Input("open-modal", "n_clicks"), Input("close-modal", "n_clicks")],
    [State("modal", "style")],
)
def toggle_modal(open_clicks, close_clicks, style):
    if open_clicks or close_clicks:
        if style["display"] == "none":
            style["display"] = "block"
        else:
            style["display"] = "none"
    return style

if __name__ == "__main__":
    app.run(debug=True)
