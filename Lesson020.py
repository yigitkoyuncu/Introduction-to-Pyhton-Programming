#Value and Reference Type

#Value Type => string, numbers
x = 10
y = 20
x = y
y = 12
print(x,y) #Burda (20,12) output olarak bize geri dönecektir.x değerinin burda 12 olmasının sebebi y = 20 yazdıktan sonra x = y dememiz.
#x = y değerini y = 12in alt satırına yazsaydık outputumuz (12,12) olacaktı.

#Reference Types => list, class
a = ["apple","banana"]
b = ["apple","banana"]
a = b
b[0] = "grape"
print(a,b)
#Reference Typelarda Value Typelarının aksine eğer birtane listedeki elemanı değiştirirsen o değiştirdiğin eleman aynı şekilde diğer listedede değişir.
