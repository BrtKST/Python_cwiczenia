import math
#1. Pierwiastek kwadratowy
#Napisz program, który wczyta liczbę od użytkownika 
# i wypisze jej pierwiastek kwadratowy (użyj math.sqrt).

liczba = int(input('Podaj liczbe: '))
print(math.sqrt(liczba))

#2. Zaokrąglanie w dół i w górę
# Wczytaj liczbę zmiennoprzecinkową i wypisz jej:
# zaokrąglenie w dół (math.floor)
# zaokrąglenie w górę (math.ceil)

liczba_float = float(input('Podaj liczbe do zaokraglenia: '))
print(f'''Zaokraglenie w dol: {math.floor(liczba_float)}
Zaokraglenie w gore: {math.ceil(liczba_float)}''')

#3. Potęgi i logarytmy Oblicz 2^10: za pomocą math.pow,
# logarytm naturalny z 10 (math.log),
# logarytm dziesiętny z 1000 (math.log10).