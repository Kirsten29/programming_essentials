word = "Python"
for letter in word:
    print(letter, end="*")
---
word = "Python"
for letter in word:
    print(letter, sep="*")
-------
while True:
    print("Stuck in an infinite loop.")
---
counter = 5
while counter > 2:
    print(counter)
    counter -= 1
-------
text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")
---
text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")
-------
n = 0

while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")

print()

for i in range(0, 3):
    print(i)
else:
    print(i, "else")
-------
for i in range(3):
    print(i, end=" ") # outputs: 0 1 2

for i in range(6, 1, -2):
    print(i, end=" ") # outputs: 6, 4, 2
-------
Create a for loop that counts from 0 to 10, and prints odd numbers to the screen. 
Use the skeleton below:
for i in range(1, 11):
    # line of code
        # line of code = 
for i in range (1, 11):
    if i % 2 != 0:
        print(i)
-------
Create a while loop that counts from 0 to 10, and prints odd numbers to the screen. 
Use the skeleton below:
x = 1
while x < 11:
    # line of code
        # line of code
    # line of code =
x = 1
while x < 11:

-------
Create a program with a for loop and a break statement. T
he program should iterate over characters in an email address, exit the loop when it 
reaches the @ symbol, and print the part before @ on one line. Use the skeleton below:

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        # line of code
    # line of code =
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")
-------
Create a program with a for loop and a continue statement. The program should iterate 
over a string of digits, replace each 0 with x, and print the modified string to the screen. 
Use the skeleton below:

for digit in "0165031806510":
    if digit == "0":
        # line of code
        # line of code
    # line of code =
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")
-------
What is the output of the following code?

n = 3

while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n) 
4
3
2
0
-------
What is the output of the following code?

n = range(4)

for num in n:
    print(num - 1)
else:
    print(num)
-1
0
1
2
3
-------
What is the output of the following code?

for i in range(0, 6, 3):
    print(i)
0
3