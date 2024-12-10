from txt import Person

class Student(Person):
    def __init__(self,name,phone,age):
        super().__init__(name,phone)
        self.age=age
    def info(self):
        return f"Name: {self.name} Phone: {self.phone} Age: {self.age}"

st=Student("Aziz",902040737,19)