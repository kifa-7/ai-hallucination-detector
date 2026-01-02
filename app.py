import streamlit as st

st.set_page_config(page_title="AI Hallucination Detector")

st.title("AI Hallucination Detector")
st.write("Detecting hallucinations in AI-generated responses")

user_input = st.text_area("Paste AI-generated text here:")

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        st.success("Hallucination Risk: Medium")
        st.write(
            "This is a demo output. The full version compares multiple AI responses "
            "using semantic similarity to detect inconsistencies."
        )
