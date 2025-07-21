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
