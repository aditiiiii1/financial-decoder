import streamlit as st
import google.generativeai as genai
import pandas as pd
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

# Streamlit UI
st.set_page_config(page_title="Financial Decoder AI", layout="wide")
st.title("📊 Gemini Pro Financial Decoder")

# File Upload
uploaded_file = st.file_uploader("Upload Financial Report (CSV)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Preview of Financial Report:")
    st.dataframe(df.head())

    # Generate AI Summary
    if st.button("Generate Summary"):
        with st.spinner("Analyzing..."):
            prompt = f"""
            You are a financial analyst AI. Summarize this financial data and highlight key insights.
            Here is the data:
            {df.to_string()}
            """
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(prompt)
            st.subheader("📑 AI-Generated Summary:")
            st.write(response.text)
