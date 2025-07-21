
list_n = [33658, 542102, 87654321012345678]

def cyfry(n):
    b = 1
    c = 0
    counter = 0
    while n > 0:
        a = n % 10
        n = n // 10
        if a % 2 == 0:
            c = c + b * (a // 2)
        else:
            c = c + b
            counter += 1
        b = b * 10
        print(b)
    return c, counter

for element in list_n:
    c, counter = cyfry(int(element))
    print('c = {}, liczba instrukcji: {}'.format(c,counter))


'''
Analiza kodu
Kod wykonuje się dopóki wartość n, czyli nasza liczba jest większa od 0,
mamy zmienne a, b, c, gdzie:
- a - wartość aktualnej liczby mod 10, czyli reszta z dzielenia przez 10
(czyli ostatnia cyfra naszej liczby)
- b - początkowo przyjmuje watość 1 i co iterację (kolejne przejście) zwiększa
swoją wartość o kolejną wielokrotność 10, liczba zer w liczbie b odpowiada
ilości cyfr w początkowej liczbie n
- c - zależnie od tego czy liczba jest parzysta przyjmuje dwa wzory,
w przypadku liczby nieparzystej do c dodajemy po prostu b, czyli
po każdej iteracji do naszego ciągu c na kolejnym miejscu dodajemy 1,
natomiast dla liczby nieparzystej dodajemy cyfrę równą połowie analizowanej
cyfry, czyli dla n= 33658, jak trafimy na 8, to dzielimy ją przez 2 i dodajemy 
w tym przypadku akurat na ostatnią pozycję

Analiza dla n = 87654321012345678
c = 4,1,3,1,2,1,1,1,0,1,1,2,1,3,1,4


'''