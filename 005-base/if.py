
print("============== Python If ... Else ===================")

print("-------- Python Conditions and If statements --------")

print("Equals: a == b")
print("Not Equals: a != b")
print("Less than: a < b")
print("Less than or equal to: a <= b")
print("Greater than: a > b")
print("Greater than or equal to: a >= b")

a = 33
b = 200
if b > a:
  print("b is greater than a")

print("-------- Elif --------")

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

print("-------- Else --------")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print("-------- Short Hand If --------")

if a > b: print("a is greater than b")

print("-------- Short Hand If ... Else --------")

a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

print("-------- And --------")

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

print("-------- Or --------")

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

print("-------- Not --------")

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

print("-------- Nested If --------")

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

print("-------- The pass Statement --------")

a = 33
b = 200

if b > a:
  pass

