#Tuple
list = [1,2,3]
tuple = (1,"iki",3)
print(type(list))
print(type(tuple))
print(list[2])
print(tuple[2])
print(len(tuple))
print(len(list))

#Aşağıdaki kodda olduğu gibi listte indexleri değiştirebilirken tupleda bunu yapamıyoruz.
list = ["elif","dilara"]
tuple = ("yiğit","güven")
list[0] = "fatma"
#tuple[0] = "ozan"
print(list)
print(tuple)

#Tuple Methods
tuple = ("elif","dilara","dilara")
#Liste metodunda olduğu gibi tuple metodunda da count bir tuple da kaç tane bu indexden olduğunu hesaplamaya yarıyor.
print(tuple.count("dilara"))
#Liste metodunda olduğu gibi tupleda da index sayısını bulabiliriz .index() metoduyla
print(tuple.index("dilara"))

#Bir tuple başka bir tuple ile birleştirebiliriz.
cars1 = ("skoda","ford","toyota")
cars2 = ("tofaş","fiat","renault")
cars = cars1 + cars2
print(cars)
#Eğer diğer tuple’ı tek bir eleman olarak içine eklemek istiyorsan aşığıdaki metodu kullanmalısın.
cars = cars + (cars2,)
print(cars)
