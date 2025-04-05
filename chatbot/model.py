from transformers import pipeline
from chatbot.pdf_reader import load_combined_text

class NEPChatbot:
    def __init__(self):
        # Load a high-performing model and tokenizer
        self.qa_pipeline = pipeline(
            "question-answering",
            model="deepset/roberta-base-squad2",
            tokenizer="deepset/roberta-base-squad2"
        )

        # Load and preprocess the NEP text
        self.paragraphs = load_combined_text().split('\n\n')

    def find_best_context(self, question):
        question_words = set(question.lower().split())
        best_para = max(
            self.paragraphs,
            key=lambda para: len(set(para.lower().split()) & question_words)
        )
        return best_para

    def get_response(self, user_input):
        context = self.find_best_context(user_input)
        result = self.qa_pipeline(question=user_input, context=context)
        return result['answer'].strip().replace('\n', ' ')

    def reset_chat(self):
        self.paragraphs = load_combined_text().split('\n\n')
