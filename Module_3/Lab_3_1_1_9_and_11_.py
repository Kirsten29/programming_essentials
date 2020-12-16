#Lab_3_1_1_9
number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
number_3 = int(input("Enter the third number: "))
if number_1 > number_2:
    largest_number = number_1
elif number_3 > number_1:
    largest_number = number_3
else:
    largest_number = number_2
print("The largest number: ", largest_number)
#largest_number = max(number1, number2, number3)

#Lab_3_1_1_11
"Imagine that your computer program loves these plants. Whenever it receives
"an input in the form of the word Spathiphyllum, it involuntarily shouts to 
"the console the following string: "Spathiphyllum is the best plant ever!"

"Write a program that utilizes the concept of conditional execution, takes a string as input, and:

"prints the sentence "Yes - Spathiphyllum is the best plant ever!" to the screen if the 
"inputted string is "Spathiphyllum" (upper-case)
"prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
"prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.

"Test your code using the data we've provided for you. And get yourself a Spathiphyllum, too!

Test Data
Sample input: spathiphyllum Expected output: No, I want a big Spathiphyllum!

Sample input: pelargonium Expected output: Spathiphyllum! Not pelargonium!

Sample input: Spathiphyllum Expected output: Yes - Spathiphyllum is the best plant ever!""

name = input("Enter flower name: ")

if name == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif name == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not", name + "!")

#Lab_3_1_1_12
# Once upon a time there was a land - a land of milk and honey, inhabited by happy and prosperous people. 
# The people paid taxes, of course - their happiness had limits. The most important tax, 
# called the Personal Income Tax (PIT for short) had to be paid once a year, 
# and was evaluated using the following rule:

# if the citizen's income was not higher than 85,528 thalers, the tax was equal
# to 18% of the income minus 556 thalers and 2 cents (this was the so-called tax relief)
# if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, 
# plus 32% of the surplus over 85,528 thalers.
# Your task is to write a tax calculator.

# It should accept one floating-point value: the income.
# Next, it should print the calculated tax, rounded to full thalers. 
# There's a function named round() which will do the rounding for you - 
# you'll find it in the skeleton code in the editor.
# Note: this happy country never returns money to its citizens. 
# If the calculated tax is less than zero, it only means no tax at all 
# (the tax is equal to zero). Take this into consideration during your calculations.

# Look at the code in the editor - it only reads one input value and outputs a result, 
# so you need to complete it with some smart calculations.

# Test your code using the data we've provided.
# Test Data
# Sample input: 10000
# Expected output: The tax is: 1244.0 thalers

# Sample input: 100000
# Expected output: The tax is: 19470.0 thalers

# Sample input: 1000
# Expected output: The tax is: 0.0 thalers

# Sample input: -100
# Expected output: The tax is: 0.0 thalers
income = float(input("Enter the annual income: "))

#
# Put your code here.
#

tax = round(tax, 0)
print("The tax is:", tax, "thalers")

income = float(input("Enter the annual income: "))

if income <= 85528:
    tax = income * 0.18 - 556.02
else:
    tax = (income - 85528) * 0.32 + 14839.02 
    
if tax < 0.0:
    tax = 0.0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
#Lab_3_1_1_13
# As you surely know, due to some astronomical reasons, years may be leap or common. 
# The former are 366 days long, while the latter are 365 days long.

# Since the introduction of the Gregorian calendar (in 1582), the following rule is used to 
# determine the kind of year:

# if the year number isn't divisible by four, it's a common year;
# otherwise, if the year number isn't divisible by 100, it's a leap year;
# otherwise, if the year number isn't divisible by 400, it's a common year;
# otherwise, it's a leap year.
# Look at the code in the editor - it only reads a year number, and needs to be completed 
# with the instructions implementing the test we've just described.

# The code should output one of two possible messages, which are Leap year or Common year, 
# depending on the value entered.

# It would be good to verify if the entered year falls into the Gregorian era, 
# and output a warning otherwise: Not within the Gregorian calendar period. Tip: use the 
# != and % operators.

# Test your code using the data we've provided.

# Test Data
# Sample input: 2000
# Expected output: Leap year

# Sample input: 2015
# Expected output: Common year

# Sample input: 1999
# Expected output: Common year

# Sample input: 1996
# Expected output: Leap year

# Sample input: 1580
# Expected output: Not within the Gregorian calendar period

year = int(input("Enter a year: "))

#
# Put your code here.
#
year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period.")
elif year % 4 != 0:
    print("Common year")
elif year % 100 != 0:
    print("Leap year")
elif year % 400 != 0:
    print("Common year")
else:
    print("Leap year")
    
#
# Put your code here.
#