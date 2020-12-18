3_1_2_2
odd_numbers = 0
even_numbers = 0

number = int(input("Enter a number or type 0 to stop: "))

while number:   #== while number != 0:
    if number % 2:  #== if number % 2 == 1::
        odd_numbers += 1
    else:
        even_numbers +=1
    number = int(input("Enter a number or type 0 to stop: "))
    
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

counter = 5
while counter != 0: #== while counter:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)