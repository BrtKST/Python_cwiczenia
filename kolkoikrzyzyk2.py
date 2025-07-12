import tkinter as tk 
from tkinter import messagebox

okno = tk.Tk()
okno.title('Moja gra - kolko i krzyzyk')
okno.geometry('300x320')

gracz = 'X'

plansza = []

def czy_wygrana():
    for i in range(3):
        if plansza[i][0]['text'] == plansza[i][1]['text'] == plansza[i][2]['text'] == gracz:
            return True
        if plansza[0][i]['text'] == plansza[1][i]['text'] == plansza[2][i]['text'] == gracz:
            return True
    return False

def ruch(x,y):
    global gracz
    if plansza[x][y]['text'] == "":
        plansza[x][y]['text'] = gracz
        if czy_wygrana():
            messagebox.showinfo(f'Koniec gry! Wygral gracz {gracz}!')
            okno.quit()
        else:
            gracz = "O" if gracz == "X" else "X"

for i in range(3):
    wiersz = []
    for j in range(3):
        button = tk.Button(okno, text ='', font = ('Arial',24),width=5,height=2, command=lambda x=i, y=j: ruch(x,y))
        button.grid(row=i, column=j)
        wiersz.append(button)
    plansza.append(wiersz)

okno.mainloop()