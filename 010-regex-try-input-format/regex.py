import re

print("============== Python RegEx ===================")

print("-------- RegEx in Python --------")

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

print(x)

print("-------- The findall() Function --------")

txt = "The rain in Spain"
x = re.findall("ai", txt)

print(x)

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

print("-------- The search() Function --------")

txt = "The rain in Spain"
x = re.search("\s", txt)

print(x)

print("The first white-space character is located in position:", x.start())

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

print("-------- The split() Function --------")

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

print("-------- The sub() Function --------")

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

print("-------- Match Object --------")

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

txt = "The rain in the Sky in Spain"
x = re.search(r"\bS\w+", txt)

print(x.span())

print((x.start(), x.end()))

txt = "The rain in the Sky in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

txt = "The rain in the Sky in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
