# 🤖 NEP Chatbot (2020–2022)

A chatbot that reads National Education Policy PDFs (2020, 2021, 2022...) and answers questions using NLP.

## 📂 Upload PDFs
Upload new NEP PDFs directly in the web interface or put them in `data/nep_pdfs/`. The chatbot will learn from them.

## 🔧 Tech Stack
- Python
- Streamlit
- HuggingFace Transformers (DistilBERT QnA)
- PyPDF2

## 🚀 How to Run
```bash
git clone https://github.com/yourname/nep2020_chatbot.git
cd nep2020_chatbot
pip install -r requirements.txt
streamlit run app.py
```

## 📚 Sample Questions
- What is NEP 2020?
- What is the 5+3+3+4 structure?
- What does NEP 2022 say about exams?

---
Made with ❤️ for a college project
