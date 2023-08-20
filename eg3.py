class Person:
    def __init__(self, name, age, gpa, *kw):
      self.name = name
      self.age = age
      self.gpa = gpa
    def myfuncition(self):
       print("Hello everyone, my name is : ", self.name)
       if self.age > 18 : print("He is a adult")
       else : print("He is a child")
       if self.gpa >= 3.2 : print("he studies very well")
       else : print("He needs to study harder")
pass

x = Person("Doan Duc Thang", 21, 3.2)
x.myfuncition()

