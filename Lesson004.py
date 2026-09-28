#Örnekler
#-----------------------------------------------------------------------------------
#1- Bir müşterinin aşağıdaki bilgiler için değişken oluşturunuz.

#Müşteri adı
#Müşteri soyadı
#Müşteri ad + soyadı
#Müşteri cinsyet
#Müşteri tc kimlik
#Müşteri doğum yılı
#Müşteri adres bilgileri
#Müşteri yaşı

customerName = "Dilara"
customerSurname = "Özgüder"
customerNS = customerName + " " + customerSurname
customerGender = True #Female
customerID = 1234
customerBY = 2006
customerAdress = "Vilnus"
customerAge = 2026 - customerBY
print(customerNS)
print(customerGender)
print(customerID)
print(customerBY)
print(customerAdress)
print(customerAge)

#2- Aşağıdaki siparişlerin toplam bilgisini hesaplayınız.

#Sipariş 1 = 110    TL
#Sipariş 2 = 1100.5 TL
#Sipariş 3 = 356.95 TL

order1 = 110
order2 = 1100.5
order3 = 356.95
total = order1 + order2 + order3
print("Total:", total)
