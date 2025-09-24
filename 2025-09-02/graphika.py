from tkinter import *
from tkinter import ttk
from yandexkey import YandexGPT

yandex = YandexGPT()


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()


question = StringVar()
lang = StringVar()

def get_answer():
    t.delete('1.0', END)
    text = yandex.get_answer(question.get(), lang.get()) + '\n'
    t.insert(END, text)
    question.set('')
    lang.set('')


Label(frm, text="Введи текст для перевода").grid(column=0, row=0)
user_input = Entry(frm, textvariable=question)
user_input.grid(column=0, row=1)

Label(frm, text="Введи язык для перевода").grid(column=0, row=2)
user_input_l = Entry(frm, textvariable=lang)
user_input_l.grid(column=0, row=3)

user_input.bind("<Return>", lambda event: get_answer())
button = Button(frm, text="Сделать запрос", command=get_answer)
button.grid(column=0, row=4)
Label(frm, text="  ").grid(column=1, rowspan=4)



t = Text(frm, width=50, height=15)
t.grid(column=2, row=0, rowspan=5)


root.mainloop()