#Yarı çapı verilen bir dairenin alan ve çevresini hesaplayanız (r: 3.14)

#Dairenin Alanı: (pi)r^2
#Dairenin Çevresi: 2(pi)r

r = float(input ("Yarı çap: "))
pi = 3.14

dcevre = 2 * pi * r
dalan = pi * (r ** 2)

print("Alan: ", str(dalan), "Çevre: ", str(dcevre))

#Eğer stringli bir printin içine float ya da integer yazmak istiyorsak error almamak için string formatına dönüştürmeli.
#Eğer inputa 2a tarzı şeyler yazılırsa value error verir.