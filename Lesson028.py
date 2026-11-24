#If and Else Statments

#If: Python’da if, bir koşul doğruysa ilgili kod bloğunu çalıştırır.
if 3 == 3:
    print("3 sayısı 3'e eşittir.")

if True:
    print("True doğrudur bundan dolayı bu çıktıyı görüyorsun True yerine False yazsaydın başta bu çıktıyı göremezdin.")

#Else: Python’da else deyimi, önceki koşulların hiçbiri sağlanmadığında hangi kodun çalışacağını belirler.
username = "S1MBATPALA"
password = "1234"
isLoggedin = (username == "S1MBATPALA") and (password == "1234"):
if isLoggedin:
    print("Logged in successfully")
else:
    print("Login failed")

