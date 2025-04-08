from transformers import pipeline
from chatbot.pdf_reader import load_combined_text

class NEPChatbot:
    def __init__(self):
        print("⏳ Loading model...")
        self.qa_pipeline = pipeline(
            "question-answering",
            model="model/minilm-uncased-squad2",
            tokenizer="model/minilm-uncased-squad2"
        )
        self.paragraphs = load_combined_text().split('\n\n')
        print("✅ Model and context loaded.")

    def find_best_context(self, question):
        question_words = set(question.lower().split())

        # Score based on overlapping words (basic relevance)
        best_para = max(
            self.paragraphs,
            key=lambda para: len(set(para.lower().split()) & question_words)
        )
        return best_para.strip()

    def get_response(self, user_input):
        context = self.find_best_context(user_input)
        result = self.qa_pipeline(question=user_input, context=context)
        return result['answer'].strip()

    def reset_chat(self):
        self.paragraphs = load_combined_text().split('\n\n')
        print("✅ Chat reset and context reloaded.")