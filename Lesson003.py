#Variables
print(4500 - (5000 * 0.27))
print(4500 - (4000 * 0.27))

maasYigit =5000
maasDilara = 4000
vergi = 0.27
print(maasYigit - (maasDilara * vergi))
print(maasDilara - (maasDilara * vergi))

#Değişken Tanımlama Kuralları

#Rakam ile başlayamaz.

number1 = 10
print(number1)

number1 = 20
print(number1)

number1 += 30
print(number1)

#Büyük küçük harf duyarlılığı vardır.

age = 20
AGE = 10
print(age)
print(AGE)

#Türkçe karakter kullanmayalım.

yas = 20
_age = 20

x = 1 #int
y = 2.3 #float
name = "Yigit" #string
isStudent = True #bool

#x, y, name, isStudent = (1, 2.3, "Yigit", True)

a = 10
b = 20
print(a+b) #30

a = "10"
b = "20"
print(a+b) #1020

#Değişkenler arası boşluk olamaz onun yerine "_" konur.
firstName = "Yigit"
last_Name = "Koyuncu"

print(firstName + last_Name) #Yiğit Koyuncu
