#Logical Operators
import random
x = 6
result = 5 < x < 10
print(result) #True
#Burda yaptığımız şey x değerinin doğru olup olmadığını tespit etmek.

#Bu yukardakini yapmak yerine "and" , "or" , "not" operatörlerini kullanabilriz.

#and
result = (5 < x) and (x < 10)
print(result) #True , True => True ; True , False => False
#and operatöründe string değerlerinide kullanabiliriz.
hak = random.randint(0, 10)
devam = str(input())
resultoyun = hak > 0 and devam == "e"
print(resultoyun)
#True, False => False
#True, True => True
#False, False => False

#or
a = int(input())
resultor = (a > 0) or (a % 2 == 0)
print(resultor)
# True, False => True
# True, True => True
# False, False => False

#not
b = int(input())
resultnot = not(b > 0) #Normalde b'yi pozitif tam sayı girdiğimizde True gelmesi gerekirken Not ile beraber False değerini elde ederiz.
print(resultnot)
