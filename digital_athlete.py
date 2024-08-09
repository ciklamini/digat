import dash
from dash import dcc, html
import pandas as pd

# Create a simple DataFrame
df = pd.DataFrame({
    "Year": [2010, 2011, 2012, 2013, 2014],
    "Value": [100, 200, 300, 400, 500]
})

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Simple Dash App'),

    html.Div(children='A simple line chart example.'),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df['Year'], 'y': df['Value'], 'type': 'line', 'name': 'Value'},
            ],
            'layout': {
                'title': 'Yearly Values'
            }
        }
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
