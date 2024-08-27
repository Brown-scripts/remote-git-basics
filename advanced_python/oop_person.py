class Person:
    def __init__(self,name:str,dob:str,age:int):
        self.name=name
        self.dob=dob
        self.age=age
    def speaks(self):
        print('hello')
    def walk(self):
        return 'walking away...'
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age

person1=Person('Nicole','30-05-2003',21) 
print(person1.get_name())
print(person1.get_age())
print(person1.walk())


class Student(Person):
    def __init__(self,name,dob,age,courses=[]):
        super().__init__(name,dob,age)
        self.courses=courses
    def speak(self):
        return "I'm so tired!"
    def get_courses(self):
        return self.courses
    
student1= Student('Nicole','30-05-2003',21,['Maths','Science','Creative Arts'])
print(student1.get_name())
print(student1.speak())
print(student1.dob)
print(student1.get_courses())


