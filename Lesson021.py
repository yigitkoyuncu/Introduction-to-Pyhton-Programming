#assignment

#x = 10
#y = 20
#z = 30
#Böyle yazmak yerine , kullanarak aşığıda yapmış olduğumuz gibi variable tanımlayabilirsin.
x, y, z = 10, 20, 30
print(x,y,z) #10 20 30

#Variableları kendi arasında değiştirebiliriz aşığıda olduğu gibi
x, y = y, x
print(x,y,z) #20 10 30

#x = x + 5 yapmak yerine += kullanabiliriz.(Toplama)
x += 5
print(x,y,z) #25 10 30

#x = x - 6 yapmak yerine += kullanabiliriz.(Çıkarma)
x -= 6
print(x,y,z) #19 10 30

#x = x * 7 yapmak yerine *= kullanabiliriz.(Çarpma)
x *= 7
print(x,y,z) #133 10 30

#x = x / 8 yapmak yerine /= kullanabiliriz.(Bölme)
x /= 8
print(x,y,z) #16.625 10 30

#x = x % 9 yapmak yerine %= kullanabiliriz.(Bölümden kalan kısım.)
x %= 9 #7.625 10 30
print(x,y,z)

#x = x // 10 yapmak yerine //= kullanabiliriz.(Tam bölüm.)
x //= 10
print(x,y,z) #0.0 10 30

#x = x ** 1 yapmak yerine **= kullanabiliriz.(Üs alma.)
x **= 11
print(x,y,z) #0.0 10 30

#Bir listeye ya da tupledaki elemanları tek tek variablelara atamak yerine en üstte yaptığımız gibi virgülün yardımıyla tek bir satır kodla atayabiliriz.
values1 = 1, 2 ,3
print(type(values1)) #<class 'tuple'>
print(values1) #(1, 2, 3)
x, y, z = values1 #Bunu yaparken values tupleındaki değerleri x, y ve z ye atamış oluyoruz.
print(x,y,z) #1 2 3

#Mesela values ın içinde 2 değer olsaydı ve atamak istediğimiz değerler 3 tane olsaydı nolurdu?
values2 = 5, 6
print(type(values2)) #<class 'tuple'>
print(values2) #5, 6
#a, b, c = values2 (Bu kodda ValueError alırız.)

#Mesela values değerinin içinde 5 tane değer olsa ve atamak istediğimiz değerler 5 tane olsa napardık?
values3 = 7, 8, 9, 10, 11
print(type(values3)) ##<class 'tuple'>
print(values3) #7, 8, 9, 10, 11
m, n, *k= values3 #k variablenın önüne * değerini koyarak values3 te kalan 3 değeride kendine çekip k için bir liste oluşturmuş olur.
print(m,n,k) #7 8 [9, 10, 11]
#z liste olduğu için print yaparken k nin indekslerinden istediğimizi yazdırabiliriz.
print(m,n,k[1]) #7 8 10