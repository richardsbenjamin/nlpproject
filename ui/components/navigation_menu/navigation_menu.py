import dash
import dash_bootstrap_components as dbc
from dash import html

def create_navmenu():
    return dbc.Nav(
        [
            html.Img(
                src="/assets/IMT_Atlantique_logo.png",
            ),
            dbc.NavLink("Adversarial Prompting", href="/", active="exact"),
            dbc.NavLink("Documentation", href="/docs", active="exact"),
        ],
        vertical=True,
        pills=True,
        style={"height": "100vh", "padding": "20px", "background-color": "#f8f9fa"},
    )
