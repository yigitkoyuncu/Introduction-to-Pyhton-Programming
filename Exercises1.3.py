#1.3 Exercises (Conditionals and Loops)
import stdio
import math
import random
import sys

#1st Question
#Compose a program that takes three integer command-line arguments and writes 'equal' if all three are equal, and 'not equal' otherwise.
Number1 = int(input("Number1: "))
Number2 = int(input("Number2: "))
Number3 = int(input("Number3: "))
if Number1 == Number2 == Number3:
    stdio.writeln("Equal")
else:
    stdio.writeln("Not Equal")

#2nd Question
#Compose a more general and robust version of quadratic.py (from Section 1.2) that writes the roots of
# the polynomial ax2bx + c, writes an appropriate error message if the discriminant is negative, and behaves appropriately
# (avoiding division by zero) if a is zero.
a = float(input("Number1: "))
b = float(input("Number2: "))
c = float(input("Number3: "))
if a == 0:
    if b != 0:
        print("Root:", -c / b)
    elif c == 0:
        print("Every real number is a solution.")
    else:
        print("No solution.")
else:
    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        print("Error: the equation has no real roots.")
    elif discriminant == 0:
        print("Root:", -b / (2 * a))
    else:
        root = math.sqrt(discriminant)
        # This form reduces cancellation for one of the roots.
        q = -0.5 * (b + math.copysign(root, b))
        print("Root 1:", q / a)
        print("Root 2:", c / q)

#3rd Question
#Write a code fragment that takes two float command-line arguments, and writes True if both are strictly between 0 and 1 and False otherwise.
NO1= float(input("Number1: "))
NO2 = float(input("Number2: "))
if 0 < NO1 < 1:
    stdio.writeln("True")
else:
    stdio.writeln("False")
if 0 < NO2 < 1:
    stdio.writeln("True")
else:
    stdio.writeln("False")

#4th Question
#Improve your solution to the "wind chill" exercise from Section 1.2 by adding code to check that the values of the
# command-line arguments fall within the ranges of validity of the formula, and also adding code to write an error message
# if that is not the case.
t = float(input("Fahrenheit: "))  # Fahrenheit
v = float(input("Mph: "))   # Miles per hour
if not (-50 <= t <= 50 and 3 <= v <= 120):
    print("Error: temperature must be between -50 and 50 F")
    print("and wind speed must be between 3 and 120 mph.")
else:
    wind_chill = (
        35.74
        + 0.6215 * t
        + (0.4275 * t - 35.75) * v ** 0.16
    )
    print(wind_chill)

#5th Question
#What is the value of j after each of the following code fragments is executed?
#a. j = 0
#   for i in range(0, 10):
#       j += i
#b. j = 1
#   for i in range(0, 10):
#      j += j
#c. for j in range(0, 10):
#       j += j
#Solution:
#a = 0+0+1+2+3+4+5+6+7+8+9 = 45
#b = (Burda j in range yazmadığından dolayı j kendini 10 kez hep topluyor ve bundan dolayı cevap 2**10 oluyor.) 1024
#c = (Burda bir değerini üstüne koymadığı için en son işlemi yapıp bırakıyor.) 18

#6th Question
#Redesign tenhellos.py to compose a program that accepts the number of lines to write as a command-line argument.
#You may assume that the argument is less than 1000. Hint: consider using i % 10 and i % 100 to determine whether to use
# st, nd, rd, or th for writing the ith Hello.
n = int(input("Number: "))
if not 0 <= n < 1000:
    exit("Error: n must be between 0 and 999.")
for i in range(1, n + 1):
    if 11 <= i % 100 <= 13:
        suffix = "th"
    elif i % 10 == 1:
        suffix = "st"
    elif i % 10 == 2:
        suffix = "nd"
    elif i % 10 == 3:
        suffix = "rd"
    else:
        suffix = "th"
    print(f"{i}{suffix} Hello")

#7th Question
#Compose a program that, using one for loop and one if statement, writes the integers from 1000 (inclusive) to 2000
# (exclusive) with five integers per line. Hint: use the % operator.
for i in range(1000, 2000):
    print(i, end="") #Burdaki end="" fonksiyonu sayılırın yan yana yazmasını sağlar.

    if i % 5 == 4: #Burda 5 tane sayının yan yana olmasını sağlar.
        print()
    else:
        print(" ", end="")

#8th Question
#Generalizing the "uniform random numbers" exercise from Section 1.2,
# compose a program that accepts an integer n as a command-line argument, uses random.random() to write n uniform random
# numbers between 0 and 1, and then writes their average value, their minimum value, and their maximum value.
n = int(input("n: "))
if n <= 0:                                   #n burda kaçta rastgele ondalıklı sayı üreteciğini belirler
    exit("Error: n must be positive.")

