#Lists

#Liste yöntemi dediğimiz şey .split() fonksiyonunda çıktıda olduğu gibi liste liste ayrılması bir list yöntemidir.
message = "Hello There. My name is Yiğit Koyuncu".split()
print(message)
print(message[0])

#Liste şeklinde aşığıdaki koddaki gibi yapabiliriz.
my_list = [1,2,3]
print(my_list)

#Listeye farklı türlerde eleman ekleyebiliriz ve bu sıkıntı yaratmaz.
my_list = ["bir" , 1, True , 5.6]
print(my_list)

#2 farklı listeyi aşığıdaki gibi 1 liste halinde birleştirebiliriz.
list1 = ["one" ,"two" ,"three"]
list2 = ["four", "five", "six"]
numbers = list1 + list2
print(numbers)
#Bu numbers listesinde kaç eleman olduğunu "len" koduyla öğrenebiliriz.
print(len(numbers))

#Eğer ilk satırdaki message .split() kodunu kullanmasaydık çıktı kelime olmaktan çıkıp sadece ilk indexi kabul edecekti.
message = "Hello there. My name is Yiğit Koyuncu"
print(message[0])

#Liste içerisinde liste yapmak istiyorsak listeleri toplamak yerine yeni bir liste oluşturumuş gibi yapıp listeleri bir elemanmış gibi kabul edeceğiz.
userA = ["Yiğit" , 20]
userB = ["Dilara", 20]
users = [userA, userB]
print(userA)
print(userB)
print(users)
#Users listesindeki bir elamana ulaşmak istiyorsak aşığıdaki gibi yapmalıyız.
print(users[0][0]) #Burdaki ilk 0 userAyi ifade ediyor ikinci 0 ise Yiğiti ifade ediyor.
print(users[1][0]) #Burdaki ilk 1 userByi ifade ediyor ikinci 0 ise Dilarayı ifade ediyor.

