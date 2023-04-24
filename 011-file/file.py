
print("============== Python File Open ===================")

print("-------- Open a File on the Server --------")

f = open("demofile.txt", "r")
print(f.read())

print("-------- Read Only Parts of the File --------")

f = open("demofile.txt", "r")
print(f.read(5))

print("-------- Read Lines --------")

f = open("demofile.txt", "r")
print(f.readline())

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

f = open("demofile.txt", "r")
for x in f:
  print(x)

print("-------- Close Files --------")

f = open("demofile.txt", "r")
print(f.readline())
f.close()

print("============== Python File Write ===================")

print("-------- Write to an Existing File --------")

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())

print("-------- Create a New File --------")

try:
  f = open("myfile.txt", "x")
except:
  print("A file exists")

f = open("myfile.txt", "w")

print("============== Python Delete File ===================")

print("-------- Delete a File --------")

import os
os.remove("demofile3.txt")

print("-------- Check if File exist: --------")

import os
if os.path.exists("demofile2.txt"):
  os.remove("demofile2.txt")
else:
  print("The file does not exist")

print("-------- Make Folder --------")

try:
  os.mkdir("myfolder")
except:
  print("A folder exists")
import os

print("-------- Delete Folder --------")

import os
os.rmdir("myfolder")

print("-------- Seek File --------")

f = open("demofile.txt", "r")

f.seek(0, 0)

for x in f:
  print(x)