total = 0.0
minimum = float("inf") #En küçük sayıyı bulmak için başlangıç değeri.
maximum = float("-inf") #En büyük sayıyı bulmak için başlangıç değeri.

for i in range(n):
    value = random.random() #random.random() metodu rastgele ondalıklı sayı üretir.
    print(value)

    total += value
    minimum = min(minimum, value)
    maximum = max(maximum, value)

print("Average:", total / n)
print("Minimum:", minimum)
print("Maximum:", maximum)

#9th Question
#Compose a program that writes a table of the values of log n, n, n log n, n2, and n3 for
#n = 2, 4, 8, 16, 32, 64, 128. Use tabs ('\t' characters) to line up columns.
print("log(n)\tn\tn*log(n)\tn^2\tn^3") # \t karakteri üstte yazdığı gibi araya boşluk koyuyor.

for exponent in range(1, 8):
    n = 2 ** exponent
    log_n = math.log(n)

    print(
        f"{log_n:.4f}\t" #.4f komutu 4 ondalıklı basamak değerini yazılmasına sağlar.
        f"{n}\t" 
        f"{n * log_n:.4f}\t"
        f"{n ** 2}\t"
        f"{n ** 3}"
    )

#10th Question
#What are m and n after the following code is executed?
#n = 123456789
#m = 0
#while n != 0:
#    m = (10 * m) + (n % 10)
#    n //= 10
#Solution: m = 987654321, n = 0

#11th Question
#What are m and n after the following code is executed?
n = 123456789
m = 0
while n != 0:
    m = (10 * m) + (n % 10)
    n //= 10
    print(m)
    print(n)
#Solution:
#9
#12345678
#98
#1234567
#987
#123456
#9876
#12345
#98765
#1234
#987654
#123
#9876543
#12
#98765432
#1
#987654321
#0

#11th Question:
#What does this code write?
f = 0
g = 1
for i in range(0, 16):
    f = f + g
    g = f - g
    stdio.writeln(f)
#Solution:
#1
#1
#2
#3
#5
#8
#13
#21
#34
#55
#89
#144
#233
#377
#610
#987

#12th Question:
#Compose a program that takes a command-line argument n and writes all the positive powers of 2 less than or equal to n.
#Make sure that your program works properly for all values of n. (Your program should write nothing if n is negative or zero.)
n = int(input("n1: "))
power = 1
while power <= n:
    print(power)
    power *= 2

#13th Question
#Compose a version of divisorpattern.py that uses while loops instead of for loops.
n = int(input("nih: "))
i = 1
while i <= n:
    j = 1
    while j <= n:
        if i % j == 0 or j % i == 0:
            print("* ", end="")
        else:
            print("  ", end="")

        j += 1
    print(i)
    i += 1

#14th Question
#Unlike the harmonic numbers, the sum 1/12 + 1/22 + ... + 1/n2 does converge to a constant as n grows to infinity.
#(Indeed, the constant is π2/6, so this formula can be used to estimate the value of π.)
#Which of the following for loops computes this sum? Assume that n is the integer 1000000 and total is a float initialized to 0.0.
for i in range(1, n+1):
    total += 1 / (i*i) #a: / performs true division, even with integer operands.
for i in range(1, n+1):
    total += 1.0 / i*i # b: Multiplication and division are evaluated left to right, so 1.0 / i*i means (1.0 / i) * i, approximately 1.
for i in range(1, n+1):
    total += 1.0 / (i*i) # c: The parentheses give the intended denominator.
for i in range(1, n+1):
    total += 1 / (1.0*i*i) #d: The denominator is also \(i^2\), represented as a float.

#15th Question
#Modify binary.py to create a program that takes i and k as command-line arguments and converts i to base k. Assume that
# k is an integer between 2 and 16. For bases greater than 10, use the letters A through F to represent the 11th through
# 16th digits, respectively.
number = int(input("number: "))
base = int(input("base: "))
if not 2 <= base <= 16:
    exit("Error: base must be between 2 and 16.")
digits = "0123456789ABCDEF"
value = abs(number) #value = abs(number) kodu, number değişkeninin mutlak değerini alıp value değişkenine atar.
result = ""
if value == 0:
    result = "0"
while value > 0:
    result = digits[value % base] + result #Bu kod genellikle bir sayıyı farklı bir sayı tabanına çevirmek için kullanılır.
    value //= base #Bu kod value değişkenini base'e böler, bölümün tam sayı kısmını alır ve tekrar value'ya atar.
if number < 0:
    result = "-" + result
print(result)

