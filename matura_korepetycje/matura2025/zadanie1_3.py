'''
r = n % 100
a = r / 10
b =  r % 10
n = n / 100
'''

def przestaw(n):
    wynik = 0
    mnoznik = 1
    #rozpisując wzor widzimy, ze za kazdym razem nowa pare skladajaca sie z a i b
    #mnozymy razy 100, pierwszy mnoznik = 1
    while n > 0:
        r = n % 100
        a = r // 10
        b = r % 10
        n = n // 100

        if a > 0:
            nowa_para = a +10 * b
        else:
            nowa_para = b
        wynik += nowa_para * mnoznik
        mnoznik *= 100
    return wynik
    

print(przestaw(316498))