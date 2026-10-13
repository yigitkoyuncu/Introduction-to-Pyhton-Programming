#Exercises for List Methods
names = ["Yiğit","Elif","Dilara","Bade"]
years = [2005, 2011, 2006, 2033]

# 1 - Bulut ismini listenin sonuna ekleyiniz.
names.append("Bulut")
print(names)

# 2 - Güven ismini listenin başına ekleyeniz
names.insert(0, "Güven")
print(names)

# 3 - Elif ismini listeden siliniz.
names.remove("Elif")
print(names)

# 4 - Dilara isminin indeksi nedir ?
names.index("Dilara")
print(names)

# 5 - Yiğit listenin bir elemanımıdır ?
print("Yiğit" in names) #Varsa True yazar yoksa eğer False çıktısını verir.

# 6 - Liste elemanlarını ters çevirin
names.reverse()
years.reverse()
print(names)
print(years)

# 7 - Liste elemanlarını alfabetik sıralayın ?
names.sort()
print(names)

# 8 - Years elemanlarını rakamsal büyüklüğe göre sıralayın.
years.sort()
print(years)

# 9 - str = "Ford, Kia" karakter dizisini listeye çevirin
cars = ["Ford", "Kia"]
print(cars)

# 10 - years listesinin en büyük ve en küçük elemanı nedir ?
print(max(years))
print(min(years))

# 11 - years listesinde kaç tane 2006 değeri vardır ?
print(years.count(2006))

# 12 - years listesinden tüm elemanları siliniz.
years.clear()

# 13 - Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız
x = str(input("Cellphone1:"))
y = str(input("Cellphone2:"))
z = str(input("Cellphone3:"))
cellphones = [x,y,z]
print(cellphones)






