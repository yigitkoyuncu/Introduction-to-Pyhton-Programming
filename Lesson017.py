#Dictionary

#Key - Value

#Bu key value dediğimiz şey plakalarda olduğu gibi bir şehiri kodlarla ifade etmek gibidir

#Örneğin: İzmir => 35, İstanbul=>34, Mersin=>33 gibi.
#Bunu listede aşağıdaki gibi gösterebiiliriz.
cities = ["İzmir", "İstanbul", "Mersin"]
plates = [35, 34, 33]
print(plates[cities.index("İzmir")])

#Bu kod, cities listesindeki "İzmir"in indeksini bulup plates listesinin aynı indeksindeki plakayı yazdırır.
#İşlem Sırası:
#1. cities.index("İzmir") → 0 döndürür. İndeksler 0’dan başlar.
#2. plates[0] → 35 değerini alır.
#3. print(35) → ekrana 35 yazdırır.
#Yani şehirlerle plakaların iki listede aynı sırada olması gerekir.

#Bunu yapmak yerine dictionaryi kullanarak çok daha kısa yöntemle print("İzmir") => 35 elde edebiliriz.
#Bu dediğimi aşığıda yapacağım key value yolluyla halledeceğiz

plates = {"İzmir" : 35,"İstanbul" : 34,"Mersin" : 33}
print(plates["İzmir"])#34
print(plates["İstanbul"])#35
print(plates["Mersin"])#33
#print(plates[35]) (Burdaki hata valueyu yazdığımızdan dolayı oluyor platesin içine keyi yazmalıyız valueyu değil.

#Eğer sonradan bir key daha eklemek istiyorsak aşığıdaki gibi yapmalıyız.
plates["Karaman"] = 70 #Bu kodu yazdıktan sonra Karaman key olarak 70 te value olarak platese eklenir.
print(plates)

#Hali hazırda key ve value olan şeyleride aşığıdaki işlemleri uygulayarak değiştirebiliriz.
plates["Karaman"] = "Memleket"
print(plates)

#Bir key elemanın içine birden fazla key ve value eklenebilir.
users = {
    "Yiğit" : {
        "age" : 21
        "roles" : ["engineer","fighter"]
        "nickname" : "s1mbatpala"
        "address" : "İzmir"

    }
}
print(users["Yiğit"])#Bu kod Yiğit keyinin içindeki tüm valueları verir.
print(users["Yiğit"]["age"]) #Bu kod ise Yiğitin içinden age keyini alarak sadece age keyinin valuesunu verir.
print(users["Yiğit"]["roles"][0]) #Burda yaptığımız şey ise roles keyinin içindeki ilk valueyu seçip almak.





