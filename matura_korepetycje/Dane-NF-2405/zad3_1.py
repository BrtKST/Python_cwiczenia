#zadanie 3.1.

def skrot(x):
    b = 1
    c = 0
    while x > 0:
        if x % 2 == 1:
            c = c + ((x % 10) * b)
            b *= 10
        else:
            pass
        x = x // 10
        
    print(f'Skrot = {c}')

przyklad = [294762, 39101, 224]

for liczba in przyklad:
    skrot(liczba)
            
#Zadanie 3.2.
with open('C:\okienka\Python_cwiczenia\matura_korepetycje\Dane-NF-2405\skrot.txt', 'r') as file:
    lines = file.readlines()
print(lines)
lines = [line.rstrip('\n') for line in lines]
print(lines)
file.close()

#szukamy ile jest liczb dla których nie istnieje nieparzysty skrót oraz należy podać
# największą z nich
def skrot_ret(x):
    b = 1
    c = 0
    x = int(x)
    while x > 0:
        if x % 2 == 1:
            c = c + ((x % 10) * b)
            b *= 10
        else:
            pass
        x = x // 10
        
    return c

maximum = 0
counter = 0

for element in lines:
    value = skrot_ret(element)
    if value == 0:
        counter += 1
        if int(element) > int(maximum):
            maximum = element

print(f'Największy skrót: {maximum}. W sumie w pliku wystepuje {counter} skrótów, które nie mają nieparzystego skrótu.')

#zadanie 3.3.

with open('C:\okienka\Python_cwiczenia\matura_korepetycje\Dane-NF-2405\skrot2.txt', 'r') as file1:
    lines1 = file1.readlines()
print(lines1)
lines1 = [line.rstrip('\n') for line in lines1]
print(lines1)
file1.close()

def wspolny_dzielnik(a,b):
    while b != 0:
        a, b = b, a % b
    return a

new_list = list()
for element in lines1:
    value = skrot_ret(element)
    if wspolny_dzielnik(int(value),int(element)) == 7:
        new_list.append(element)

print('Liczby i skróty, których NWD = 7:')
for element in new_list:
    print(element)