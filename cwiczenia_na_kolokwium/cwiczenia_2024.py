'''
#Zadanie 1

lista = [int(input(f'Podaj liczbe {i+1}: ')) for i in range(0,5)]
print(sum(lista), max(lista), min(lista), max(lista)-min(lista))

#Zadanie 2

lista = [1,3,3,4,5,1,1,2,3,9,2]
new_list = list(set(lista[::1]))
print(new_list)

#Zadanie 3
ile_pierwszych = int(input('Ile liczb pierwszych:'))
pierwsze =list()
liczba = 2

while len(pierwsze) < ile_pierwszych:
    for x in range(2, int(liczba**0.5)+1):
        if liczba % x == 0:
            break
    else:
        pierwsze.append(liczba)
    liczba += 1
print("Liczby pierwsze:", pierwsze)
'''

#Zadanie 4
with open('liczby.txt','r') as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]
    lines.sort()
print(lines)

if len(lines) % 2 != 0:
    print(f'Mediana = {lines[(int(int(len(lines))/2)) - 1]}')
else:
    mediana = (lines[(int(int(len(lines))/2))]+lines[(int(int(len(lines))/2))-1])/2
    print(f'Mediana = {mediana}')