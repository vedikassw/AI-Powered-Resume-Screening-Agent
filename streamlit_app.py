import streamlit as st
from app.utils import extract_text_from_pdf, clean_text
from app.model import get_similarity

st.title("AI-Powered Resume Screening Agent")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description")

if uploaded_file and job_description:
    resume_text = extract_text_from_pdf(uploaded_file)
    resume_text = clean_text(resume_text)
    job_description = clean_text(job_description)

    score = get_similarity(resume_text, job_description)

    st.subheader(f"Match Score: {score}%")

    if score > 70:
        st.success("Strong Match ✅")
    elif score > 40:
        st.warning("Moderate Match ⚠️")
    else:
        st.error("Low Match ❌")
