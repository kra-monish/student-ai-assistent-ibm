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
    response = model.generate_text(
    prompt=f"""
You are a professional Student AI Assistant.
Give detailed, clear and complete answers.
Explain concepts with examples, steps and practical guidance.

Student Question:
{question}

Answer:
""",
    params={
        "max_new_tokens": 1000,
        "temperature": 0.7
    }
)
    response = model.generate_text(
    prompt=f"""
You are Student AI Assistant.
Provide complete solutions.
Do not give short answers.
Explain step by step with examples, code (if needed), and conclusion.

Question:
{question}

Detailed Answer:
""",
    params={
        "max_new_tokens": 4000,
        "temperature": 0.5
    }
)

st.write(response)
