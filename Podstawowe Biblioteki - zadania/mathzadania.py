#Oto zestaw podstawowych zadań prezentujących i pozwalających 
#zapoznać się z możliwościami biblioteki math

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
# logarytm naturalny z 10 (math.log) zaokrąglony do 5 miejsc po przecinku,
# logarytm dziesiętny z 1000 (math.log10).

potega = math.pow(2,10)
log_nat = math.log(10)
log_dzies = math.log10(1000)
print(f'Potega: {potega}, logarytm nat: {round(log_nat,5)}, logarytm dziesietny: {log_dzies}')

#4. Pole koła Napisz funkcję, która przyjmuje promień koła 
# i zwraca jego pole (użyj math.pi).
r = float(input('Podaj promien kola: '))
pole = math.pi * (r ** 2)
print("Pole kola o promieniu {} wynosi : {}".format(r, round(pole,2)))

#5. Odległość między punktami
#Mając punkty A i B oblicz ich odległość w układzie współrzędnych (użyj math.sqrt).

A = [10,2]
B = [3, 4]
odl = math.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)
print(f'Odleglosc wynosi {odl:.2f}')