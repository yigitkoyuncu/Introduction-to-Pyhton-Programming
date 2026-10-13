#1.2 Exercises (Built-in Types of Data)
import stdio
import math
import sys
import random

# 1st Quastion
# Assume that a = 5 and b = 10.
# What are the values of a, b, and t after the following code executes? Explain why.
a = 5
b = 10

t = a
b = t
a = b
stdio.writeln(a)
stdio.writeln(b)
stdio.writeln(t)
#Solution : a = 5, b = 5, t = 5.

#2nd Quastion
# Compose a program that uses math.sin() and math.cos() to check that the value of cos2 θ + sin2 θ is approximately 1.0
#for any θ entered as a command-line argument. Just write the value. Why are the values not always exactly 1.0?
theta = float(sys.argv[1])
theta_in_rad = math.radians(theta)

val_of_sin = math.sin(theta_in_rad)
val_of_cos = math.cos(theta_in_rad)

result = (val_of_sin**2) + (val_of_cos**2)
sys.stdout.write(str(result)+ '\n')
#Solution:1.0

#3rd Question
#Suppose that a and b are booleans. Show that this expression evaluates to True:
#(not (a and b) and (a or b)) or ((a and b) or not (a or b))
for a in [True, False]:
    for b in [True, False]:
        result = (not (a and b) and (a or b)) or ((a and b) or not (a or b))
        print(a, b, result)
#Solution:True True True
         #True False True
         #False True True
         #False False True

#4th Question
#Simplify the following Boolean expression without changing its meaning.
#a = 8
#b = 8
#result = not (a < b) and not (a > b)
a = 8
b = 8
result = not (a < b) and not (a > b)
stdio.writeln(int(result))
#Solution:a==b

#5th Question
#What does each of these statements write? Explain each outcome.
stdio.writeln(2 + 3) #5
stdio.writeln(2.2 + 3.3) #5.5
stdio.writeln('2' + '3') #23
stdio.writeln('2.2' + '3.3') #2.23.3
stdio.writeln(str(2) + str(3)) #23
stdio.writeln(str(2.2) + str(3.3)) #2.23.3
stdio.writeln(int('2') + int('3')) #5
stdio.writeln(int('2' + '3')) #23
stdio.writeln(float('2') + float('3')) #5.0
stdio.writeln(float('2' + '3')) #23.0
stdio.writeln(int(2.6 + 2.6)) #5
stdio.writeln(int(2.6) + int(2.6)) #4

#6th Question
#Write a code that square roots
a = 1
b = 0
c = -25

root1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
root2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)

print(root1)
print(root2)
#Solution:5.0
         #-5.0

#7th Question
#What does stdio.writeln((1.0 + 2 + 3 + 4) / 4) write?
stdio.writeln((1.0 + 2 + 3 + 4) / 4) #2.5

#8th Question
#Suppose that a is 3.14159. What do each of these statements write? Explain each outcome.
a = 3.14159
stdio.writeln(a) #3.14159
stdio.writeln(a + 1.0) #4.14159
stdio.writeln(8 // int(a)) #2
stdio.writeln(8.0 / a) #2.5464812403910124
stdio.writeln(int(8.0 / a)) #2

#9th Question
#Describe the effect of writing sqrt instead of math.sqrt in quadratic.py.
x = 25
print(math.sqrt(x))
from math import sqrt
print(sqrt(x))
#Solution:Using import math requires math.sqrt(). To call sqrt() directly, you must import it using from math import sqrt.

#10th Question
#Does (math.sqrt(2) * math.sqrt(2) == 2) evaluate to True or False?
result = math.sqrt(2) * math.sqrt(2) == 2
print(result) #False
print(math.sqrt(2) * math.sqrt(2)) #2.0000000000000004

#11th Question
#Compose a program that takes two positive integers as command-line arguments and writes True if either evenly divides the other.
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
result = (a % b == 0) or (b % a == 0)
print(result)
#Solution:True / False

#12th Question
#Compose a program that takes three positive integers as command-line arguments and writes False if any one of them is
# greater than or equal to the sum of the other two and True otherwise.
#(Note: This computation tests whether the three numbers could be the lengths of the sides of some triangle.)
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))
result = (a + b > c) and (a + c > b) and (b + c > a)
print(result)
#Solution:True / False

#13th Question
#Give the value of a after the execution of each of the following sequences:
#PartA                 PartB                 PartC
#a = 1                 a = True              a = 2
#a = a + a             a = not a             a = a * a
#a = a + a             a = not a             a = a * a
#a = a + a             a = not a             a = a * a
# Part A
a = 1
a = a + a
a = a + a
a = a + a
print("A:", a)
# Part B
a = True
a = not a
a = not a
a = not a
print("B:", a)
# Part C
a = 2
a = a * a
a = a * a
a = a * a
print("C:", a)
#Solution:A: 8
#         B: False
#         C: 256

#14th Question
#A physics student gets unexpected results when using the code
#force = G * mass1 * mass2 / radius * radius
#to compute values according to the formula F = Gm1m2 / r2. Explain the problem and correct the code.
G = 9.81
mass1 = 10
mass2 = 20
radius = 5
force = G * mass1 * mass2 / (radius ** 2)
print(force) #78.45
#The original expression incorrectly multiplied by radius after dividing by it. The denominator must be radius ** 2.

#15th Question
#Suppose that x and y are two floats that represent the Cartesian coordinates of a point (x, y) in the plane.
#Give an expression that evaluates to the distance of the point from the origin.
x = float(input("Enter x: "))
y = float(input("Enter y: "))
distance = math.sqrt(x**2 + y**2)
print(distance)
#Solution:Input 3 and 4 → Output 5.0.

#16th Question
#Compose a program that takes two integers a and b from the command line and writes a random integer between a and b.
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
number = random.randint(a, b) #.randit is important for this code that code writes random int between a and b.
print(number)

#17th Question
#Compose a program that writes the sum of two random integers between 1 and 6 (such as you might get when rolling dice).
die1 = random.randint(1,6)
die2 = random.randint(1,6)
sum = die1 + die2
stdio.writeln("First die:" + str(die1) )
stdio.writeln("Second die:" + str(die2))
stdio.writeln("Sum: " + str(sum))

#18th Question
#Compose a program that takes a float t from the command line and writes the value of sin(2t) + sin(3t).
t = float(input("Enter t: "))
result = math.sin(2*t) + math.sin(3*t)
print(result)

#19th Question
#Compose a program that takes three floats x0, v0, and t from the command line, evaluates x0 + v0t - Gt2 / 2, and writes the result.
#(Note: G is the constant 9.80665. This value is the displacement in meters after t seconds when an object is thrown
# straight up from initial position x0 at velocity v0 meters per second.)
g = 9.80665
x0 = float(input("Enter initial position: "))
v0 = float(input("Enter initial velocity: "))
t = float(input("Enter time: "))
x = x0 + v0*t - (g*t**2)/2
print("Position:", x)

#20th Question
#Compose a program that takes two integers m and d from the command line and writes True if day d of month m is between
# March 20 and June 20, and False otherwise. (Interpret m with 1 for January, 2 for February, and so forth.)
m = int(input("Enter month: "))
d = int(input("Enter day: "))
result = ((m == 3 and d >= 20) or
          (m == 4) or
          (m == 5) or
          (m == 6 and d <= 20))
print(result)



