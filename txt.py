class Person:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
    def info(self):
        return f"Name: {self.name} Phone: {self.phone} "

pers=Person("Aziz",902040737)
print(pers.info())