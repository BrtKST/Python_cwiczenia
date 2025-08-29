#zadanie 1 - Counter 
'''Napisz funkcję, która przyjmuje napis i zwraca 3 najczęściej występujące 
litery wraz z ich licznością.'''
import collections

string_1 = 'ala ma kota i kot ma ale'
zliczanie = collections.Counter(string_1)
#jeżeli tylko litery to:
#zliczanie - collections.Counter(char for char in string_1 if char.isalpha())
print(type(zliczanie))
print(zliczanie.most_common(3))


#zadanie 2 - defaultdict
'''Masz listę krotek (klucz, wartość). Zbuduj słownik, gdzie klucze 
odpowiadają wszystkim unikalnym kluczom z listy, a wartości to lista 
przypisanych im elementów.'''

krotka_2 = [('pies',1),('kot',2),('kot',3),('pies',1)]
dict_2 = collections.defaultdict(list)
for k, v in krotka_2:
    dict_2[k].append(v)
print(dict_2)

#zadanie 3 - deque
'''Zaimplementuj kolejkę o maksymalnym rozmiarze n. Jeśli do kolejki zostanie 
dodany nowy element, a jest już pełna, usuń najstarszy.'''

n = 3
kolejka = collections.deque(maxlen=3)
kolejka.append(2)
kolejka.append(1)
kolejka.append(0)
print(kolejka)
kolejka.append(-1) #automatycznie usunie się najstarszy (kolejka FIFO)
print(kolejka)

#zadanie 4 - namedtuple
'''Zdefiniuj strukturę Punkt z polami x i y. Następnie napisz funkcję, 
która oblicza odległość euklidesową pomiędzy dwoma punktami.'''

import math
Punkt = collections.namedtuple('Punkt', ["x","y"])
Punkt1 = Punkt(1,2)
Punkt2 = Punkt(3,2)


def odleglosc(p1, p2):
    return round(((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5,2)
    #jezeli zaimportujemy biblioteke math to:
    #return round(math.dist((p1.x, p1.y), (p2.x, p2.y)), 2)
print(odleglosc(Punkt1, Punkt2))


#zadanie 5 - OrderedDict
'''Dane są pary (klucz, wartość). Zbuduj słownik uporządkowany według momentu 
pierwszego wystąpienia klucza, a jeśli klucz się powtórzy to zignoruj go.'''

dane = [("a", 1), ("b", 2), ("a", 3), ("c", 4)]
#slownik_5 = collections.OrderedDict(set(dane)) !!!SET gubi kolejność elementów!!!
slownik_5 = collections.OrderedDict()
for k,v in dane:
    if k not in slownik_5:
        slownik_5[k] = v
print(slownik_5)