#16th Question
#Compose a program named that accepts a positive integer command-line argument n,
# places the binary representation of n into a string, and then writes the string.
n = int(input("n: "))
binary = "" #Neden binaryı böyle yaptık çünkü binary değişkeninde binary sayıyı string olarak biriktireceğiz.
if n <= 0:
    exit("Error: n must be positive.")
else:
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
        print(binary)

#17th Question
#Write a program that traces a gambler's ruin simulation by writing a line after each bet that has one asterisk(yıldız işareti)
# corresponding to each dollar held by the gambler.
stake = int(input("stake: "))
goal = int(input("goal: "))
if not 0 < stake < goal:
    exit("Error: require 0 < stake < goal.")
cash = stake
while 0 < cash < goal:
    if random.random() < 0.5:
        cash += 1
    else:
        cash -= 1
    print("*" * cash) #aradaki yıldız değeri stringi baştaki yıldız stringini çarpıyor.

#18th Question:
#Write a Python program called gambler.py that simulates a gambler who starts with an initial amount of money (stake)
# and aims to reach a target amount (goal).
#The program should:
#Accept three integer command-line arguments: stake, goal, and trials.
#Simulate trials independent experiments.
#In each experiment, the gambler starts with stake dollars.
#For each bet, the gambler has a 50% chance of winning $1 and a 50% chance of losing $1.
#Continue betting until the gambler either loses all their money ($0) or reaches the goal.
#Count the total number of bets and the number of successful experiments.
#Print the percentage of wins and the average number of bets per experiment.
stake = int(input("stake: "))
goal = int(input("goal: "))
trials = int(input("trials: "))
bets = 0
wins = 0
for t in range(trials):
    cash = stake
    while cash > 0 and cash < goal:
        bets += 1
        if random.randrange(1, 2) == 0:
            cash += 1
        else:
            cash -= 1
    if cash == goal:
        wins += 1
print(str(100 * wins//trials) + '% wins')
print('Avg # bets: ' + str(bets//trials))

#19th Question
#Write a Python program called factors.py that accepts a positive integer n as a command-line argument and prints its
# prime factors in ascending order.
#Your program should:
#Start with the smallest prime factor, 2.
#Use a while loop to check whether n is divisible by the current factor.
#If the factor divides n evenly, print the factor and divide n by it.
#Repeat this process until the factor no longer divides n.
#Increase the factor and continue until all prime factors have been found.
#Print each prime factor, including repeated factors, separated by spaces.
n = int(input("n: "))
factor = 2
while factor*factor <= n:
    while n % factor == 0:
        # Cast out and write factor.
        n //= factor
        stdio.write(str(factor) + ' ')
    factor += 1
    # Any factors of n are greater than or equal to factor.
if n > 1:
    stdio.write(n)
stdio.writeln()

#20th Question (***)
#Compose a program that takes one integer command-line argument n and writes a two dimensional n-by-n checker board pattern
# with alternating spaces and asterisks, like the following 4-by-4 pattern.
#* * * *
# * * * *
#* * * *
# * * * *
n = int(input("n: "))
if n < 0:
    exit("Error: n must be nonnegative.")
for row in range(n):
    if row % 2 == 1:
        print(" ", end="")
    for column in range(n):
        print("* ", end="")
    print()

#21th Question (***)
#Write a Python program that takes an integer command-line argument n and prints a hollow triangle of height n and base width 2 * n - 1.
#Use nested for loops with variables named row and column. Print asterisks along the two sides and the base, leaving the interior empty.
#    *
#   * *
#  *   *
# *     *
#*********
n = int(input("n: "))
for row in range(n):
    for column in range(2 * n - 1):
        if (
            column == n - 1 - row
            or column == n - 1 + row
            or row == n - 1
        ):
            print("*", end="")
        else:
            print(" ", end="")
    print()

#22th Question (***)
#Write a Python program that takes a positive integer command-line argument n and prints a filled diamond using asterisks.
#The diamond should have 2 * n - 1 rows and a maximum width of 2 * n - 1 asterisks. Use nested for loops with variables named row and column.
#n = 5
#    *
#   ***
#  *****
# *******
#*********
# *******
#  *****
#   ***
#    *
n = int(input("n: "))
for row in range(2 * n - 1):
    distance = abs(n - 1 - row) #abs kodu sonucu pozitif yapar.
    for column in range(2 * n - 1):
        if distance <= column <= 2 * n - 2 - distance:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#23th Question
#Compose a program that generates a point that is randomly distributed in the unit disk, but without using a break statement.
#Compare your solution to the one given at the end of this section.
x = random.uniform(-1, 1) #.uniform() metodu -1 ile 1 arasında rastgele bir ondalıklı sayı üretir.
y = random.uniform(-1, 1)
while x * x + y * y > 1:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
print(x, y)