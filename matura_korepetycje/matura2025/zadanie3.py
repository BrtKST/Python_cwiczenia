with open('C:\okienka\Python_cwiczenia\matura_korepetycje\matura2025\dron_przyklad.txt', 'r') as file:
    lines =[line.rstrip() for line in file] #lista składana (list comprehension), konwertowanie string na int i usuwanie \n
    print(lines)
    lines = [(int(x), int(y)) for x,y in (line.split() for line in lines)]
print(lines)

#Zadanie 3.1 
#algorytm euklidesa - podmiana a = b oraz b = a%b dopóki b != 0

counter = 0
def nwd(a,b):
    while b != 0:
        a_pom = a
        a = b
        b = a_pom % b  #można to zapisać w jednej linijce a, b = b, a%b
    return a

for para in lines:
    if nwd(abs(para[0]),abs(para[1])) > 1:
        counter += 1
    
print(counter)

