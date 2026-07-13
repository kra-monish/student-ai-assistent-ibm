import streamlit as st
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai import Credentials

st.set_page_config(page_title="Student AI Assistant")

st.title("🎓 Student AI Assistant")

# IBM Credentials
credentials = Credentials(
    api_key=st.secrets["IBM_API_KEY"],
    url="https://us-south.ml.cloud.ibm.com"
)

model = ModelInference(
    model_id="ibm/granite-4-h-small",
    credentials=credentials,
    project_id=st.secrets["PROJECT_ID"]
)

question = st.text_input("Ask your question")

if question:
    response = model.generate_text(
        prompt=f"""
You are a helpful Student AI Assistant.
Help students with programming, AI and career guidance.

Question: {question}
"""
    )

    st.success(response)
