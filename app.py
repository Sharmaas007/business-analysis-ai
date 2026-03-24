import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Business Analyst AI Agent",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Business Analyst AI Agent")
st.markdown("Transform unstructured requirements into professional documentation")

with st.sidebar:
    st.markdown("## ⚙️ Configuration")
    
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        st.warning("⚠️ OpenAI API Key not configured")
        st.info("""
        1. Go to https://platform.openai.com/api-keys
        2. Create a new API key
        3. Create a `.env` file in your project folder
        4. Add: `OPENAI_API_KEY=your-key-here`
        5. Restart this app
        """)
    else:
        st.success("✓ API Key Configured")

st.markdown("### Enter Your Business Requirement")

requirement_input = st.text_area(
    "Business Requirement:",
    placeholder="Describe your business requirement here...",
    height=200,
    label_visibility="collapsed"
)

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("🔍 Analyze Requirement", key="analyze"):
        if not requirement_input.strip():
            st.error("❌ Please enter a requirement to analyze")
        else:
            st.info("✓ Setup your agent first. See README for instructions.")

with col2:
    if st.button("🗑️ Clear", key="clear"):
        st.rerun()

st.markdown("""
---
### Setup Instructions:
1. Install: `pip install -r requirements.txt`
2. Configure API key in `.env` file
3. Run: `streamlit run app.py`
""")
