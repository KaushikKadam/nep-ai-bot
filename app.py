import streamlit as st
from chatbot.model import NEPChatbot
import os

# Allow file upload
st.set_page_config(page_title="NEP Chatbot", page_icon="📚")
st.title("📚 NEP Chatbot")

if "bot" not in st.session_state:
    st.session_state.bot = NEPChatbot()

# st.markdown("### 📥 Upload NEP PDF (optional)")
# uploaded_file = st.file_uploader("Upload new NEP PDF", type=["pdf"])
# if uploaded_file is not None:
#     save_path = os.path.join("data/nep_pdfs", uploaded_file.name)
#     with open(save_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())
#     st.success(f"Uploaded {uploaded_file.name}")
#     st.session_state.bot.reset_chat()

st.markdown("""
Ask anything about the National Education Policy (NEP) 2020.
The bot is trained on the NEP 2020 document and can answer questions based on it.
You can ask questions like:
- What is the NEP 2020?
- What are the key features of NEP 2020?
- What is the vision of NEP 2020?
- What is the implementation timeline?
- What is the role of the Ministry of Education?
- What is the 5+3+3+4 system?
            
""")

user_input = st.text_input("Ask your question:")
if user_input:
    with st.spinner("Thinking..."):
        response = st.session_state.bot.get_response(user_input)
        st.success(response)

# if st.button("🔄 Reload All PDFs"):
#     st.session_state.bot.reset_chat()
#     st.success("Knowledge refreshed from PDFs!")

st.markdown("---")
st.markdown("Elphinstone college project | 2025")
