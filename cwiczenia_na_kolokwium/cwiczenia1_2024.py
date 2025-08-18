#zadanie 1
'''
liczby = [int(input(f'Podaj {i+1} liczbę: ')) for i in range(0,5)]
print(sum(liczby), max(liczby), min(liczby), max(liczby)-min(liczby))
'''
#zadanie 2
lista = [1,2,2,3,4,4,5]
new_lista = list(set(lista))
print(new_lista)

#zadanie 3
ile = int(input('Podaj ile liczb pierwszych: '))
lista =[]
liczba = 2
while int(len(lista)) < ile:
    for x in range(2, int(liczba**0.5)+1):
        if liczba % x == 0:
            break 
    else:   
        lista.append(liczba)
    liczba += 1
    
print(lista)

#zadanie 4
with open('liczby.txt', 'r') as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]
    lines.sort()

file.close()
print(lines)

if len(lines) % 2 == 0:
    mediana = (lines[int(len(lines))//2] + lines[int((len(lines))//2) - 1]) /2
else:
    mediana = lines[int((len(lines))//2) - 1]

print('Mediana = {}'.format(mediana))