
print("============== Python Lists ===================")

print("-------- List --------")

thislist = ["apple", "banana", "cherry"]
print(thislist)

print("-------- Allow Duplicates --------")

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

print("-------- List Length --------")

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

print("-------- List Items - Data Types --------")

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

list1 = ["abc", 34, True, 40, "male"]

print(list1)

print("-------- type() --------")

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

print("-------- The list() Constructor --------")

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

print("============== Python - Access List Items ===================")

print("-------- Access Items --------")

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

print("-------- Negative Indexing --------")

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

print("-------- Range of Indexes --------")

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

print("-------- Range of Negative Indexes --------")

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

print("-------- Check if Item Exists --------")

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

print("============== Python - Change List Items ===================")

print("-------- Change Item Value --------")

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

print("-------- Change a Range of Item Values --------")

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

print("-------- Insert Items --------")

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

print("============== Python - Add List Items ===================")

print("-------- Append Items --------")

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

print("-------- Insert Items --------")

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

print("-------- Extend List --------")

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

print("-------- Add Any Iterable --------")

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

print("============== Python - Remove List Items ===================")

print("-------- Remove Specified Item --------")

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

print("-------- Remove Specified Index --------")

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist
#print(thislist)

print("-------- Clear the List --------")

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

print("============== Python - Loop Lists ===================")

print("-------- Loop Through a List --------")

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

print("-------- Loop Through the Index Numbers --------")

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

print("-------- Using a While Loop --------")

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

print("-------- Looping Using List Comprehension --------")

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

print("============== Python - List Comprehension ===================")

print("-------- List Comprehension --------")

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

print("-------- Condition --------")

newlist = [x for x in fruits if x != "apple"]

print(newlist)

print("-------- Iterable --------")

newlist = [x for x in range(10)]

print(newlist)

newlist = [x for x in range(10) if x < 5]

print(newlist)

print("-------- Expression --------")

newlist = [x.upper() for x in fruits]

print(newlist)

newlist = ['hello' for x in fruits]

print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)

print("============== Python - Sort Lists ===================")

print("-------- Sort List Alphanumerically --------")

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

print("-------- Sort Descending --------")

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

print("-------- Customize Sort Function --------")

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

print("-------- Case Insensitive Sort --------")

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

print("-------- Reverse Order --------")

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

print("============== Python - Copy Lists ===================")

print("-------- Copy a List --------")

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

print("============== Python - Join Lists ===================")

print("-------- Join Two Lists --------")

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

