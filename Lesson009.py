#Exercises

website = "https://github.com/yigitkoyuncu"
course = "Introduction to Python Programming"

# 1 - "course" karakter dizisinde kaç karakter bulunmaktadır ?
print(len(course))

# 2 - "website"  içinden github.com/ karakterini yazdır.
print(website[8:19])

# 3 - "website" içinden yigitkoyuncu karakterini yazdır.
print(website[19:34])
lenght = len(website)
print(website[lenght - 12:lenght])

# 4 - "course" içinden ilk 15 ve son 15 karakterini alın.
print(course[:15]) #Burda soldaki indexleri dahil ediyoruz çünkü : rakamın solunda kalıyor.
print(course[0:15])
print(course[-15:]) #[-15:-1] yaparsak çıktadaki son index belli olmaz ondan dolayı [-15:] yapmalıyız ve burda sağdaki indexleri alıyoruz.

# 5 - "course" ifadesindeki karakterleri tersten yazdırılalım.
print(course[::]) #Burda bütün indexleri dahil etmiş oluyoruz.
print(course[::2]) #Burda 2 indexten birini almış oluyor.
print(course[::3]) #Burda 3 indexten birini almış oluyor.
print(course[::-1]) #Burda ise asıl sorunun cevabı olan indexleri tam tersi şekilde yazdırmış oluyoruz.

#-----------------------------------------------------------------------------------------------------------------------

#Aşağıdaki stringi beşle çarparsan beş kez yazar.
s = "12345" * 5
print(s)

#Eğer spesifik olarak bir index seçmek istersek aşağıdaki gibi uygulama yapmalıyız.
print(s[::5])

#-----------------------------------------------------------------------------------------------------------------------

name, surname, age, job = "Dilara" , "Özgüder" , 20 , "Bilgisayar Mühendisi"

# 6 - Yukarıda verilen değişkenler ile ekrana aşığıdaki ifadeyi yazdırın.
# "Benim adım Dilara Özgüder, yaşım 20 ve mesleğim Bilgisayar Mühendisi."
print(f"Benim adım {name} {surname},yaşım {age} ve mesleğim {job}.")
print("Benim adım {} {},yaşım {} ve mesleğim {}.".format(name, surname, age, job))

# 7 - "Hello world" ifadesindeki w harfini "W" ile değiştirin.
s = "Hello world"
s =  s[0:6] + "W" + s[-4:] #Burda yaptığımız şey s dönüştürmek
# s[0:6] dediğimiz şey "Hello" kısmı, s[-4:] kısmı ise orld kısmıdır.
#Bunun başka bir metodu ise replace metodudur ve bu metod aşağıdaki gibi gösterilirmiştir.
s.replace("w" , "W")
print(s)

# 8 - "abc" ifadesini yan yana 3 defa yazdırın.
x = "abc" * 3
print(x)
