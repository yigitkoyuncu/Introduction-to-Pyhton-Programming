#Exercises

website = "https://www.yigitkoyuncu.com"
course = "Introduction To Python"

# 1 - "Hello World" karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
sentence = " Hello World "
sentence = sentence.strip()
print(sentence)
# NOT :Eğer sadece soldaki boşluğu silmek istersek ".lstrip()" eğer sadece sağdaki boşluğu silmek istersek ".rstrip()" kodunu kullanırız.

# 2 - "ww.yigitkoyuncu.com içindeki yigitkoyuncu bilgisindeki haricindeki her karakteri silin.
website1 = website.lstrip("htps:/w.")
website1 = website.rstrip(".com")
print(website1)

# 3 - "course" karakter dizisinin tüm karakterlerinini küçük harf yapın
course1 = course.lower()
print(course1)

# 4 - "website" içinde kaç tane i karakteri vardır ?
count = website.count("i")
print(count)

# 5 - "website" www ile başlayıp com ile bitiyormu ?
isFound = website.startswith("www")
print(isFound)
isFound = website.endswith("com")
print(isFound)

# 6 - "website" içinde ".com" ifadesi var mı ?
isFound_com = website.find("com")
print(isFound_com)
#Eğer aşağıdaki gibi find kodunu olmayan bir cümle yazarsak sonuç -1 olarak gösterilir.
isFound_com = website.find("comm")
print(isFound_com)
isFound_com = website.index("com")
print(isFound_com)
#Eğer aşağıdaki gibi index koduna olmayan bir cümle yazarsak value error alırız.
#isFound_com = website.index("comm")
#print(isFound_com) exception

# 7 - "course" içindeki karakterlerin hepsi alfabetik mi ? (isalpha)
alpha_course = course.isalpha()
print(alpha_course)

# 8 - "course" içindeki karakterlerin hepsi rakamlardan mı oluşuyor ? (isdigit)
digit_course = course.isdigit()
print(digit_course)

# 9 - "Contents" ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
countents = "Contents"
countents = countents.center(50 ,"*")
print(countents)
#Bunun bir diğer yöntemide .just() kodunu kullanmaktır aşağıdaki gibi.
countents = countents.rjust(50, "*")
countents = countents.ljust(50, "*")
print(countents)

# 10 - "course" karakter dizisindeki tüm boşluk karakterlerini "_" ile değiştirin.
replacment_course = course.replace(" ","_")
print(replacment_course)

# 11 - "Hello World" karakter dizisinin "World" ifadesini "There" olarak değiştirin.
helloworld = "Hello World"
helloworld = helloworld.replace("World","There")
print(helloworld)

# 12 - "course" karakter dizisini boşluk karakterlerinden ayırın.
course_split = course.split(" ")
print(course_split)





