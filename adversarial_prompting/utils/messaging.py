import re

NEGATION_PATTERNS = re.compile(r"\b(not|never|no|cannot|can't|won't|sorry|unable|impossible|refuse)\b", re.IGNORECASE)

def is_negative_response(response):
    return NEGATION_PATTERNS.search(response) is not None

def add_message(conversation_history, role, content):
    conversation_history.append({"role": role, "content": content})

def print_message(role, content):
    print(f"\n{role}: {content}\n")
