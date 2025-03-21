from dash import html

def create_chat_box():
    return html.Div(
        [
            html.H3("Analysis of Generative Artificial Intelligence Inconsistencies", style={"text-align": "center"}),
            html.Div(
                id="chat-messages",
                style={
                    "height": "80vh",
                    "overflow-y": "scroll",
                    "border": "1px solid #ddd",
                    "padding": "10px",
                    "margin-bottom": "10px",
                },
            ),
        ]
    )