#3_1_2_4
for i in range(10):
    print("The value of i is currently", i)

for i in range(2, 8):
    print("The value of i is currently", i)

#3_1_2_5
for i in range(2, 8, 3): #(2, 8, 4)(2, 8, 2)
    print("The value of i is currently", i

pow = 1
for exp in range(16):
    print("2 to the power of", exp, "is", pow)
    pow *= 2

#3_1_2_6
# Do you know what Mississippi is? Well, it's the name of one 
# of the states and rivers in the United States. The Mississippi 
# River is about 2,340 miles long, which makes it the second longest 
# river in the United States (the longest being the Missouri River). 
# It's so long that a single drop of water needs 90 days to travel its entire length!

# The word Mississippi is also used for a slightly different purpose: to count mississippily.

# If you're not familiar with the phrase, we're here to explain to you what it means: 
# it's used to count seconds.

# The idea behind it is that adding the word Mississippi to a number when counting 
# seconds aloud makes them sound closer to clock-time, and therefore "one Mississippi, two Mississippi, three Mississippi" will take approximately an actual three seconds of time! It's often used by children playing hide-and-seek to make sure the seeker does an honest count.


# Your task is very simple here: write a program that uses a for loop to 
# "count mississippily" to five. Having counted to five, the program should 
# print to the screen the final message "Ready or not, here I come!"

# Use the skeleton we've provided in the editor.

import time

# Write a for loop that counts to five.
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    # Body of the loop - use: time.sleep(1)

# Write a print function with the final message:
import time

for i in range(1, 6):
    print(i, "Mississippi")
    time.sleep(1)

#3_1_2_7
# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")

# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")
# The break instruction:
# Inside the loop. 1
# Inside the loop. 2
# Outside the loop.

# The continue instruction:
# Inside the loop. 1
# Inside the loop. 2
# Inside the loop. 4
# Inside the loop. 5
# Outside the loop.

#3_1_2_8
largestNumber = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter += 1
    if number > largestNumber:
        largestNumber = number

if counter != 0:
    print("The largest number is", largestNumber)
else:
    print("You haven't entered any number.")
#
largestNumber = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largestNumber:
        largestNumber = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print("The largest number is", largestNumber)
else:
    print("You haven't entered any number.")

#3_1_2_9
# Design a program that uses a while loop and continuously 
# asks the user to enter a word unless the user enters 
# "chupacabra" as the secret exit word, in which case the 
# message "You've successfully left the loop." should be printed 
# to the screen, and the loop should terminate.

# Don't print any of the words entered by the user. 
# Use the concept of conditional execution and the break statement.
secret_word = "chupacabra"
counter = 0

while True:
    secret_word = str(input("Enter the secret word: "))
    if secret_word == "chupacabra":
        break


if counter != 0:
    secret_word = str(input("Enter the secret word: "))
else:
    print("You've succesfully left the loop.")
# -> 
while True:
    word = input("You're stuck in an infinite loop! Enter the secret word to leave the loop: ")
    if word == "chupacabra":
        break
print("You've successfully left the loop!")

#3_1_2_10
# The continue statement is used to skip the current block 
# and move ahead to the next iteration, without executing the statements inside the loop.

# It can be used with both the while and for loops.

# Your task here is very special: you must design a vowel eater! Write a program that uses:

# a for loop;
# the concept of conditional execution (if-elif-else)
# the continue statement.
# Your program must:

# ask the user to enter a word;
# use userWord = userWord.upper() to convert the word entered by the user to 
# upper case; we'll talk about the so-called string methods and the upper() method very soon 
# - don't worry;
# use conditional execution and the continue statement to "eat" the following vowels 
# A, E, I, O, U from the inputted word;
# print the uneaten letters to the screen, each one of them on a separate line.
# Test your program with the data we've provided for you.

# Test data
# Sample input: Gregory
# Expected output:
# G
# R
# G
# R
# Y

# Sample input: abstemious
# Expected output:

# B
# S
# T
# M
# S

# Sample input: IOUEA
# Expected output:

--------------
# Prompt the user to enter a word
# and assign it to the userWord variable.

for letter in userWord:
    # Complete the body of the for loop.

userWord = input("Enter your word: ")
userWord = userWord.upper()

for letter in userWord:
    if letter == "A":  #if letter in "AEIUO":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        print(letter)

#3_1_2_11
# Your task here is even more special than before: you must redesign 
# the (ugly) vowel eater from the previous lab (3.1.2.10) and create 
# a better, upgraded (pretty) vowel eater! Write a program that uses:
# a for loop;
# the concept of conditional execution (if-elif-else)
# the continue statement.
# Your program must:

# ask the user to enter a word;
# use userWord = userWord.upper() to convert the word entered by the user 
# to upper case; we'll talk about the so-called string methods and the upper() 
# method very soon - don't worry;
# use conditional execution and the continue statement to "eat" the following 
# vowels A, E, I, O, U from the inputted word;
# assign the uneaten letters to the wordWithoutVovels variable and print the variable to the screen.
# Look at the code in the editor. We've created wordWithoutVovels and assigned an 
# empty string to it. Use concatenation operation to ask Python to combine selected 
# letters into a longer string during subsequent loop turns, and assign it to the 
# wordWithoutVovels variable.

# Test your program with the data we've provided for you.
# Test data
# Sample input: Gregory
# Expected output:
# GRGRY

# Sample input: abstemious
# Expected output:
# BSTMS

# Sample input: IOUEA
# Expected output:
wordWithoutVowels = ""
userWord = input("Enter your word: ")
userWord = userWord.upper()

for letter in userWord:
    if letter in "AEIOU":
        continue
    wordWithoutVowels = wordWithoutVowels + letter #wordWithoutVowels += letter

print(wordWithoutVowels)

#3_1_2_12
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

#3_1_2_13
for i in range(5):
    print(i)
else:
    print("else:", i)
#
i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)
#When the loop's body isn't executed, the control variable retains the value it had before the loop.

