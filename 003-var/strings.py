
print("============== Python Strings ===================")

print("-------- Strings --------")

print("Hello")
print('Hello')

print("-------- Assign String to a Variable --------")

a = "Hello"
print(a)

print("-------- Multiline Strings --------")

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

print(a)

print("-------- Strings are Arrays --------")

a = "Hello, World!"
print(a[1])

print("-------- Looping Through a String --------")

for x in "banana":
  print(x)

print("-------- String Length --------")

a = "Hello, World!"
print(len(a))

print("-------- Check String --------")

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

print("-------- Check if NOT --------")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

print("============== Python - Slicing Strings ===================")

print("-------- Slicing --------")

b = "Hello, World!"
print(b[2:5])

print("-------- Slice From the Start --------")

b = "Hello, World!"
print(b[:5])

print("-------- Slice To the End --------")

b = "Hello, World!"
print(b[2:])

print("-------- Negative Indexing --------")

b = "Hello, World!"
print(b[-5:-2])

print("============== Python - Modify Strings ===================")

print("-------- Upper Case --------")

a = "Hello, World!"
print(a.upper())

print("-------- Lower Case --------")

a = "Hello, World!"
print(a.lower())

print("-------- Remove Whitespace --------")

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

print("-------- Replace String --------")

a = "Hello, World!"
print(a.replace("H", "J"))

print("-------- Split String --------")

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

print("============== Python - String Concatenation ===================")

print("-------- String Concatenation --------")

a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

print("============== Python - Format - Strings ===================")

print("-------- String Format --------")

#age = 36
#txt = "My name is John, I am " + age   #error
#print(txt)

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

print("============== Python - Escape Characters ===================")

print("-------- Escape Character --------")

txt = "We are the so-called \"Vikings\" from the north."

print(txt)

print("\'  Single Quote")
print("\\  Backslash")  
print("\n  New Line")
print("\r  Carriage Return")
print("\t  Tab")
print("\b  Backspace") 
print("\f  Form Feed")
print("\110\145\154\154\157    Octal value")
print("\x48\x65\x6c\x6c\x6f    Hex value")
