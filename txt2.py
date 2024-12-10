from txt1 import Student

class Student2(Student):
    def __init__(self,name,phone,age,location):
        super().__init__(name,phone,age)
        self.location=location
    def info(self):
        return f"Name: {self.name} Phone: {self.phone} Age: {self.age} Location: {self.location}"

st=Student2("Aziz",902040737,19,"Andijan")