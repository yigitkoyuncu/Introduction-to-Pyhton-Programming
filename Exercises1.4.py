#Excercises 1.4

#1st Question
#Compose a program that creates a one-dimensional array a containing exactly 1000 integers,
# and then attempts to access a[1000]. What happens when you run the program?
#Solution:IndexError

#2nd Question
#Write a Python code fragment that calculates the Euclidean distance between two one-dimensional
# arrays a and b, each containing n elements.
import math

total = 0
for i in range(n):
    total += (a[i] - b[i]) ** 2

distance = math.sqrt(total)
print(distance)

#3rd Question
#Compose a code fragment that reverses the order of a one-dimensional array of floats. Do not create another array to hold the result.
# Hint: Use the code provided earlier in this web page for exchanging two elements.
a = [1, 2, 3, 4, 5]
n = len(a)
for i in range(n // 2):
    temp = a[n - i - 1]
    a[n - i - 1] = a[i]
    a[i] = temp

#4th Question
#What is wrong with the following code fragment?
#a = []
#for i in range(10):
#    a[i] = i * i
#Solution:The list is initially empty, so accessing a[i] raises an IndexError. Use append() to add new elements.

#5th Question
#What does the following code fragment write?
#a = stdarray.create1D(10, 0)
#for i in range(10):
#   a[i] = 9 - i
#for i in range(10):
#   a[i] = a[a[i]]
#for v in a:
#   stdio.writeln(v)
#Solution:0 1 2 3 4 4 3 2 1 0

#6th Question
#What is a[] afater executing the following code fragment?
#n = 10
#a = [0, 1]
#for i in range(2, n):
#    a += [a[i-1] + a[i-2]]
#Solution:Fibonacci series

#7th Question
#Compose a code fragment that writes the contents of a two-dimensional array of bools, using * to represent
# True and a space to represent False. Include row and column numbers.
a = [[True, False, True],
     [False, True, False],
     [True, True, False]]
print("   ", end="")
for j in range(len(a[0])):
    print(j, end=" ")
print()

for i in range(len(a)):
    print(i, end="  ")
    for j in range(len(a[i])):
        if a[i][j]:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#8th Question
#Compose a program that takes an integer command-line argument n and writes n poker hands
# (five cards each) from a shuffled deck, separated by blank lines.
import sys
import random
n = int(sys.argv[1])
if n < 0 or n > 10:
    print("n must be between 0 and 10.")
    sys.exit()
ranks = ["2", "3", "4", "5", "6", "7", "8",
         "9", "10", "Jack", "Queen", "King", "Ace"]
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
deck = []
for rank in ranks:
    for suit in suits:
        deck.append(rank + " of " + suit)

random.shuffle(deck)
for i in range(n):
    for j in range(5):
        print(deck[5 * i + j])
    print()

#9th Question:
#Given a two-dimensional array a, write a code fragment that creates a copy named b. Do not use slicing or built-in copying methods.
# Assume that:
#a) a is square.
#b) a is rectangular.
#c) a is ragged.
a = [[1, 2],
     [3, 4, 5],
     [6]]
b = []
for i in range(len(a)):
    row = []
    for j in range(len(a[i])):
        row.append(a[i][j])
    b.append(row)
print(b)

#10th Question
#Given a rectangular two-dimensional array a, write a Python code fragment that prints its transpose (interchanging rows and columns).
a = [[1, 2, 3],
     [4, 5, 6]]
for j in range(len(a[0])):
    for i in range(len(a)):
        print(a[i][j], end=" ")
    print()

#11th Question
#Write a Python code fragment that transposes a square two-dimensional array b in place, without creating another array.
b = [[1, 2],
     [3, 4]]
n = len(b)
for i in range(n):
    for j in range(i + 1, n):
        temp = b[i][j]
        b[i][j] = b[j][i]
        b[j][i] = temp

#12th Question
#Given an m-by-n two-dimensional array a, write a code fragment that creates a new n-by-m array b containing the transpose of a.
a = [[1, 2, 3],
     [4, 5, 6]]
m = len(a)
n = len(a[0])
b = []
for j in range(n):
    row = []
    for i in range(m):
        row.append(a[i][j])
    b.append(row)

#13th Question
#Given two n-by-n boolean matrices a and b, write a code fragment that computes their product c, using or instead of
# addition and (and) instead of multiplication.
a = [[True, False],
     [True, True]]
b = [[False, True],
     [True, False]]
n = len(a)
c = []
for i in range(n):
    c.append([False] * n)
for i in range(n):
    for j in range(n):
        for k in range(n):
            c[i][j] = c[i][j] or (a[i][k] and b[k][j])

