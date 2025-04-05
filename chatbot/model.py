# chatbot/model.py
import re
from transformers import pipeline
from chatbot.pdf_reader import load_combined_text

class NEPChatbot:
    def __init__(self):
        # Fast, reliable QnA model
        self.qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
        raw_text = load_combined_text()
        self.context = self.clean_text(raw_text)

    def clean_text(self, text):
        # Remove weird line breaks and extra spaces
        text = re.sub(r'\n+', ' ', text)
        text = re.sub(r'\s{2,}', ' ', text)
        return text.strip()

    def get_response(self, user_input):
        result = self.qa_pipeline(question=user_input, context=self.context)
        return result['answer']

    def reset_chat(self):
        raw_text = load_combined_text()
        self.context = self.clean_text(raw_text)
