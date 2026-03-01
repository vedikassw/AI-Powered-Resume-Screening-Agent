import streamlit as st
from app.utils import extract_text_from_pdf, clean_text
from app.model import get_similarity

st.set_page_config(page_title="AI Resume Screening Agent")

st.title("AI Resume Screening Agent")
st.write("Upload a resume and paste the job description to calculate a match score.")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description")

if uploaded_file and job_description:
    resume_text = extract_text_from_pdf(uploaded_file)
    resume_text = clean_text(resume_text)
    job_description = clean_text(job_description)

    score = get_similarity(resume_text, job_description)

    st.subheader("Match Score")
    st.success(f"{score}%")

    if score >= 75:
        st.info("Strong match candidate")
    elif score >= 50:
        st.warning("Moderate match candidate")
    else:
        st.error("Low match candidate")
