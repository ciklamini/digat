# -*- coding: utf-8 -*-
"""
goal was to drop dabra 3D point tracks and imshow
https://community.plotly.com/t/exporting-multi-page-dash-app-to-pdf-with-entire-layout/37953/32

"""

from dash import Dash, dcc, html, dash_table, Input, Output, State, callback
import base64
import datetime
import io
import plotly.express as px 
import pandas as pd
import markdowns_for_app as mds

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)


def load_initial_data():
    return pd.read_csv('asset/3Dpts_initial.emt',  
        skiprows=9, 
        delimiter=r"\s+")

def plot_data(df):
    # if 'time' in df.columns:
    if 'Frame' in df.columns:
        melted_df = df.melt(id_vars=['Frame'], var_name='Series', value_name='Value')
        fig = px.line(melted_df, x='Frame', y='Value', color='Series')
        return dcc.Graph(figure=fig)
    else:
        return html.Div(['The "time" column is required in the dataset.'])
    
app.layout = html.Div([
    
    dcc.Markdown(mds.get_intro_markdown(), mathjax=True),
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop 3Dtracks emt file or ',
            html.A('Select It ')
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
        multiple=True
    ),
    html.Div(id='output-data-upload'),
])

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
        elif 'emt' in filename:
            # Assume that the user uploaded emt file 
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')),  
                skiprows=9, 
                delimiter=r"\s+")
            
            # X = df.values.astype('float32')
            df_normalized = (df-df.min())/(df.max()-df.min())
            
            X = df_normalized
            X = X.dropna()
            # X = X.ffill(axis = 0) 
            
            fig = px.imshow(X.T)
    except Exception as e:
        print(e)
        return html.Div(['There was an error processing this file.'
        ])

    return html.Div([
        # markdown pro describe 
        dcc.Markdown(mds.get_description_markdown(), mathjax=True),
        # ukazat vse pomoci lines 
        
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable(
            data = df.to_dict('records'),
            columns = [{'name': i, 'id': i} for i in df.columns],
            page_size=5,
            
        ),
        html.Hr(),  # horizontal line
        html.Div('Plot '),
        dcc.Graph(figure=fig), # tohle jede

        html.Hr(),  # horizontal line
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])

@callback(Output('output-data-upload', 'children'),
          # Output("graph", "figure"),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'),
              State('upload-data', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children
    else: 
        df = load_initial_data()
        df_normalized = (df-df.min())/(df.max()-df.min())
        
        X = df_normalized
        X = X.dropna()
        X = X.ffill(axis = 0)
            
        fig = px.imshow(X.T)

        
        return html.Div([
            plot_data(df),
            html.Hr(),  # horizontal line
            plot_data(X),
            html.Hr(),  # horizontal line
            dcc.Graph(figure=fig), 
            # dcc.Graph(figure=fig2), 
            ])

if __name__ == '__main__':
    app.run_server(debug=True)
