
print("============== Python Classes and Objects ===================")

print("-------- Create a Class --------")

class MyClass:
  x = 5

print("-------- Create Object --------")

p1 = MyClass()
print(p1.x)

print("-------- The __init__() Function --------")

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

print("-------- The __str__() Function --------")

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

print("-------- Object Methods --------")

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

print("-------- The self Parameter --------")

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

print("-------- Modify Object Properties --------")

p1.age = 40

print(p1)

print("-------- Delete Object Properties --------")

del p1.age

print("-------- Delete Objects --------")

del p1

print("-------- The pass Statement --------")

class Person:
  pass
