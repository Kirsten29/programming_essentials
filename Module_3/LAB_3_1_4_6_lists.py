LAB_3_1_4_6_lists
There once was a hat. The hat contained no rabbit, but a list of five numbers: 1, 2, 3, 4, and 5.

Your task is to:

write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user (step 1)
write a line of code that removes the last element from the list (step 2)
write a line of code that prints the length of the existing list (step 3.)

hatList = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.

# Step 2: write a line of code here that removes the last element from the list.

# Step 3: write a line of code here that prints the length of the existing list.

print(hatList)

hatList = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

hatReplace = int(input("Replace the middle number by entering an integer number: "))# Step 1: write a line of code that prompts the user
hatList[2] = hatReplace# to replace the middle number with an integer number entered by the user.
print(hatList)

del hatList[4] #or del hatList[-1] , -2 voor de 1 na laatste # Step 2: write a line of code here that removes the last element from the list.

print("The length of the existing list is", len(hatList))# Step 3: write a line of code here that prints the length of the existing list.

print(hatList)