#3_1_2_14
# Listen to this story: a boy and his father, a computer programmer, 
# are playing with wooden blocks. They are building a pyramid.
# Their pyramid is a bit weird, as it is actually a pyramid-shaped wall - 
# it's flat. The pyramid is stacked according to one simple principle: each 
# lower layer contains one block more than the layer above.
# The figure illustrates the rule used by the builders:
      []        #fysiek bouwen zou volgens bottum-up gaan, vanuit de computer gaat het top-down.
     [][]       #laag 1 = 1 blok, laag 2= 2 blokken, laag 3 = 3 blokken. nr laag = aantal benodigde blokken
    [][][]

# Your task is to write a program which reads the number of blocks the builders have, 
# and outputs the height of the pyramid that can be built using these blocks.

# Note: the height is measured by the number of fully completed layers - if the 
# builders don't have a sufficient number of blocks and cannot complete the next 
# layer, they finish their work immediately.

# Test your code using the data we've provided.
# Sample input: 6
# Expected output: The height of the pyramid: 3

# Sample input: 20
# Expected output: The height of the pyramid: 5

# Sample input: 1000
# Expected output: The height of the pyramid: 44

# Sample input: 2
# Expected output: The height of the pyramid: 1

blocks = int(input("Enter the number of blocks: "))

height = 0
while blocks > height:
    height = height + 1 #height += 1
    blocks = blocks - height #blocks -= height
    

print("The height of the pyramid:", height)

#3_1_2_15
In 1937, a German mathematician named Lothar Collatz formulated an intriguing 
# hypothesis (it still remains unproven) which can be described in the following way:
# take any non-negative and non-zero integer number and name it c0;
# if it's even, evaluate a new c0 as c0 ÷ 2;
# otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
# if c0 ≠ 1, skip to point 2.
# The hypothesis says that regardless of the initial value of c0, it will always go to 1.
# Of course, it's an extremely complex task to use a computer in order to prove the 
# hypothesis for any natural number (it may even require artificial intelligence), 
# but you can use Python to check some individual numbers. Maybe you'll even find the 
# one which would disprove the hypothesis.
# Write a program which reads one natural number and executes the above steps as long 
# as c0 remains different from 1. We also want you to count the steps needed to achieve 
# the goal. Your code should output all the intermediate values of c0, too.
# Hint: the most important part of the problem is how to transform Collatz's idea into 
# a while loop - this is the key to success.
# Test your code using the data we've provided.

Test Data

Sample input: 15
Expected output:

46
23
70
35
106
53
160
80
40
20
10
5
16
8
4
2
1
steps = 17

Sample input: 16
Expected output:

8
4
2
1
steps = 4

Sample input: 1023
Expected output:

3070
1535
4606
2303
6910
3455
10366
5183
15550
7775
23326
11663
34990
17495
52486
26243
78730
39365
118096
59048
29524
14762
7381
22144
11072
5536
2768
1384
692
346
173
520
260
130
65
196
98
49
148
74
37
112
56
28
14
7
22
11
34
17
52
26
13
40
20
10
5
16
8
4
2
1
steps = 62

