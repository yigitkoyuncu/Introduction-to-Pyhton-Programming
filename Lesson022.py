#Exercises for Assignments
x, y, z = 2, 5, 10
numbers = 1, 5, 7, 10, 6

#1 - Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir?
number1 = int(input("number1:"))
number2 = int(input("number2:"))
numberproduct = number1 * number2
numbersum = x + y + z
thebigone = numberproduct - numbersum
print(thebigone)

#2 - y'nin x'e kalansız bölümünü hesaplaynız.
numberflooryx = y // x
print(numberflooryx) #2

#3 - (x,y,z) toplamının mod 3'ü nedir ?
sum = x + y + z
modresult = sum % 3
print(modresult) #2

#4 - y'nin x'inci kuvetini hesaplayınz.
exponentresult = y ** x
print(exponentresult) #25

#5 - x, *y, z = numbers işlemine göre z'nin küpü kaçtır ?
x, *y, z = numbers
print(*y) #y variable'ı burda 5 7 10 dan oluşan bir liste oluyor.
zexponent = z ** 3
print(zexponent) #216

#6 - x, *y, z = numbers işlemine göre y'nin değerleri toplamı kaçtır?
x, *y, z = numbers
ysum = y[0] + y[1] + y[2]
print(ysum) #22
