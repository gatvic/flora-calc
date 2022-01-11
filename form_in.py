from tkinter import *

from tkinter import ttk

window = Tk()
window.title('Калькулятор удобрений')
window.geometry('400x300+300+250')

n = str(0)
p = str(0)
k = str(0)
ca = str(0)
mg = str(0)

frame_top = LabelFrame(text='NPK состав')
frame_top.pack()
label_1 = Label(frame_top, width=7, height=4, bg='green', text=f'N = {n}')
label_1.pack(side=LEFT)
label_2 = Label(frame_top, width=7, height=4, bg='orange', text=f'P = {p}')
label_2.pack(side=LEFT)
label_3 = Label(frame_top, width=7, height=4, bg='red', text=f'K = {k}')
label_3.pack(side=LEFT)
label_4 = Label(frame_top, width=7, height=4, bg='grey', text=f'Ca = {ca}')
label_4.pack(side=LEFT)
label_5 = Label(frame_top, width=7, height=4, bg='purple', text=f'Mg = {mg}')
label_5.pack(side=LEFT)


def callbackFunc(event):
    return event


labelTop = Label(window, text='Выбор растения')
labelTop.pack()
comboEx = ttk.Combobox(window, values=['Перец', 'Клубника', 'Томат'])
# pprint(dict(comboEx))
comboEx.pack()
comboEx.current(0)
comboEx.bind('Select', callbackFunc)


# print(comboEx.current(), comboEx.get())
florarium = {'Перец': ['220', '50', '200', '170', '50'],
             'Клубника': ['120', '45', '100', '200', '50'],
             'Томат': ['300', '120', '150', '420', '60']}

culture = ''
frame_npk = LabelFrame(text=f'NPK формула для культуры {culture}')
frame_npk.pack(side=TOP)
label_6 = Label(frame_npk, width=7, height=4, bg='green', text=f'N = {n}')
label_6.pack(side=LEFT)
label_7 = Label(frame_npk, width=7, height=4, bg='orange', text=f'P = {p}')
label_7.pack(side=LEFT)
label_8 = Label(frame_npk, width=7, height=4, bg='red', text=f'K = {k}')
label_8.pack(side=LEFT)
label_9 = Label(frame_npk, width=7, height=4, bg='grey', text=f'Ca = {ca}')
label_9.pack(side=LEFT)
label_10 = Label(frame_npk, width=7, height=4, bg='purple', text=f'Mg = {mg}')
label_10.pack(side=LEFT)

window.mainloop()
