class Student:
    def __init__(self, name):
        self.name = name
        self.oceny = []
        self.ile = 3
        self.srednia = 0
        self.wprowadz_oceny()
    
    def wprowadz_oceny(self):
        i = 0
        while i < self.ile:
            ocenka = int(input('Podaj ocenę: '))
            self.oceny.append(ocenka)
            i += 1
        self.srednia = sum(self.oceny) / self.ile
        print(self.czy_zdal())  
    
    def czy_zdal(self):
        return f'Student {self.name} zdał, średnia: {self.srednia:.2f}' if self.srednia > 3.0 else f'Student {self.name} nie zdał, średnia: {self.srednia:.2f}'

    def __str__(self):
        return f'Student: {self.name}, Oceny: {self.oceny}, Średnia: {self.srednia:.2f}'

student = Student('Grzes')
print(student)
