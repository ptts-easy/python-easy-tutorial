import datetime

print("============== Python Datetime ===================")

print("-------- Python Dates --------")

x = datetime.datetime.now()

print(x)

print("-------- Date Output --------")

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

print("-------- Creating Date Objects --------")

x = datetime.datetime(2020, 5, 17)

print(x)

print("-------- The strftime() Method --------")

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))
