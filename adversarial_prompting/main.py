from config.config import API_KEY, MODEL
from model.chat_client import ChatClient
from utils.messaging import is_negative_response, print_message
import re
import textwrap
from colorama import init, Fore, Style

# Inicializa o Colorama para suporte a cores no terminal
init(autoreset=True)

def format_response(response, width: int = 80) -> str:
    """
    Formata qualquer resposta da API para uma exibição melhor no terminal.
    - Converte **negrito** para texto destacado.
    - Converte `código` para texto em amarelo.
    - Formata listas numeradas e itens iniciados com '-' ou '•'.
    - Realiza quebra de linha para manter a largura definida.
    """
    # Converte a resposta para string, caso não seja
    response = str(response)
    
    # Formata negrito (**texto**)
    response = re.sub(r"\*\*(.*?)\*\*", lambda m: Style.BRIGHT + m.group(1) + Style.NORMAL, response)
    # Formata código inline (`texto`)
    response = re.sub(r"`(.*?)`", lambda m: Fore.YELLOW + m.group(1) + Fore.RESET, response)
    
    formatted_lines = []
    for line in response.splitlines():
        stripped = line.strip()
        if re.match(r"^\d+\.\s", stripped):
            line = Fore.CYAN + stripped + Fore.RESET
        elif stripped.startswith(("-", "•")):
            line = Fore.GREEN + stripped + Fore.RESET
        formatted_lines.append(line)
        
    wrapped_lines = [textwrap.fill(line, width=width) for line in formatted_lines]
    return "\n".join(wrapped_lines)

def main():
    client = ChatClient(api_key=API_KEY, model=MODEL)
    
    user_input = input("You: ")
    assistant_response = client.add_and_get_response("user", user_input)
    print_message("Mistrall", format_response(assistant_response))
    
    # Converter a resposta para string antes de verificar se é negativa
    if is_negative_response(str(assistant_response)):
        assistant_response = client.handle_negative_response()
        print_message("Mistrall", format_response(assistant_response))
    
    summary_response = client.summarize_response()
    print_message("Summary", format_response(summary_response))
    
if __name__ == "__main__":
    main()
