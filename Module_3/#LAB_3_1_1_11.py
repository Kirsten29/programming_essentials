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
    print("Spathiphyllum! Not", name, + "!")
