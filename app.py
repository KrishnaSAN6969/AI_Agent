import streamlit as st
from main import run_research


st.set_page_config(page_title="AI Research Assistant", page_icon="🧠", layout="wide")

st.title("🧠 AI Research Assistant")
st.write("Ask me any research question, and I will gather information using tools and return structured results.")


query = st.text_input("🔍 Enter your research question:")


if st.button("Run Research"):
    if query.strip():
        with st.spinner("🔎 Researching... Please wait."):
            try:
                result = run_research(query)

                st.subheader("📌 Topic")
                st.write(result.topic)

                st.subheader("📝 Summary")
                st.write(result.summary)

                st.subheader("📚 Sources")
                for src in result.sources:
                    st.markdown(f"- [{src}]({src})")

                st.subheader("🛠️ Tools Used")
                st.write(", ".join(result.tools_used))

            except Exception as e:
                st.error(f"Something went wrong: {e}")
    else:
        st.warning("⚠️ Please enter a question before running research.")
