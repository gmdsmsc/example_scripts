from dash import Dash, dcc, html, Input, Output
import base64
import io
import pandas as pd

def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)

    try:
        if filename.endswith('.csv'):
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        elif filename.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(io.BytesIO(decoded))
        else:
            return html.Div(['Unsupported file type'])
    except Exception as e:
        return html.Div(['Error processing file'])

    return html.Div([
        html.H5(filename),
        html.Pre(df.head().to_string())
    ])



app = Dash(__name__)

app.layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select a File')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
        },
        multiple=False  # set True to allow multiple files
    ),
    html.Div(id='output-data')
])

@app.callback(
    Output('output-data', 'children'),
    Input('upload-data', 'contents'),
    Input('upload-data', 'filename'))
def update_output(contents, filename):
    if contents is not None:
        return parse_contents(contents, filename)



if __name__ == '__main__':
    app.run(debug=True)
