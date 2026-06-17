import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AWS RAG Assistant",layout="wide")


page = st.sidebar.selectbox("Choose Page",["Chat", "Analytics"])

if page == "Chat":
    st.title("AWS Agreement Assistant 🤖")
    question = st.text_input("Ask Question")

    if st.button("Ask"):
        if not question:
            st.warning("Please enter a question")
        else:
            try:
                with st.spinner("Searching document and generating answer..."):
                    response = requests.post(API_URL + "/ask",json={"question": question},timeout=120)

                if response.status_code == 200:
                    data = response.json()
                    st.subheader("Answer")
                    st.write(data["answer"])
                    st.subheader("Sources")

                    for source in data["sources"]:
                        st.write("Page:",source["page"])
                        st.write(source["content"])
                        st.divider()

                else:
                    st.error(f"Backend Error : {response.status_code}")
                    st.write(response.text)

            except requests.exceptions.ConnectionError:
                st.error("FastAPI server is not running")

            except Exception as e:
                st.error("Something went wrong")
                st.write(e)

else:
    st.title("Analytics Dashboard 📊")

    try:
        response = requests.get(API_URL + "/analytics")

        if response.status_code == 200:
            data = response.json()
            st.metric("Total Questions",data["total_questions"])
            st.metric("Average Latency",round(data["average_latency"],2))
            st.subheader("Failed Questions")
            st.write(data["failed_questions"])
        else:
            st.error("Unable to load analytics")

    except Exception as e:
        st.error("Backend not connected")
        st.write(e)