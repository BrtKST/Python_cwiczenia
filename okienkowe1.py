from tkinter import *
from tkinter import ttk


'''
root = Tk()
frm = ttk.Frame(root,padding=10)
frm.grid()
ttk.Label(frm, text='Hello World!').grid(column=0, row=0)
ttk.Button(frm, text='Quit', command=root.destroy).grid(column=1, row=0)
root.mainloop()
'''

okno = Tk()
okno.title('TEST')
okno.geometry('300x200')
i=0

def przycisk_klikniety():
    global i
    i = i + 1
    if i % 2 != 0:
        etykieta.config(text = "TEST w Tkinter!")
    else:
        etykieta.config(text='Znikam')

etykieta = Label(okno, text = 'Kliknij mnie', font=("Arial", 14))
etykieta.pack(pady=20)

# Przycisk (button)
przycisk = Button(okno, text="Kliknij mnie", command=przycisk_klikniety)
przycisk.pack()

# Uruchomienie pętli głównej aplikacji
okno.mainloop()
