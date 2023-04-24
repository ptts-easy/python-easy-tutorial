
print("============== Python Sets ===================")

print("-------- Set --------")

thisset = {"apple", "banana", "cherry"}
print(thisset)

print("-------- Duplicates Not Allowed --------")

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

print("-------- Get the Length of a Set --------")

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

print("-------- Set Items - Data Types --------")

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)

set1 = {"abc", 34, True, 40, "male"}

print(set1)

print("-------- type() --------")

myset = {"apple", "banana", "cherry"}
print(type(myset))

print("-------- The set() Constructor --------")

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

print("============== Python - Access Set Items ===================")

print("-------- Access Items --------")

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

print("============== Python - Add Set Items ===================")

print("-------- Add Items --------")

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

print("-------- Add Sets --------")

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

print("-------- Add Any Iterable --------")

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

print("============== Python - Remove Set Items ===================")

print("-------- Remove Item --------")

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

thisset = {"apple", "banana", "cherry"}

del thisset

#print(thisset)     #error

print("============== Python - Loop Sets ===================")

print("-------- Loop Items --------")

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

print("============== Python - Join Sets ===================")

print("-------- Join Two Sets --------")

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

print("-------- Keep ONLY the Duplicates --------")

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

print("-------- Keep All, But NOT the Duplicates --------")

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

