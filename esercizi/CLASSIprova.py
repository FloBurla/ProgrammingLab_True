import random

class Person():
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
    def __str__(self):
        return('This guy is called "{} {}"'.format(person.name,person.surname))

    def say_hi(self):
        random_number=random.randint(0,2)
        if random_number==0:
            print("Hi,i'm {}".format(self.name))
        if random_number==1:
            print("What are you doing in my house?")
        if random_number==2:
            print("{} {}, at your Service".format(self.name,self.surname))

class Student(Person):
    def __str__(self):
        return('Student {} {}'.format(self.name,self.surname))

class Professor(Person):
    def __str__(self):
        return('Professor {} {}'.format(self.name,self.surname))
    def say_hi(self):
        print("Hi, I'm professor {} {}".format(self.name,self.surname))
        
student=Student('Giulio','Caravagna')
print(student)
student.say_hi()

print('----------------------------------------')

professor=Professor('Marco','Montemagno')
print(professor)
professor.say_hi()