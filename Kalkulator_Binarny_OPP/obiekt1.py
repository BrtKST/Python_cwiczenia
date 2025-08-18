class Student:
    count = 0
    total_gpa = 0

    def __init__(self,name,gpa):
        self.name = name 
        self.gpa = gpa 
        Student.count += 1
        #print('DODANO STUDENTA')
        Student.total_gpa += gpa
        
    
    def get_info(self):
        return f'{self.name} : {self.gpa}'
    
    @classmethod
    def get_count(cls):
        return f'Total number of student: {cls.count}'

    @classmethod    
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return cls.total_gpa/cls.count
    
student = Student('Pawel', 3.2)
student2 = Student('Grzes', 4.1)
print(student.get_count())
print(student2.get_average_gpa())