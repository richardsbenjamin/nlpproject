from dash import html, dcc

def create_user_message(message):
    return html.Div(
        [
            html.Span(message, style={"flex": "1"}),
            html.I(
                className="fas fa-user",
                style={"font-size": "20px", "color": "#888", "margin-left": "10px"},
            ),
        ],
        style={
            "background-color": "#EFF6FF",
            "padding": "10px",
            "border-radius": "10px",
            "margin-bottom": "10px",
            "max-width": "70%",
            "margin-left": "auto",
            "display": "flex",
            "align-items": "center",
            "justify-content": "space-between",
        },
    )

def create_assistant_message(message):
    return html.Div(
        [
            html.I(
                className="fas fa-robot",
                style={"margin-right": "8px", "font-size": "20px", "color": "#888"},
            ),
            message
        ],
        style={
            "background-color": "#F8F9FA",
            "padding": "10px",
            "border-radius": "10px",
            "margin-bottom": "10px",
            "max-width": "70%",
            "margin-right": "auto",
            "display": "flex",
            "align-items": "center",
        },
    )

def create_loading_message():
    return html.Div(
        [
            html.I(
                className="fas fa-robot",
                style={"margin-right": "8px", "font-size": "20px", "color": "#888"},
            ),
            html.Div(
                className="spinner-border spinner-border-sm",
                role="status",
                style={"margin-right": "8px"},
            )
        ],
        style={
            "background-color": "#F8F9FA",
            "padding": "10px",
            "border-radius": "10px",
            "margin-bottom": "10px",
            "max-width": "70%",
            "margin-right": "auto",
            "display": "flex",
            "align-items": "center",
        },
    )
    
def format_response(response: str):
    response = str(response)
    return dcc.Markdown(response)

