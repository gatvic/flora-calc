from tkinter import *
# from tkinter.messagebox import showinfo
from tkinter.ttk import Combobox

window = Tk()
window.title('NPK формула культуры')
window.geometry('400x300+500+250')

plants = ['Перец', 'Клубника', 'Томат']

labelTop = Label(window, text='Выбор растения')
labelTop.pack()
selected_plants = StringVar()
comboEx = Combobox(window, textvariable=selected_plants)
comboEx['values'] = plants
comboEx['state'] = 'readonly'
# comboEx.current(1)
plant = ''


def callbackFunc(event):
    global plant
    plant = event.widget.get()
    print(plant)


comboEx.bind('<<ComboboxSelected>>', callbackFunc)
comboEx.pack()

print(comboEx.current(), comboEx.get())
florarium = {'Перец': ['220', '50', '200', '170', '50'],
             'Клубника': ['120', '45', '100', '200', '50'],
             'Томат': ['300', '120', '150', '420', '60']}

color = ['green', 'orange', 'red', 'grey', 'purple']
el = ['N', 'P', 'K', 'Ca', 'Mg']
el_q = ['0', '0', '0', '0', '0']

frame_npk = LabelFrame(text=f'NPK формула для культуры ')
# cur_plant =
l_p = Label(frame_npk, width=7,
            height=4, bg='grey',
            textvariable=selected_plants)
l_p.pack(side=LEFT)
frame_npk.pack(side=TOP)

for i in range(5):
    a = Label(frame_npk, width=7,
              height=4, bg=color[i],
              text=f'{el[i]} = {el_q[i]}',
              )
    a.pack(side=LEFT)

window.mainloop()
