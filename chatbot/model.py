from transformers import pipeline
from chatbot.pdf_reader import load_combined_text

class NEPChatbot:
    def __init__(self):
        self.qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
        self.context = load_combined_text()

    def get_response(self, user_input):
        result = self.qa_pipeline(question=user_input, context=self.context)
        return result['answer']

    def reset_chat(self):
        self.context = load_combined_text()
