import dash
from dash import html, dash_table, Input, Output, State

app = dash.Dash(__name__)

# Sample data
data = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"},
]

# Dark-mode styled table
table = dash_table.DataTable(
    id="table",
    columns=[
        {"name": "ID", "id": "id"},
        {"name": "Name", "id": "name"},
        {"name": "Action", "id": "action"},
    ],
    data=[{**row, "action": f"Open {row['id']}"} for row in data],
    style_table={
        "backgroundColor": "#0e1117",
        "borderRadius": "8px",
        "overflow": "hidden",
        "padding": "10px",
    },
    style_header={
        "backgroundColor": "#262730",
        "color": "#fafafa",
        "fontWeight": "bold",
        "border": "none",
    },
    style_cell={
        "backgroundColor": "#0e1117",
        "color": "#fafafa",
        "border": "none",
        "padding": "8px",
        "textAlign": "left",
    },
    style_data_conditional=[
        {
            "if": {"row_index": "odd"},
            "backgroundColor": "#1c1e24",
        },
        {
            "if": {"state": "active"},
            "backgroundColor": "#31333F",
            "border": "1px solid #565869",
        },
        {
            "if": {"state": "selected"},
            "backgroundColor": "#565869",
            "color": "#ffffff",
        },
    ],
)

app.layout = html.Div(
    style={"backgroundColor": "#0e1117", "height": "100vh", "padding": "20px"},
    children=[
        table,

        # Modal overlay
        html.Div(
            id="modal",
            style={"display": "none",
                   "position": "fixed", "top": "0", "left": "0",
                   "width": "100%", "height": "100%",
                   "backgroundColor": "rgba(0,0,0,0.7)",
                   "zIndex": "1000", "justifyContent": "center", "alignItems": "center"},
            children=html.Div(
                id="modal-content",
                style={"backgroundColor": "#262730", "padding": "20px",
                       "borderRadius": "8px", "width": "300px", "margin": "auto",
                       "textAlign": "center", "color": "#fafafa"},
                children=[
                    html.H4("Row Info", style={"color": "#fafafa"}),
                    html.Div(id="modal-body"),
                    html.Button("Close", id="close-btn",
                                style={"marginTop": "15px",
                                       "backgroundColor": "#565869",
                                       "color": "#fafafa",
                                       "border": "none",
                                       "padding": "8px 16px",
                                       "borderRadius": "4px",
                                       "cursor": "pointer"})
                ]
            )
        )
    ]
)

@app.callback(
    Output("modal", "style"),
    Output("modal-body", "children"),
    Input("table", "active_cell"),
    Input("close-btn", "n_clicks"),
    State("table", "data"),
)
def toggle_modal(active_cell, close_clicks, rows):
    ctx = dash.callback_context
    if ctx.triggered:
        trigger = ctx.triggered[0]["prop_id"].split(".")[0]
        if trigger == "close-btn":
            return {"display": "none"}, ""
        elif trigger == "table" and active_cell and active_cell["column_id"] == "action":
            row = rows[active_cell["row"]]
            return {"display": "flex",
                    "position": "fixed", "top": "0", "left": "0",
                    "width": "100%", "height": "100%",
                    "backgroundColor": "rgba(0,0,0,0.7)",
                    "zIndex": "1000", "justifyContent": "center", "alignItems": "center"}, \
                   f"You clicked row {row['id']}"
    return {"display": "none"}, ""

if __name__ == "__main__":
    app.run(debug=True)