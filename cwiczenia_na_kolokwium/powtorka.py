#zadanie 1

liczby = [int(input('Podaj liczbe calkowita: ')) for i in range(5)]
print(sum(liczby),max(liczby),min(liczby),max(liczby)-min(liczby))

#zadanie 2
lista2 = [1,2,3,3,1,4,3,2,5]
new_list = [element for element in lista2 if lista2.count(element) == 1]
print(new_list)

#zadanie 3
