# app.py
# This is the main file where everything gets rendered

import dash
import pandas as pd
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html

# Import components
import components.stockTable as st

# First style sheet is for proxima-nova font
# Second style sheet is for general styling
css = ['https://use.typekit.net/evo5yeo.css', 'assets/styles.css']
app = dash.Dash(__name__, external_stylesheets=css)

colors = {
    'lightGreen': 'rgb(140, 215, 130)',
    'background': 'rgb(28, 36, 47)',
    'turqoise': 'rgb(24, 173, 138)',
    'offwhite': 'rgb(200, 200, 200)',
    'golden': 'rgb(186, 163, 13)',
    'darkRed': 'rgb(122, 23, 23)',
    'raspberry': 'rgb(173, 61, 149)'
}

def wrap(component):
    return html.Div(
        [component],
        className='wrapper'    
    )

app.layout = html.Div([
    html.H1('Investment Dashboard'), 
    wrap(st.render())
])

if __name__ == '__main__':
    app.run_server(debug=True)