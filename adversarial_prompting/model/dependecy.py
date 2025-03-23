import spacy
import os

# Load the SpaCy model
nlp = spacy.load("en_core_web_lg")

# Load bad words from external file
bad_words_file_path = os.path.join(os.path.dirname(__file__), "bad_word_bank.txt")
with open(bad_words_file_path, "r", encoding="utf-8") as f:
    bad_words = set(word.strip().lower() for word in f.readlines())

# Categorizing suspicious words (subset from bad-words list)
crime_keywords = {"fraud", "theft", "bribe", "blackmail", "extort", "scam", "money laundering", "forgery", "embezzle"}
violence_keywords = {"attack", "murder", "assault", "homicide", "terrorism", "abduction"}
sexual_keywords = {"rape", "harass", "molest", "porn", "prostitution"}
hate_speech_keywords = {"racist", "homophobic", "xenophobic", "slur", "bigot"}

# Merge categories into one set of suspicious keywords
suspicious_keywords = crime_keywords | violence_keywords | sexual_keywords | hate_speech_keywords

# Entity categories (adjusted to match bad-words list themes)
suspicious_entities = {
    "MONEY", "CURRENCY", "CARDINAL", "QUANTITY", "PERCENT",
    "LAW", "CRIME", "ORDINAL", "EVENT",
    "ORG", "GPE", "FAC", "NORP", "LOC",
    "PERSON", "GROUP", "TITLE", "ROLE", "WORK_OF_ART", "RELIGION",
    "PRODUCT", "TECHNOLOGY", "SOFTWARE", "HARDWARE", "WEAPON", "DEVICE",
    "MEDICAL_CONDITION", "DISEASE", "SYMPTOM", "DRUG", "VIRUS", "BACTERIA", "CHEMICAL", "TOXIN",
    "NATIONALITY", "IDEOLOGY", "MILITARY", "WAR", "TERRORIST_GROUP", "INSURGENCY",
    "DOMAIN", "IP_ADDRESS", "SERVER", "NETWORK", "HACKING_TOOL", "DARKWEB_SITE", "EXPLOIT",
    "EMAIL", "USERNAME", "PASSWORD", "PHONE_NUMBER", "SOCIAL_SECURITY_NUMBER", "CREDIT_CARD",
}

SIMILARITY_THRESHOLD = 0.6  # Threshold for semantic similarity checking

def check_cos_sim(word1_str: str, word2_str: str) -> bool:
    """Checks if two words are semantically similar using SpaCy word embeddings."""
    word1 = nlp(word1_str)
    word2 = nlp(word2_str)
    return word1.similarity(word2) > SIMILARITY_THRESHOLD

def check_words(token: str, word_list: set[str]) -> bool:
    """Checks if a token matches or is similar to any word in a given word list."""
    token = token.lower()
    if token in word_list:
        return True
    return any(check_cos_sim(token, sus_word) for sus_word in word_list)

def check_suspicious_words(token: str) -> bool:
    """Checks if a token is a suspicious keyword."""
    return check_words(token, suspicious_keywords)

def check_suspicious_entities(entity_label: str, entity_text: str) -> bool:
    """Checks if an entity label or text is suspicious."""
    return entity_label in suspicious_entities or check_words(entity_text.lower(), suspicious_keywords)

def detect_illegal_activity(text: str) -> dict:
    """Detects suspicious words and entities in a given text."""
    doc = nlp(text)

    found_keywords = [token.text for token in doc if check_suspicious_words(token.lemma_)]
    found_entities = [(ent.text, ent.label_) for ent in doc.ents if check_suspicious_entities(ent.label_, ent.text)]

    return {
        "suspicious_keywords": found_keywords,
        "suspicious_entities": found_entities,
        "is_suspicious": bool(found_keywords or found_entities),
    }
