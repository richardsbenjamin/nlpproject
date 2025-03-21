import dash_bootstrap_components as dbc
from dash import html

def create_chat_input():
    return dbc.Container([
        dbc.InputGroup([
                dbc.Input(id="chat-input", placeholder="Ask a weird question...", autoComplete="off"),
                dbc.Button("Send", id="send-button", color="primary"),
        ]),
        dbc.InputGroup([
            dbc.Switch(id="worried-mum-switch", label="Worried Mum Method", value=False),
            html.Div(id="worried-mum-switch-output"),
            dbc.DropdownMenu(
                label="Treatment Method",
                children=[
                    dbc.DropdownMenuItem("No Method", id="no-method-option"),
                    dbc.DropdownMenuItem("Prompting", id="prompting-option"),
                    dbc.DropdownMenuItem("Machine Learning", id="machine-learning-option"),
                    dbc.DropdownMenuItem("Dependency Analysis", id="dependency-analysis-option"),
                ],
                id="treatment-dropdown",
            ),
            html.Div("No Method", id="treatment-dropdown-output", className="mt-2"),
        ]),
    ])
