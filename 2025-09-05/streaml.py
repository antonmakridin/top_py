import streamlit as st
from yandex import YandexGPT
token = 'AQVNwEo4xD0mPA7lXzS4sCGLHp3K8uenS6I9eho5'
catalog = 'b1goak37d5prthkdfd7n'

yandex = YandexGPT(token, catalog)

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