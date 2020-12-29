3_1_4_8
numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

numbers.insert(1, 333)
print(numbers)#

[111, 7, 2, 1]
5
[111, 7, 2, 1, 4]
6
[222, 111, 7, 2, 1, 4]
[222, 333, 111, 7, 2, 1, 4]
-------
3_1_4_9
myList = [] # creating an empty list

for i in range(5):
    myList.append(i + 1)

print(myList)

[1, 2, 3, 4, 5]
---
myList = [] # creating an empty list

for i in range(5):
    myList.insert(0, i + 1)

print(myList)

[5, 4, 3, 2, 1]
-------
3_1_4_10
myList = [10, 1, 8, 3, 5]
total = 0

for i in range(len(myList)):
    total += myList[i]

print(total)
---
or:
myList = [10, 1, 8, 3, 5]
total = 0

for i in myList:
    total += i

print(total)
-------
3_1_4_11
variable1 = 1
variable2 = 2

variable2 = variable1
variable1 = variable2
---
variable1 = 1
variable2 = 2

auxiliary = variable1
variable1 = variable2
variable2 = auxiliary
---
variable1 = 1
variable2 = 2

variable1, variable2 = variable2, variable1
-------
3_1_4_12
myList = [10, 1, 8, 3, 5]

myList[0], myList[4] = myList[4], myList[0]
myList[1], myList[3] = myList[3], myList[1]

print(myList)

[5, 3, 8, 1, 10]
---
Will it still be acceptable with a list containing 100 elements? No, it won't.

Can you use the for loop to do the same thing automatically, 
irrespective of the list's length? Yes, you can.

myList = [10, 1, 8, 3, 5]
length = len(myList)

for i in range(length // 2):
    myList[i], myList[length - i - 1] = myList[length - i - 1], myList[i]

print(myList)

[5, 3, 8, 1, 10]
we've assigned the length variable with the current list's length 
(this makes our code a bit clearer and shorter)
we've launched the for loop to run through its body length // 2 times 
(this works well for lists with both even and odd lengths, because when 
the list contains an odd number of elements, the middle one remains untouched)
we've swapped the ith element (from the beginning of the list) with the one with 
an index equal to (length - i - 1) (from the end of the list); in our example, 
for i equal to 0 the (l - i - 1) gives 4; for i equal to 1, it gives 3 - this is 
exactly what we needed.