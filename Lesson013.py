#Exercises for Lists

# 1 - "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturun.
cars = ["Bmw","Mercedes","Opel","Mazda"]
print(cars)

# 2 - Yukardaki "cars" listesi kaç elemanlarıdır bunu program nasıl bilebilir ?
print(len(cars))

# 3 - "cars" listesinin ilk ve son elemanı nedir bunu bulunuz ?
first_car = cars[0]
last_car = cars[-1]
print(first_car)
print(last_car)

# 4 - Mazda değirini Ford ile değiştirin.
cars[-1] = "Ford" #Eğer listede bir elemanı değiştirmek istiyorsan listedeki arabanın indexini bulup ona yeni bir değer vermelisin.
print(cars)

# 5 - Mercedes listenin bir elemanımıdır ?
isTrue = "Mercedes" in cars #Burdaki in operetoru listenin içinde bu stringi arar ve doğru olup olmadığını söyler.
print(isTrue)

# 6 - Listenin -2 indexteki değeri nedir ?
print(cars[-2])

# 7 - Listenin ilk 3 elemanını alın.
print(cars [0:3])
print(cars[:3])

# 8 - Listenin son 2 elemanı yerine "Audi" ve "Porsche" değerlerini ekleyin.
cars[-2] = "Audi"
cars[-1] = "Porsche"
print(cars)
#Yada bunun daha bir kısa yöntemi olan aşığıdaki gibi yapabiliriz.
cars[-2:] = ["Audi","Porsche"]
print(cars)

# 9 - Bu listenin üzerine "Honda" ve "Renault" değerlerini ekleyin.
cars = cars + ["Honda" , "Renault"]
print(cars)

# 10 - Bu listenin son elemanını siliniz.
del cars[-1]
print(cars)

# 11 - Listenin elemanlarını tersten yazdırın.
print(cars[::-1])

# 12 - Aşığıdaki verileri bir liste içinde saklaynız.

    # Öğrenci1: Yiğit Koyuncu 2005, (70,60,70)
    # Öğrenci2: Elif Koyuncu 2011, (80,80,70)
    # Öğrenci3: Dilara Özgüder 2006, (80,70,90)

student1 = ["Yiğit", "Koyuncu",2005, [70,60,70]]
student2 = ["Elif", "Koyuncu", 2011, [80,80,70]]
student3 = ["Dilara", "Özgüder", 2006, [80,70,90]]

# 13 - Üsteki liste elemanlarını ekrana yazdırın.
result1 = f"{student1[0]} {student1[1]} {2026-student1[2]} yaşında ve not ortalaması {(student1[3][0]+student1[3][1]+student1[3][2])/3} "
result2 = f"{student2[0]} {student2[1]} {2026-student2[2]} yaşında ve not ortalaması {(student2[3][0]+student2[3][1]+student2[3][2])/3} "
result3 = f"{student3[0]} {student3[1]} {2019-student3[2]} yaşında ve not ortalaması {(student3[3][0]+student3[3][1]+student3[3][2])/3} "
