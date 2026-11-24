#Elif statment

#Elif :Python’da elif deyimi, önceki koşulların hiçbiri sağlanmadığında yeni bir koşulu kontrol eder ve
# bu koşul doğruysa kendi kod bloğunu çalıştırır.

x = int(input("x: "))
y = int(input("y: "))
if x > y:
    print("x ,y'den büyüktür.")
elif x == y:
    print("x ,y'ye eşittir.")
else:
    print("x ,y'den küçüktür.")

#NOT:Python’da elif deyimi, aynı koşul zincirinde if’ten sonra ve varsa else’ten önce yazılır.

num = int(input("num: "))
if num > 0:
    print("num is positive.")
elif num == 0:
    print("num is zero.")
else:
    print("num is negative.")
    
