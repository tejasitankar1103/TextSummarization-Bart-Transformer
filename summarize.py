from transformers import pipeline
import streamlit as st

def generate_summary(text: str) -> str:
    """
    Generate an abstractive summary for the input text using BART transformer.

    Parameters:
    text (str): The input text to summarize.

    Returns:
    str: The summarized text.
    """

    @st.cache_resource
    def load_summarizer():
       return pipeline("summarization", model="facebook/bart-large-cnn")


    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']


if __name__ == "__main__":
    # Example text to test summarization
    sample_text = (
        "The Amazon rainforest, also known in English as Amazonia, is a moist broadleaf tropical rainforest "
        "in the Amazon biome that covers most of the Amazon basin of South America. This basin encompasses "
        "7,000,000 km2 (2,700,000 sq mi), of which 5,500,000 km2 (2,100,000 sq mi) are covered by the rainforest. "
        "This region includes territory belonging to nine nations."
    )

    print("Original Text:")
    print(sample_text)
    print("\nGenerated Summary:")
    print(generate_summary(sample_text))
