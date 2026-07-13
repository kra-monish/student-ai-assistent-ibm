import streamlit as st

st.set_page_config(page_title="Student AI Assistant")

st.title("🎓 Student AI Assistant")

question = st.text_input("Ask your question")

if question:
    q = question.lower()

    if "python" in q:
        st.success("Python is a high-level programming language used in AI, Web Development, Data Science and Automation.")

    elif "ai" in q or "artificial intelligence" in q:
        st.success("Artificial Intelligence enables computers to learn, reason and solve problems like humans.")

    elif "machine learning" in q:
        st.success("Machine Learning is a branch of AI where computers learn from data without being explicitly programmed.")

    elif "career" in q:
        st.success("Focus on DSA, Projects, GitHub, Resume and Internships to build a strong software career.")

    else:
        st.success("Thank you for your question. This Student AI Assistant can help with Programming, AI and Career Guidance.")
