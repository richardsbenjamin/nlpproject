import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from components import (
    create_navmenu,
    register_chat_messages,
    register_chat_settings,
    redirect
)

app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"
    ],
    suppress_callback_exceptions=True,    
)

app.layout = dbc.Container(
    [
        dcc.Location(id="url", refresh=False),  
        dbc.Row(
            [
                dbc.Col(create_navmenu(), width=2),
                dbc.Col(html.Div(id="page-content"), width=10),  
            ]
        )
    ],
    fluid=True,
)

register_chat_messages(app)
register_chat_settings(app)
redirect(app)

if __name__ == "__main__":
    app.run_server(debug=False)