#String Methods

#Burdaki cümleyi tamamen büyük harflerle yazmak için ".upper()" kodu kullanılır.
message1 = " Hello there. My name is Yiğit Koyuncu"
message1 = message1.upper()
print(message1)

#Yukardaki aynı cümleyi tamamen küçük harflerle yazmak için ".lower()" kodu kullanılır.
message2 = message1.lower()
print(message2)

#Aynı cümleninin her kelimenin baş harfini büyük yapmak için ".title()" kodu kullanılır.
message3 = message1.title()
print(message3)

#Aynı cümlenin sadece baş harfini büyük yapmak için ".capitalize()" kodu kullanılır.
message4 = message1.capitalize()
print(message4)

#Bu cümlenin başındaki boşluk indexini silmek için ".strip()" kodu kullanılır.
message5 = message1.strip()
print(message5)

#Cümledeki kelimeleri teker teker ayırmak istersekde ".split()" kodunu kullanabiliriz.
message6 = message1.split()
print(message6)
#Spiltin içine nokta koyarsak noktalardan sonrakileri ayırcak.
message7= message1.split(".")
print(message7)

#Bu mesage6daki indexlere ulaşmak istediğimizde ise sonuç kelime kelime çıktıda çıkacaktır.
print(message6[0])
print(message6[3])

#Kelimelerin arasına birleştirmek için " " ".join(message) " kodunu kullanabiliriz.
message8 = "---".join(message7)
print(message8)
message9 = "*".join(message1)
print(message9)

#Cümlenin içinden herhangi bir kelimenin hangi indexle başladığını öğrenmek için aşağıdaki gibi yapılmalıdır.
index = message1.find("YIĞIT")
print(index)
#Eğer cümlenin içinde bu kelime bulunmuyorsa printlediğinde sonuç -1 çıkar aşığıdaki örnek gibi.
index = message1.find("Yiğit")
print(index)

#Aşığıda vericek olduğumuz kodda cümlenin başındaki karakterin doğru olup olmadığını bu kod ile sorgulayabiliriz.
isFound=message1.startswith(" ")
print(isFound)

#Aşığıda vericek olduğumuz kodda cümlenin sonundaki karakterin doğru olup olmadığını bu kod ile sorgulayabiliriz.
isFound=message1.endswith("U")
print(isFound)

#Cümle içerisinde bir kelimeyi değiştirmek istersek ".replace("","")" kodunu kullanabiliriz.
message10 = message1.replace("YIĞIT","DILARA")
print(message10)
message11 =  message1.replace(" ","*")
print(message11)

#Bir url oluştururken türkçe karakterleri değiştirmek için bu metodu kullanabiliriz.
message12 = message1.replace("ç","c").replace("ö","o").replace(" ","_")
print(message12)

#Bir cümleyi çıktıda ortalamak için .center() kodunu kullanabiliriz parantez içi ise kaç indexle ortalamak gerektiğini anlatır.
message13 = message1.center(50)
print(message13)
message14 = message1.center(100)
print(message14)
#Virgulun yanına herhangi bir index atadığımızda boşlukları full o indexle doldurur.
message15 = message1.center(50,"*")
print(message15)
message16 = message1.center(100,"a")
print(message16)
