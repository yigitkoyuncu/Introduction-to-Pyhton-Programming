#Examples For if and else statment

# 1 - Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz.Ehliyet alma koşulu
#     en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.

name = str(input("name:"))
age = int(input("age:"))
education = str(input("education:"))

if name == "Yiğit":
    if age >= 18:
        if education == "University" or education == "High School":
            print("You can obtain a driver's license.")
else:
    print("You cannot obtain a driver's license.")

# 2 - Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamya göre not aralığını karşılık gelen not bilgisini
#     yazdırınız.
#     0 - 24 => 0
#     25 - 44 => 1
#     45 - 54 => 2
#     55 - 69 => 3
#     70 - 84 => 4
#     85 - 100 => 5

grade1 = int(input("grade1:"))
grade2 = int(input("grade2:"))
grade3 = int(input("grade3:"))

average = (grade1 + grade2 + grade3) / 3
if 25 > average > 0 :
    print(0)
if 45 > average >= 25:
    print(1)
if 55 > average >= 45:
    print(2)
if 70 > average >= 55:
    print(3)
if 85 > average >= 75:
    print(4)
if 100 > average >= 85:
    print(5)

# 3 - Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
#     1.Bakım => 1.yıl
#     2.Bakım => 2.yıl
#     3.Bakım => 3.yıl
#     **Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız.
#     ***datetime modulünü kullanmamız gerekiyor.
#     (simdi) - (2018/8/1) => ...gün
import datetime

x = datetime.date.today()
y = datetime.date(2018, 8, 1)
days = (x-y).days
years = days //365
for i in range(1, years+1):
    if 11 <= i % 100 <= 13:
        suffix = "th"
    elif i % 10 == 1:
        suffix = "st"
    elif i % 10 == 2:
        suffix = "nd"
    elif i % 10 == 3:
        suffix = "rd"
    else:
        suffix = "th"
print(f"{i}{suffix} maintenance")










