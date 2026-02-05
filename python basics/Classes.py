class Employee:      
    name = "John"        
    age = 26

emp = Employee()        
type(emp)               


class Employee:            
    name = "Sana"          
    age = 26

    def hello(self):    
      print("Hello")

emp = Employee()           
emp.hello()                

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    def details(self):
        print("Employee Name: ",  self.name)
        print("Employee Age: ", self.age)
 

emp1 = Employee("John", 26)      
emp2 = Employee("Jane", 24)         

emp1.details()
emp2.details()


class Student:
    def __init__(self, name):
        self.name = name        
        
    def intro(self):
        print('Hi I am', self.name)

    def change_name(self, name):
        self.name = name

john = Student('john')

# access method
john.intro()

# access attribute
print(john.name)

# change name
john.change_name('JJOOHHNN')
john.intro()



class Rectangle:
    def __init__(self, length, width ):
        self.length = length
        self.width = width
    def area(self):
        print(f"Length - {self.length}, Width - {self.width}")
        return self.length * self.width

first = Rectangle(5,2)
print(first.area())

class Dog:
  def __init__(self, breed, age, color):
    self.breed = breed
    self.age = age
    self.color = color
  def details(self):
    print(f"Breed - {self.breed}, Age - {self.age}, Color - {self.color} ")

dog1 = Dog('Husky', 5, 'Blank')

dog1.details()

