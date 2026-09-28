#Format

name = "Yiğit"
surname = "Koyuncu"
age = 20

#Süslü parantezin içine direkt format name olarak yazabildik.İndexlerden 0 ismi 1 soyismini ifade ediyor.
print("My name is {0} {1}".format(name, surname))
print("My name is {1} {0}".format(name, surname))

#İndexleri kullanmak istemezsek burda n ve s değerini vererekten ters çevirebiliriz.
print("My name is {s} {n}".format(n = name,s = surname))

#Eğer yukarda age bilgisi tanımlamazsak age böyle ekleyebiliriz.
print("My name is {} {} and I'm {} years old.".format(name, surname, "20"))

#Eğer formaata hepsini name bilgisi olarak yazdırabiliriz formatın üçünede name yazarak.
print("My name is {} {}) and I'm {} years old.".format(name, name, name))

#---------------------------------------------------------------------------------------------------------

#Aşağıda gibi yapıldığında sonuç tamamen tamımı verilir.
result = 200 / 700
print("the result is {r:}".format(r = result))
#Eğer sonucun 0'dan sonraki basamak değerlerini sınırlandırmak istiyorsak . sağında ayarlıyoruz.
print("the result is {r:1.3}".format(r = result))
#Ve . solunda ise sonucun karakter sayısını ifade ediyor.
print("the result is {r:10.3}".format(r = result))

#---------------------------------------------------------------------------------------------------------

#f string nasıl yapılır.
print(f"My name is {name} {surname} and I'm {age} years old.")
