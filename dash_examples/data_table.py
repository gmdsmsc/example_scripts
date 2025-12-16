import dash
from dash import Dash, html
from dash import dash_table
import pandas as pd

app = Dash(__name__)

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 30, 35],
    "City": ["London", "Paris", "Berlin"]
})

app.layout = html.Div([
    dash_table.DataTable(
        data=df.to_dict("records"),
        columns=[{"name": i, "id": i} for i in df.columns],
        sort_action="native",
        filter_action="native",
        page_action="native",
        page_size=5
    )
])

if __name__ == "__main__":
    app.run(debug=True)