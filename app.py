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
Ask anything about the National Education Policy 📘

Try asking:
- What is the 5+3+3+4 education system?
- What changes were made in 2022?
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
