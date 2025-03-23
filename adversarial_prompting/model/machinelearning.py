import lightgbm as lgb
import joblib
import os


def get_model():
    return lgb.Booster(model_file=os.getcwd() + r'\adversarial_prompting\model\lgb_model.txt')

def get_vectoriser():
    return joblib.load(os.getcwd() + r'\adversarial_prompting\model\tfidf_vectorizer.pkl')

def classify_prompt(vectorizer, model, message):
    X_input = vectorizer.transform([message])
    predictions = model.predict(X_input)
    return predictions[0] < 0.5