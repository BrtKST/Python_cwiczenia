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
            

        
