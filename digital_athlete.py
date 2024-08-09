import dash  
from dash import html, dcc, Input, Output, State  
import dash_bootstrap_components as dbc  
import base64  
import io  
from PIL import Image  
import dash_core_components as dcc  
import dash_html_components as html  
  
# Initialize the Dash app  
app = dash.Dash(__name__)  
  
app.layout = html.Div([  
    # Header  
    html.H1("Image Upload and Visualization App"),  
      
    # Upload component  
    dcc.Upload(  
        id='upload-image',  
        children=html.Div([  
            'Drag and Drop or ',  
            html.A('Select Files')  
        ]),  
        style={  
            'width': '100%',  
            'height': '60px',  
            'lineHeight': '60px',  
            'borderWidth': '1px',  
            'borderStyle': 'dashed',  
            'borderRadius': '5px',  
            'textAlign': 'center',  
            'margin': '10px'  
        },  
        # Allow multiple files to be uploaded  
        multiple=False  
    ),  
  
    # Layout with two columns  
    dbc.Row([  
        # Left column with image visualization  
        dbc.Col([  
            html.Div(id='output-image-upload')  
        ], width=6),  
  
        # Right column with string description in markdown  
        dbc.Col([  
            dcc.Markdown(id='image-description')  
        ], width=6)  
    ])  
])  
  
def parse_contents(contents):  
    content_type, content_string = contents.split(',')  
  
    decoded = base64.b64decode(content_string)  
    image = Image.open(io.BytesIO(decoded))  
    return image  
  
@app.callback(  
    [Output('output-image-upload', 'children'),  
     Output('image-description', 'children')],  
    [Input('upload-image', 'contents')],  
)  
def update_output(contents):  
    if contents is not None:  
        image = parse_contents(contents)  
        image_visual = html.Img(src=contents, style={'width': '100%'})  
  
        # Here you can define your string description  
        string_description = """  
        ### Image Description  
        - **Format:** {}  
        - **Size:** {}x{}  
        """.format(image.format, image.width, image.height)  
  
        return image_visual, string_description  
    else:  
        return None, None  
  
# Run the app  
if __name__ == '__main__':  
    app.run_server(debug=True)  
