import dash
from dash import html
#placeholder

dash.register_page(__name__)


layout = html.Div([
    html.H1('Placeholder Page'),
    html.Div('content.'),
])
