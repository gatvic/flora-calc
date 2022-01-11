import tkinter as tk
# from tkinter import messagebox
from tkinter import ttk

window = tk.Tk()
window.title('Калькулятор удобрений')
window.geometry('400x300+300+250')

n = str(0)
p = str(0)
k = str(0)
ca = str(0)
mg = str(0)

frame_top = tk.LabelFrame(text='NPK состав')

label_1 = tk.Label(frame_top, width=7, height=4, bg='green', text=f'N = {n}')

label_2 = tk.Label(frame_top, width=7, height=4, bg='orange', text=f'P = {p}')

label_3 = tk.Label(frame_top, width=7, height=4, bg='red', text=f'K = {k}')

label_4 = tk.Label(frame_top, width=7, height=4, bg='grey', text=f'Ca = {ca}')

label_5 = tk.Label(frame_top, width=7, height=4, bg='purple', text=f'Mg = {mg}')


culture = ''
frame_npk = tk.LabelFrame(text=f'NPK формула для культуры {culture}')

label_6 = tk.Label(frame_npk, width=7, height=4, bg='green', text=f'N = {n}')

label_7 = tk.Label(frame_npk, width=7, height=4, bg='orange', text=f'P = {p}')

label_8 = tk.Label(frame_npk, width=7, height=4, bg='red', text=f'K = {k}')

label_9 = tk.Label(frame_npk, width=7, height=4, bg='grey', text=f'Ca = {ca}')

label_10 = tk.Label(frame_npk, width=7, height=4, bg='purple', text=f'Mg = {mg}')


window.mainloop()
