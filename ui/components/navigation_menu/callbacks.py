import dash
from dash import html
from dash.dependencies import Input, Output
from ..chat_box.chat_box import create_chat_box
from ..chat_input.chat_input import create_chat_input
from ..documentation.documentation import docs_layout 

def redirect(app):
    @app.callback(
        Output('page-content', 'children'),
        Input('url', 'pathname')  
    )
    def display_page(pathname):
        if pathname == '/docs':
            return docs_layout 

        return html.Div([
            create_chat_box(),
            create_chat_input(),
            html.Div(id="last-user-message"),  
            html.Div(id="loading-message-trigger")
        ])
