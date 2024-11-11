import streamlit as st
from transformers import pipeline

# Set up the summarization pipeline
@st.cache_resource
def load_summarizer():
    return pipeline("summarization")

summarizer = load_summarizer()

# Streamlit app layout
st.title("Text Summarization App")
st.write("Enter some text below, and I'll generate a summary for you.")

# Text input box
input_text = st.text_area("Enter the text you want summarized:", height=200)

# Slider to control summary length
min_length = st.slider("Minimum summary length", 20, 100, 50)
max_length = st.slider("Maximum summary length", 50, 200, 100)

# Generate summary when button is clicked
if st.button("Summarize Text"):
    if input_text:
        with st.spinner("Generating summary..."):
            summary = summarizer(input_text, min_length=min_length, max_length=max_length, do_sample=False)[0]["summary_text"]
            st.subheader("Summary")
            st.write(summary)
    else:
        st.warning("Please enter text to summarize.")
