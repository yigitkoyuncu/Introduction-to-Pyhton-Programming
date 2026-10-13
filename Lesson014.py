#List Methods
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

#Liste elemanlarından maksimum ve minumumları aşığıdaki gibi bulabiliriz.
val1_max = max(numbers)
val1_min = min(numbers)
val2_max = max(letters)
val2_min = min(letters)
print(val1_max)
print(val1_min)
print(val2_max)
print(val2_min)

#Eğer bir listeden belirli aralıkta istersek ise aşığıdaki gibi yapmalıyız.
valx = numbers[3:4]
valy = numbers[:4]
valz = numbers[3:]
print(valx)
print(valy)
print(valz)

#İstediğimiz listedeki elemanı değiştirmek için aşığıdaki gibi yapabiliriz.
numbers[4] = 40
print(numbers)

#.append metodu listenin sonuna tek bir öğe ekler.
numbers.append(49)
print(numbers)
numbers.append(89)
print(numbers)

#insert(), listenin belirttiğin konumuna bir öğe ekler. Sonraki öğeler sağa kayar.
numbers.insert(2, 99)
print(numbers)
numbers.insert(-1, 99)#Burda insert metodunu sondan eklemeyi gösteriyor.
print(numbers)

#pop(), listeden bir öğeyi çıkarır ve çıkardığı öğeyi döndürür.
numbers.pop(0) #Burda numbers listesindeki ilk indexi siliyor.
print(numbers)
numbers.pop(-1)#Burda numbers listesindeki son eleman siliniyor.
print(numbers)

#remove(), listeden belirttiğin değerin ilk geçtiği öğeyi siler.Bu remove metodunda indexin karakteri bakılır.
numbers.remove(99)# Burda önceden iki tane 99 vardı en baştaki 99 sildi çünkü remove metodu sağdan sola doğru okuyor.
print(numbers)

#sort(), bir listenin öğelerini varsayılan olarak küçükten büyüğe sıralar ya da alfabetik olarak sıralar.
numbers.sort()
letters.sort()
print(numbers)
print(letters)

#reverse(), listedeki öğelerin mevcut sırasını tersine çevirir.
numbers.reverse()
print(numbers)
letters.reverse()
print(letters)

#reverse(), listedeki öğelerin mevcut sırasını tersine çevirir.
print(len(numbers))
print(len(letters))

#count(), listede belirttiğin değerin kaç kez geçtiğini verir.
print(numbers.count(99))
print(letters.count("a"))

#clear(), listedeki tüm öğeleri silerek listeyi boşaltır.
numbers.clear()
print(numbers)
print(len(numbers))




