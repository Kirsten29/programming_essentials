#LAB-3_1_2_11
"Your task here is even more special than before: you must redesign the (ugly) vowel 
"eater from the previous lab (3.1.2.10) and create a better, upgraded (pretty) vowel 
"eater! Write a program that uses:

"a for loop;
"the concept of conditional execution (if-elif-else)
"the continue statement.
"Your program must:

"ask the user to enter a word;
"use userWord = userWord.upper() to convert the word entered by the user to upper case; we'll talk about the so-called string methods and the upper() method very soon - don't worry;
"use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
"assign the uneaten letters to the wordWithoutVovels variable and print the variable to the screen.
"Look at the code in the editor. We've created wordWithoutVovels and assigned an empty string to it. Use concatenation operation to ask Python to combine selected letters into a longer string during subsequent loop turns, and assign it to the wordWithoutVovels variable.

"Test your program with the data we've provided for you.

Sample input: Gregory
Expected output: GRGRY

Sample input: abstemious
Expected output: BSTMS

Sample input: IOUEA
Expected output:

 wordWithoutVovels = "" #Typo: wordWithoutVoWels

# Prompt the user to enter a word
# and assign it to the userWord variable


for letter in userWord:
    # Complete the body of the loop.

# Print the word assigned to wordWithoutVowels.

wordWithoutVowels = ""
userWord = input("Enter a word: ")# Prompt the user to enter a word
userWord = userWord.upper()# and assign it to the userWord variable

for letter in userWord:
    if letter in "AEIOU":
        continue
    wordWithoutVowels = wordWithoutVowels + letter
print(wordWithoutVowels)
    # Complete the body of the loop.

# Print the word assigned to wordWithoutVowels.