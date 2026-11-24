#Identity and Membership Operators

#Identity Operator: is
x = y = [1, 2, 3]
z = [1, 2, 3]
print(x == y) #Aynı küme değerine sahipler bundan dolayı output True olur.
print(x == z) #Aynı küme değerine sahipler bundan dolayı output True olur.
print(x is y) #Aynı objedirler bundan dolayı output True olur.
print(x is z) #Farklı objedirler bundan dolayı output False olur.

#Membership Operator: in
a = ["apple", "banana", "cherry"]
print("banana" in a) #True

name = "Yiğit"
print("ğ" in name) #True
print("ğ" not in name) #False

