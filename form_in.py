from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Калькулятор удобрений')
window.geometry('400x300+300+250')

frame_top = LabelFrame(text='NPK состав')
frame_top.pack()
label_1 = Label(frame_top, width=7, height=4, bg='green', text='N')
label_1.pack(side=LEFT)
label_2 = Label(frame_top, width=7, height=4, bg='orange', text='P')
label_2.pack(side=LEFT)
label_3 = Label(frame_top, width=7, height=4, bg='red', text='K')
label_3.pack(side=LEFT)
label_4 = Label(frame_top, width=7, height=4, bg='grey', text='Ca')
label_4.pack(side=LEFT)
label_5 = Label(frame_top, width=7, height=4, bg='purple', text='Mg')
label_5.pack(side=LEFT)



window.mainloop()
