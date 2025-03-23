from dash import html, Input, Output, State, dcc, callback_context
from ui.components.chat_box.functions import (
    create_assistant_message,
    create_user_message,
    create_loading_message,
    format_response
)
from adversarial_prompting.model.chat_client import ChatClient
from config.config import API_KEY, MODEL

client = ChatClient(api_key=API_KEY, model=MODEL)

def register_chat_messages(app):
    @app.callback(
        [
            Output("chat-messages", "children"), 
            Output("chat-input", "value"), 
            Output("last-user-message", "data"), 
            Output("chat-input","disabled", allow_duplicate=True),
            Output("send-button", "disabled", allow_duplicate=True)],
        [Input("send-button", "n_clicks"), Input("chat-input", "n_submit")],
        [State("chat-input", "value"), State("chat-messages", "children")],
        prevent_initial_call=True
    )
    def add_user_message(n_clicks, n_submit, user_message, existing_messages):
        if not user_message:
            return existing_messages, "", None, False, False

        user_message_div = create_user_message(user_message)
        updated_messages = (existing_messages or []) + [user_message_div]

        return updated_messages, "", user_message, True, True

    @app.callback(
        [Output("chat-messages", "children", allow_duplicate=True), Output("loading-message-trigger", "data")],
        Input("last-user-message", "data"),
        State("chat-messages", "children"),
        prevent_initial_call=True,
    )
    def add_loading_message(last_user_message, existing_messages):
        if not last_user_message:
            return existing_messages, None

        loading_message_div = create_loading_message()
        updated_messages = existing_messages + [loading_message_div]

        return updated_messages, True

    @app.callback(
        [
            Output("chat-messages", "children", allow_duplicate=True), 
            Output("chat-input", "disabled"),
            Output("send-button", "disabled")
        ],
        Input("loading-message-trigger", "data"),
        State("last-user-message", "data"),
        State("chat-messages", "children"),
        prevent_initial_call=True,
    )
    def add_assistant_response(trigger, last_user_message, existing_messages):
        if not last_user_message:
            return existing_messages, True, True

        _, assistant_response = client.add_and_get_response("user", last_user_message)
        updated_messages = existing_messages[:-1]

        processed_response = client.process_response(assistant_response)
        summary_div = create_assistant_message(
            format_response(processed_response)
        )
        updated_messages += [summary_div]
        
        client.reset()

        return updated_messages, False, False


def register_chat_settings(app):

    @app.callback(
        Output("worried-mum-switch-output", "children"),
        Input("worried-mum-switch", "value")
    )
    def update_output(value):
        client.switch_worried_mum(value)
        return ""
    
    @app.callback(
        Output("treatment-dropdown-output", "children"),
        [Input("no-method-option", "n_clicks"),
        Input("prompting-option", "n_clicks"),
        Input("machine-learning-option", "n_clicks"),
        Input("dependency-analysis-option", "n_clicks")]
    )
    def update_output(n1, n2, n3, n4):
        if not callback_context.triggered:
            return "No Method"
        else:
            button_id = callback_context.triggered[0]["prop_id"].split(".")[0]
            method =  " ".join(button_id.split('-')[:-1])
            client.set_treatment_method(method)
            return method.capitalize()