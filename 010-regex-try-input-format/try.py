
print("============== Python Try Except ===================")

print("-------- Exception Handling --------")

try:
  print(x)
except:
  print("An exception occurred")

print("-------- Many Exceptions --------")

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

print("-------- Else --------")

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

print("-------- Finally --------")

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

print("-------- Raise an exception --------")

try:
  x = -1

  if x < 0:
    raise Exception("Sorry, no numbers below zero")
except Exception as err:
  print(f"Unexpected {err=}, {type(err)=}")

try:
  x = "hello"

  if not type(x) is int:
    raise TypeError("Only integers are allowed")
except Exception as err:
  print(f"Unexpected {err=}, {type(err)=}")
