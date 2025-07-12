import streamlit as st
from summarize import generate_summary

# Page configuration
st.set_page_config(page_title="Text Summarizer", layout="centered")

# Title and description
st.title("📝 Text Summarization using BART")
st.markdown(
    "This app uses the `facebook/bart-large-cnn` model to generate an **abstractive summary** of the text you enter."
)

# Text input
user_input = st.text_area("Enter article or paragraph text below:", height=250)

# Button to generate summary
if st.button("Summarize"):
    if user_input.strip():
        with st.spinner("Generating summary..."):
            try:
                summary = generate_summary(user_input)
                st.subheader("📄 Summary")
                st.success(summary)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some text to summarize.")
