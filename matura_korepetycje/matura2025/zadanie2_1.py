with open('C:\okienka\Python_cwiczenia\matura_korepetycje\matura2025\symbole_przyklad.txt', 'r') as file:
    lines = [line.strip() for line in file]
#print(lines)

#zadanie 2.1
palindrom = [line for line in lines if line == line[::-1]]
print(f'Odpowiedz do zadania pierwszego: {palindrom}')

#zadanie 2.2
counter = [0,0,0]
for l in range(0,int(len(lines))-2):
    for i in range(2,int(len(lines[l]))):
        if lines[l][i] == lines[l][i-1] == lines[l][i-2]:
            if lines[l+1][i] == lines[l+1][i-1] == lines[l+1][i-2] and lines[l+2][i] == lines[l+2][i-1] == lines[l+2][i-2]:
                counter[0] += 1
                if counter[0] <= 1:
                    counter[1] = (l + 1) + 1 # l+1 bo index pierwszy = 0, a liczymy rzedy od 1 oraz kolejne +1 bo szukamy srodka kwadratu
                    counter[2] = i  


print(counter)

