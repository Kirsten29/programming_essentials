numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers) # printing original list content

Original list content: [10, 5, 7, 2, 1]

How do you change the value of a chosen element in the list?.
Let's assign a new value of 111 to the first element in the list. We do it this way:
numbers[0] = 111
print("\nPrevious list content: ", numbers)

Previous list content:  [111, 5, 7, 2, 1]

And now we want the value of the fifth element to be copied to the second element 
- can you guess how to do it?
numbers[1] = numbers[4]
print("New list content:", numbers)

New list content: [111, 1, 7, 2, 1]
-------
3_1_4_3
print("\nList length:", len(numbers)) # printing the list's length

List length: 5
-------
3_1_4_4
del numbers[1] # removing the second element from the list
print("New list's length:", len(numbers)) # printing new list length
print("\nNew list content:", numbers) # printing current list content

New list's length: 4
New list content: [111, 7, 2, 1]
