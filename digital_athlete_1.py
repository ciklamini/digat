
# -*- coding: utf-8 -*-
"""
"""
import dash  
from dash import html, dcc, Input, Output, State  
import dash_bootstrap_components as dbc  
import base64  
import io  
from PIL import Image  
  
class ImageUploadApp:  
    def __init__(self, title="Image Upload and Visualization App"):  
        self.title = title  
        self.app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])  
        self._set_layout()  
        self._set_callbacks()  
  
    def _set_layout(self):  
        self.app.layout = html.Div([  
            # Header  
            html.H1(self.title),  
              
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
  
    def _set_callbacks(self):  
        @self.app.callback(  
            [Output('output-image-upload', 'children'),  
             Output('image-description', 'children')],  
            [Input('upload-image', 'contents')],  
        )  
        def update_output(contents):  
            if contents is not None:  
                image = self._parse_contents(contents)  
                image_visual = html.Img(src=contents, style={'width': '100%'})  
  
                # Here you can define your string description  
                string_description = self._generate_description(image)  
  
                return image_visual, string_description  
            else:  
                return None, None  
  
    def _parse_contents(self, contents):  
        content_type, content_string = contents.split(',')  
  
        decoded = base64.b64decode(content_string)  
        image = Image.open(io.BytesIO(decoded))  
        return image  
  
    def _generate_description(self, image):  
        return """  
        ### Image Description  
        - **Format:** {}  
        - **Size:** {}x{}  
        """.format(image.format, image.width, image.height)  
  
    def run(self, debug=True):  
        self.app.run_server(debug=debug)  


if __name__ == '__main__':
  app = ImageUploadApp()   
  server = app.server # tohle je mega dulezity
  app.run()  
