import streamlit as st
from transformers import pipeline, set_seed
from langchain_community.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

st.set_page_config(page_title="LangChain Text Gen + Summary", layout="centered")
st.title("LangChain-powered Text Generator & Summarizer")

@st.cache_resource
def load_models():
    # GPT-2 for generation
    generator_pipeline = pipeline("text-generation", model="gpt2", device=0)  # Use device=0 for GPU
    llm = HuggingFacePipeline(pipeline=generator_pipeline)

    # BART for summarization
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    return llm, summarizer

llm, summarizer = load_models()

topic = st.text_input("Enter a topic:", placeholder="e.g., Quantum Computing")

if st.button("Generate & Summarize"):
    if not topic:
        st.warning("Please enter a topic.")
    else:
        # Create a custom prompt for GPT-2
        prompt = PromptTemplate.from_template("Write a paragraph about {topic}")
        chain = LLMChain(llm=llm, prompt=prompt)

        with st.spinner("Generating text..."):
            result = chain.run(topic=topic)

        st.subheader("📝 Generated Text")
        st.write(result)

        with st.spinner("Summarizing..."):
            summary = summarizer(result, max_length=100, min_length=30, do_sample=False)[0]['summary_text']

        st.subheader("📌 Summary")
        st.success(summary)
