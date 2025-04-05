from transformers import pipeline

class NEPChatbot:
    def __init__(self):
        self.qa_pipeline = pipeline(
            "question-answering",
            model="deepset/roberta-base-squad2",
            tokenizer="deepset/roberta-base-squad2"
        )
        with open("data/faq_summary.txt", "r", encoding="utf-8") as f:
            self.context = f.read().replace("\n", " ")

    def get_response(self, user_input):
        result = self.qa_pipeline(question=user_input, context=self.context)
        answer = result['answer'].replace("\n", " ").strip()
        return answer

    def reset_chat(self):
        with open("data/faq_summary.txt", "r", encoding="utf-8") as f:
            self.context = f.read().replace("\n", " ")
