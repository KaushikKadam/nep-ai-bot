from transformers import pipeline
from chatbot.pdf_reader import load_combined_text

class NEPChatbot:
    def __init__(self):
        # ⚡ Using ultra-fast TinyBERT model
        self.qa_pipeline = pipeline("question-answering", model="deepset/tinybert-base-cased-squad2")
        self.paragraphs = load_combined_text().split('\n\n')  # Split by paragraph

    def find_best_context(self, question):
        # Match question keywords with paragraphs to find best context
        question_words = set(question.lower().split())
        best_para = max(
            self.paragraphs,
            key=lambda para: len(set(para.lower().split()) & question_words)
        )
        return best_para

    def get_response(self, user_input):
        context = self.find_best_context(user_input)
        result = self.qa_pipeline(question=user_input, context=context)
        return result['answer']

    def reset_chat(self):
        self.paragraphs = load_combined_text().split('\n\n')
