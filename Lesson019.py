#Sets

fruits = {"apple", "banana", "cherry"}
print(fruits)
#print(fruits[0]) Setsler indekslenemez.

for x in fruits:
    print(x) #Setsteki bütün elemanları For döngüsüyle gösterebiliriz.

#Setse yeni eleman eklemek için .add() metodunu kullanabiliriz.
fruits.add("peach")
print(fruits)

#Birden fazla eleman eklemek istersek ise .updata() metodunu kullanabiliriz.
fruits.update(["grapes", "mango"])
print(fruits)
#Eğerki içerde var olan bir elemanı eklmeye kalkarsak yinede, şimdi aşığıda göreceğiniz gibi o eleman tekrar setse eklenmez.
fruits.update(["grapes", "mango", "apple"])
print(fruits) #Bu fruit setinde apple olduğu için yine 2. apple eklenmez.

#Bir listede tekrarlayan elemanlar varken o listeyi set olarak dışarı çıkarmak istediğimizde o listedeki tekrarlayan elemanlardan sadece 1 tane çıkar.
myList = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,4]
print(set(myList)) #{1, 2, 3, 4} output olarak burdan bu çıkar.
print(myList) #Burda çıktıda set olarak çıkartmadığımızdan ve bu bir liste olduğunda listedeki tüm elemanlar output olarak çıkar.

#Bir setsten herhangi bir eleman silmek istersek .remove() metodunu veya .discard() metodunu kullanmalıyız.
fruits.remove("apple")
print(fruits)
fruits.discard("grapes")
print(fruits)

#.pop() metodu listede son elemanı siliyordu fakat setste rastgele bir tane elemanı siliyor çünkü setste elemanlar sıralı değil.
fruits.pop()
print(fruits)

#.clear() metodu aynı listelerde olduğu gibi setsteki tüm elemanları siliyor.
fruits.clear()
print(fruits)