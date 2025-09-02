from tkinter import *
from tkinter import ttk
from yandex import YandexGPT

token = 'AQVNwEo4xD0mPA7lXzS4sCGLHp3K8uenS6I9eho5'
catalog = 'b1goak37d5prthkdfd7n'

yandex = YandexGPT(token, catalog)


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()


question = StringVar()

def get_answer():
    t.delete('1.0', END)
    text = yandex.get_answer(question.get()) + '\n'
    t.insert(END, text)
    question.set('')


Label(frm, text="Введи запрос").grid(column=0, row=0)
user_input = Entry(frm, textvariable=question)
user_input.grid(column=0, row=1)
user_input.bind("<Return>", lambda event: get_answer())
button = Button(frm, text="Сделать запрос", command=get_answer)
button.grid(column=0, row=2)
Label(frm, text="  ").grid(column=1, row=0)



t = Text(frm, width=50, height=15)
t.grid(column=2, row=0, rowspan=3)


root.mainloop()