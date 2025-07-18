with open('C:\okienka\Python_cwiczenia\matura_korepetycje\matura2025\symbole.txt', 'r') as file:
    lines = [line.strip() for line in file]
#print(lines)

#zadanie 2.1
palindrom = [line for line in lines if line == line[::-1]]
print(f'Odpowiedz do zadania pierwszego: {palindrom}')

#zadanie 2.2
results = []

for l in range(len(lines) - 2):
    for i in range(2, len(lines[l])):
        # sprawdzanie czy 3 w rzedzie znaki sa takie same, potem rzedy ponizej
        if lines[l][i] == lines[l][i-1] == lines[l][i-2]:
            if (lines[l+1][i] == lines[l+1][i-1] == lines[l+1][i-2] == lines[l][i] and
                lines[l+2][i] == lines[l+2][i-1] == lines[l+2][i-2] == lines[l][i]):
                # środek kwadratu: rząd l+1 (jeszcze dodatkowe +1 ze względu na indeksowanie od 0), kolumna i-1 (licząc od 1)
                results.append((l + 1 + 1, i))

print(len(results))
for rzad, kolumna in results:
    print(rzad, kolumna)

