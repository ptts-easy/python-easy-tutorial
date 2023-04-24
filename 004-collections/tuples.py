
print("============== Python Tuples ===================")

print("-------- Tuple --------")

thistuple = ("apple", "banana", "cherry")
print(thistuple)

print("-------- Allow Duplicates --------")

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

print("-------- Tuple Length --------")

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

print("-------- Create Tuple With One Item --------")

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

print("-------- Tuple Items - Data Types --------")

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

tuple1 = ("abc", 34, True, 40, "male")

print(tuple1)

print("-------- type() --------")

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

print("-------- The tuple() Constructor --------")

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

print("============== Python - Access Tuple Items ===================")

print("-------- Access Tuple Items --------")

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

print("-------- Negative Indexing --------")

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

print("-------- Range of Indexes --------")

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

print("-------- Range of Negative Indexes --------")

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

print("-------- Check if Item Exists --------")

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

print("============== Python - Update Tuples ===================")

print("-------- Change Tuple Values --------")

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

print("-------- Add Items --------")

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

print("-------- Remove Items --------")

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)

thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists

print("============== Python - Unpack Tuples ===================")

print("-------- Unpacking a Tuple --------")

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

print("-------- Using Asterisk* --------")

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

print("============== Python - Loop Tuples ===================")

print("-------- Loop Through a Tuple --------")

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

print("-------- Loop Through the Index Numbers --------")

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

print("-------- Using a While Loop --------")

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

print("============== Python - Join Tuples ===================")

print("-------- Join Two Tuples --------")

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

print("-------- Multiply Tuples --------")

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
