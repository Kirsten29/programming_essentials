LAB_3_1_1_5
"Using one of the comparison operators in Python, write a simple two-line program"
"that takes the parameter n as input, which is an integer, and prints False if n is less than 100,"
"and True if n is greater than or equal to 100."

Test Data
Sample input: 55 Expected output: False

Sample input: 99 Expected output: False

Sample input: 100 Expected output: True

Sample input: 101 Expected output: True

Sample input: -5 Expected output: False

Sample input: +123 Expected output: True

n = int(input("Enter a number: "))
print(n >= 100)