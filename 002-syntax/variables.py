
print("============== Python Variables ===================")

print("-------- Creating Variables --------")

x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

print("-------- Casting --------")

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)

print("-------- Get the Type --------")

x = 5
y = "John"
print(type(x))
print(type(y))

print("-------- Single or Double Quotes --------")

x = "John"
print(x)

# is the same as
x = 'John'
print(x)

print("-------- Case-Sensitive --------")

a = 4
A = "Sally"
#A will not overwrite a

print(a)
print(A)

print("============== Python - Variable Names ===================")

print("-------- Multi Words Variable Names --------")

print("Camel Case :: ", "myVariableName = 'John'");

print("Pascal Case :: ", "MyVariableName = 'John'");

print("Snake Case :: ", "my_variable_name = 'John'");

print("============== Python Variables - Assign Multiple Values ===================")

print("-------- Many Values to Multiple Variables --------")

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

print("-------- One Value to Multiple Variables --------")

x = y = z = "Orange"
print(x)
print(y)
print(z)

print("-------- Unpack a Collection --------")

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

print("============== Python - Output Variables ===================")

print("-------- Output Variables --------")

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
#print(x + y)   #error

x = 5
y = "John"
print(x, y)

print("============== Python - Global Variables ===================")

print("-------- Global Variables --------")

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

print("-------- The global Keyword --------")

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)