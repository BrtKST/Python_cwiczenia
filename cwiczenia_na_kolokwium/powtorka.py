#zadanie 1

liczby = [int(input('Podaj liczbe calkowita: ')) for i in range(5)]
print(sum(liczby),max(liczby),min(liczby),max(liczby)-min(liczby))

#zadanie 2
lista2 = [1,2,3,3,1,4,3,2,5]
new_list = [element for element in lista2 if lista2.count(element) == 1]
print(new_list)

#zadanie 3

n = int(input('Podaj liczbe calkowita: '))

def czy_pierwsza(x):
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
def pierwsze(n):
    lista3 = []
    if n == 0:
        return f'Zly zakres'
    elif n == 1:
        lista3.append(2)
        return lista3
    elif n>1:
        i = 3
        lista3.append(2)
        while len(lista3) < n:
            if czy_pierwsza(i):
                lista3.append(i)
            i += 1
        return lista3
print(pierwsze(n))

#zadanie 3 - 2 wersja
n1 = int(input('Podaj liczbe calkowita: '))

def czy_pierwsza1(x):
    return x>1 and all(x % i for i in range(2,int(x**0.5)+1))
def pierwsze1(n):
    lista3_1 = []
    while len(lista3_1) < n:
        i = 2
        if czy_pierwsza1(i): lista3_1.append(i)
        i+=1
print(pierwsze(n1))