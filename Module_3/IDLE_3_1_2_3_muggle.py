secret_number = 777

print(    #multi-line printing: print strings on multiple lines
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number = int(input("Enter a number: "))
while number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    number = int(input("Enter a number: ")
print("Well done, muggle! You are free now as the secret number is indeed:", secret_number)
