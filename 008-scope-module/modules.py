
print("============== Python Modules ===================")

print("-------- Create a Module --------")

#mymodule.py

#def greeting(name):
#  print("Hello, " + name)

print("-------- Use a Module --------")

import mymodule

mymodule.greeting("Jonathan")

print("-------- Variables in Module --------")

#mymodule.py

#person1 = {
#  "name": "John",
#  "age": 36,
#  "country": "Norway"
#}

import mymodule

a = mymodule.person1["age"]
print(a)

print("-------- Re-naming a Module --------")

import mymodule as mx

a = mx.person1["age"]
print(a)

print("-------- Built-in Modules --------")

import platform

x = platform.system()
print(x)

print("-------- Using the dir() Function --------")

import platform

x = dir(platform)

print(x)

print("-------- Import From Module --------")

from mymodule import person1

print (person1["age"])

def main ():
  print("main")
 
if __name__ == '__main__':
    main()