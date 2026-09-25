#Type Conversation
x = input("1st number: ")
y = input("2nd number: ")

print(type(x))
print(type(y))
sum = int(x) + int(y)
print(sum)
#--------------------------------------------

x = 5             #int
y = 2.5           #float
name = "Yigit"    #string
isOnline = True   #bool

print(type(x))
print(type(y))
print(type(name))
print(type(isOnline))

#int to float
x = float(x)
print(x)
print(type(x))

#float to int
y= int(y)
print(y)
print(type(y))

#sum with string data type
result = str(x) + str(y)
print(result)
print(type(result))

#bool to string
isOnline = str(isOnline)
print(isOnline)
print(type(isOnline))

#bool to integer
isOnline = False
isOnline = int(isOnline)
print(isOnline)
print(type(isOnline))