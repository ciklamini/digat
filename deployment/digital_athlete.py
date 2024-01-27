
import pandas as pd
import dash
from dash import Dash, dcc, html, Input, Output
import dash_vtk
from dash import html
import numpy as np
import vtk
from dash_vtk.utils import to_mesh_state
app = dash.Dash(__name__)
server = app.server
app.layout = html.Div(
    style={"height": "calc(100vh - 16px)"},
    children=[
                dcc.Dropdown(['DA' ], 
                              'DA', id='demo-dropdown'),
                html.Div(id='dd-output-container', style={"height": "100%", "width": "100%", }),    
                ]  )
@app.callback(
    Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value')
)

if __name__ == "__main__":    app.run_server(debug=True)

