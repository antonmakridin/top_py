import streamlit as st
from yandexkey import YandexGPT

yandex = YandexGPT()

st.title("Чат с Яндексом")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["text"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "text": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant yandex in chat message container
    with st.chat_message("assistant"):
        answer = yandex.get_answer(st.session_state.messages)
        answers = st.write(answer)
    # Add assistant yandex to chat history
    st.session_state.messages.append({"role": "assistant", "text": answer})