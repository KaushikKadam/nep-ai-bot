from transformers import pipeline
from chatbot.pdf_reader import load_combined_text

class NEPChatbot:
    def __init__(self):
        self.qa_pipeline = pipeline("question-answering", model="deepset/minilm-uncased-squad2")
        self.paragraphs = load_combined_text().split('\n\n')  # Split by paragraph

    def find_best_context(self, question):
        # Simple scoring: count question keywords in each paragraph
        question_words = set(question.lower().split())
        best_para = max(
            self.paragraphs,
            key=lambda para: len(set(para.lower().split()) & question_words)
        )
        return best_para

    def get_response(self, user_input):
        result = self.qa_pipeline(question=user_input, context=self.context)
        answer = result['answer'].replace("\n", " ").strip()
        return answer

    def reset_chat(self):
        self.paragraphs = load_combined_text().split('\n\n')
