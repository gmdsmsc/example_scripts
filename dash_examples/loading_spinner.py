import dash
from dash import dcc, html, Output, Input, State
import time
import base64
import io

# Initialize the app
app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Upload(
        id="upload-data",
        children=html.Div([
            "Drag and Drop or ",
            html.A("Select a File")
        ]),
        style={
            "width": "300px",
            "height": "60px",
            "lineHeight": "60px",
            "borderWidth": "1px",
            "borderStyle": "dashed",
            "borderRadius": "5px",
            "textAlign": "center",
            "margin": "10px"
        },
        multiple=False  # Only allow single file upload
    ),
    dcc.Loading(
        id="loading-spinner",
        type="circle",  # Options: 'circle', 'dot', 'default'
        children=html.Div(id="loading-output")
    )
])

@app.callback(
    Output("loading-output", "children"),
    Input("upload-data", "contents"),
    State("upload-data", "filename")
)
def load_data(contents, filename):
    if contents is None:
        return "Upload a file to load data"
    
    # Simulate a long computation
    time.sleep(3)

    # Optionally process the uploaded file
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    # You could parse the file here with pandas if needed
    # For example:
    # import pandas as pd
    # df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))

    return f"File '{filename}' loaded successfully!"

if __name__ == "__main__":
    app.run(debug=True)
