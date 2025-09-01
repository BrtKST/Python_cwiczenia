#Zad. 1.
'''
Napisz program w języku Python (≥ 3.6), który:
a) utworzy obiekt własnej klasy,
b) obiekt przyjmuje w konstruktorze liczbę całkowitą,
c) obiekt posiada metodę zwracającą wartość pierwiastka kwadratowego tej liczby (użyj math.sqrt).

Uwaga 1.1. Program nie może być dłuższy niż 6 linii kodu, a definicja klasy – więcej niż 3 linie kodu.
'''

import math 

class Obiekt:
    def __init__(self,liczba): self.liczba = int(liczba)
    def pierwiastek(self): return math.sqrt(self.liczba)

liczba1 = Obiekt(4)
print(liczba1.pierwiastek())

#Zad. 2.
'''
Napisz funkcję, która przyjmuje ścieżkę folderu (string) 
i zwraca listę wszystkich plików w tym folderze (użyj modułu os).
'''
import os
def zwroc(path): return os.listdir(path)

pliki = zwroc('.')
print(pliki)

#Zad. 3.
'''
Napisz funkcję, która przyjmuje słownik w formacie JSON (string) 
i zwraca listę wszystkich kluczy zagnieżdżonych na pierwszym poziomie 
(użyj modułu json).'''

import json
slownik3 = '{"a":1,"b":2,"c":3}'
def slowniki(x):
    return([json.loads(x).keys()])
print(f'Klucze ze slownika: {slowniki(slownik3)}')

#Zad. 4.
'''
Napisz funkcję, która przyjmuje listę słów i zwraca obiekt 
Counter z biblioteki collections, zliczający wystąpienia poszczególnych słów.
Napisz drugą funckję, która zwraca najpopularniejszy element.
'''

import collections
lista = ['jabłko','banan','banan','mandarynka','banan','jabłko']

def licznik(x):
    return collections.Counter(x)
print(licznik(lista))

def najpopulrniejsza(x):
    return collections.Counter.most_common(x)[0]
print(najpopulrniejsza(licznik(lista)))