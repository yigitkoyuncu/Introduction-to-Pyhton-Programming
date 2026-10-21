#Comprasion

#Bu aşağıdaki gibi username passwordla alakalı şeyler karşılaştırma opertörleriyle yapılabiliyor.
#username, password => database
#"yigitkoyuncu", "1124234235"

#Burda a, b, c, d variablelarını kendi içinde karşılaştırıyoruz.
a, b, c, d = 5, 5, 6, 7
resultab1 = (a == b)
print(resultab1) #True
resultac1 = (a == c)
print(resultac1) #False
resultab2 = (a != b) #Burdaki != operatörü eşit değil anlamına geliyor.
print(resultab2) #False
resultac2 = (a != c)
print(resultac2) #True
resultab3 = (a > b)
print(resultab3) #False
resultac3 = (c > a)
print(resultac3) #True
resultab4 = (a >= b)
print(resultab4) #True
resultac4 = (a >= c)
print(resultac4) #False

#Trueyla 1 eşittir çünkü True bilgisinin numaric karşılığı 1'dir.
resultTrue = True == 1
print(resultTrue) #True
#Falsela 0 eşittir çünkü False bilgisinin numaric karşılığı 1'dir.
resultFalse = False
print(resultFalse) #True
#True ile False boolenlerini toplama ya da çıkarma işleminde 1 ile 0 değerleri olarak kullanabiliriz aşığıdaki yaptığımız gibi.
resultBoolenSum = True + False + 40 #resultBoolenSum = 1 + 0 + 40
print(resultBoolenSum) #41


#Burda yaptığımız şey username inputuyla "ygtkync" stringinin doğru olup olmadığını karşılaştırıyoruz.
username = input(str("Enter your username: "))
resultusername = ("ygtkync" == username)
print(resultusername) #usernamedeki inputa bağlı olarak True / False değerlerinden birini elde ederiz.
