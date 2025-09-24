import streamlit as st
from yandexkey import YandexGPT


yandex = YandexGPT()

st.title("Сбор данных")

# если загружаем первый раз - создай пустой список пользователей
if 'users' not in st.session_state:
    st.session_state['users'] = []

# Поле ввода
# name = st.text_input("Введи имя")
# age = st.text_input("Введи возраст")
question = st.text_input('Введи вопрос')

users = st.session_state['users']

# # Кнопка "Сохранить"
button = st.button('Спросить')

if button:
    if question:
        text = yandex.get_answer(question)
        # users.append({'вопрос': question, 'ответ': text})
        st.markdown(text)
    else:
        st.warning('Неверные данные')
# st.write(users)