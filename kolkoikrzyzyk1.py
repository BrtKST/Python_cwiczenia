import tkinter as tk
from tkinter import messagebox

# Główne okno
okno = tk.Tk()
okno.title("Kółko i Krzyżyk")
okno.geometry("300x320")

# Zmienna śledząca gracza
gracz = "X"

# Plansza — 3x3 lista przycisków
przyciski = []

def sprawdz_wygrana():
    for i in range(3):
        # Wiersze
        if przyciski[i][0]["text"] == przyciski[i][1]["text"] == przyciski[i][2]["text"] != "":
            return True
        # Kolumny
        if przyciski[0][i]["text"] == przyciski[1][i]["text"] == przyciski[2][i]["text"] != "":
            return True
    # Przekątne
    if przyciski[0][0]["text"] == przyciski[1][1]["text"] == przyciski[2][2]["text"] != "":
        return True
    if przyciski[0][2]["text"] == przyciski[1][1]["text"] == przyciski[2][0]["text"] != "":
        return True
    return False

def ruch(x, y):
    global gracz
    if przyciski[x][y]["text"] == "":
        przyciski[x][y]["text"] = gracz
        if sprawdz_wygrana():
            messagebox.showinfo("Koniec gry", f"Wygrał gracz {gracz}!")
            okno.quit()
        else:
            # Zmiana gracza
            gracz = "O" if gracz == "X" else "X"

# Tworzenie siatki przycisków
for i in range(3):
    wiersz = []
    for j in range(3):
        b = tk.Button(okno, text="", font=("Arial", 24), width=5, height=2,
                      command=lambda x=i, y=j: ruch(x, y))
        b.grid(row=i, column=j)
        wiersz.append(b)
    przyciski.append(wiersz)

# Dodanie etykiety pod planszą (opcjonalnie)
info = tk.Label(okno, text="Gracz X zaczyna", font=("Arial", 12))
info.grid(row=3, column=0, columnspan=3)

okno.mainloop()
