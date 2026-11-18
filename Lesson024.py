#Examples for Comprasion
from Lesson004 import total

# 1 - Girilen 2 sayıdan hangisi büyüktür.
a = int(input("a: "))
b = int(input("b: "))
if a == b:
    print("Equal")
if a < b:
    print("a is less than b")
if a > b:
    print("a is greater than b")

# 2 - Kullanıcıdan 2 vize (%60) ve final (%40) notunu ortalama hesaplayınız. Eğer ortalama 50 ve üstündeyse geçti değilse
#kaldı yazdırın.
vize1 = int(input("Vize 1: "))
vize2 = int(input("Vize 2: "))
vizetotal = vize1 + vize2
final = int(input("Final: "))
result = ((final*40/100) + (vizetotal*60/100)) / 2
if result => 50:
    print("Geçti")
else:
    print("Kaldı")

# 3 - Girilen bir sayının tek mi çift mi olduğunu yazdırın.
a = int(input("a: "))
if a % 2 == 0:
    print("Çift Sayı")
else:
    print("Tek Sayı")

# 4 - Girilen bir sayının negatif pozitif durumunu yazdırın.
a = int(input("a: "))
if a > 0:
    print("Pozitif")
else:
    print("Negatif")

# 5 - Email bilgisini isteyip doğruluğunu kontrol ediniz. (email = email@yigitkoyuncu.github)
email = "email@yigitkoyuncu.github"
youremail = string(input("Enter your email: "))
if youremail == email:
    print("Email Is Correct")
else:
    print("Email Is Incorrect")
