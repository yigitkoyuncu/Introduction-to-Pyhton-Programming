#Examples For Logical Operators

# 1 - Girilen bir sayının 0 - 100 arasında olup olmadığını kontrol ediniz.
x = int(input())
between0_100 = x > 0 and x < 100
print(between0_100)

# 2 - Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
y = int(input())
positiveevenno = (y % 2 == 0) and (y > 0)
print(positiveevenno)

# 3 - Email ve parola bilgileri ile giriş kontrolü yapınız.
email = str(input())
parola = str(input())
kontrol = (email == "yigitkoyuncu.github") and (parola == "y")
print(kontrol)

# 4 - Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
a = int(input())
b = int(input())
c = int(input())
biggerno = (a > b > c) or (b > c > a) or (c > a > b) or (c > b > a) or (b > a > c) or (a > c > b)
print(biggerno)

# 5 - Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalamayı hesaplayınız.
#     Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#     a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#     b-) Finalden 70 alındığında ortalamının önemi olmasın.
firstmidterm = int(input())
secondmidterm = int(input())
final = int(input())
average = [((firstmidterm + secondmidterm) / 2) * 60 /100] + [(final) * 40 / 100]
if average >= 50 and final >= 50:
    print("Geçti")
else:
    print("Kaldı")

# 6 - Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#     Formül: (Kilo / boy uzunluğunun karesi)
#     Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#     0 - 18.4 => Zayıf
#     18.5 - 24.9 => Normal
#     25.0 - 29.9 => Fazla Kilolu
#     30.0 - 34.9 => Şişman (Obez)
Ad = str(input())
Kilo = int(input())
Boy = float(input())
Indeks = Kilo / (Boy ** 2)
if 18.5 > Indeks > 0:
    print("Zayıf")
if 25 > Indeks >= 18.5:
    print("Normal")
if 30 > Indeks >= 25.0:
    print("Fazla Kilolu")
if 35 > Indeks >= 30.0:
    print("Obez")


