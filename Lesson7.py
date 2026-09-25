#String

#inti stringe çevirmen lazım yoksa error alırsın.
name = "Yiğit"
surname = "Koyuncu"
age = 20

print("My name is " + name + " " + surname + "and I am " + str(age) + " years old.")

#\n outputta yeni satır olmasını sağlar.
name = "Yiğit"
surname = "Koyuncu"
age = 20
greeting = "My name is " + name + " " + surname + " and \nI am " + str(age) + " years old."

print(greeting)

#İndexleri belirliyoruz.
print(greeting[0])
print(greeting[3])

#Greetingde kaç tane karakter olduğunu belirlemek için leni kullanılırız.
print(len(greeting))

#Burda greetingdeki son indexi bulmak için yapılması gerekenler aşağıdaki gibidir.
lenght = len(greeting)
print(greeting[lenght-1])

#Belirli index aralığı aşağıdaki gibi bulunur.
print(greeting[3:7])
print(greeting[3:])
print(greeting[:16])
print(greeting[2:40:2]) #Burdaki en son sayı 2 indexten birini almamızı sağlıyor.