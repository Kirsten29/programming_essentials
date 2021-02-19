3_1_6_3
myList[start:end]

To repeat:
start is the index of the first element included in the slice;
end is the index of the first element not included in the slice.

This is how negative indices work with the slice:

myList = [10, 8, 6, 4, 2]
newList = myList[1:-1]
print(newList)

The snippet's output is: [8, 6, 4].

If the start specifies an element lying further than the one described by the end 
(from the list's beginning point of view), the slice will be empty:

myList = [10, 8, 6, 4, 2]
newList = myList[-1:1]
print(newList)

The snippet's output is: [].
-------
3_1_6_4
If you omit the start in your slice, it is assumed that you want to get a slice beginning 
at the element with index 0.
In other words, the slice of this form:

myList[:end]

is a more compact equivalent of:

myList[0:end]
---
myList = [10, 8, 6, 4, 2]
newList = myList[:3]
print(newList)

This is why its output is: [10, 8, 6].

Similarly, if you omit the end in your slice, it is assumed that you want the slice 
to end at the element with the index len(myList).

In other words, the slice of this form:

myList[start:]

is a more compact equivalent of:

myList[start:len(myList)]

Look at the following snippet:

myList = [10, 8, 6, 4, 2]
newList = myList[3:]
print(newList)

Its output is therefore: [4, 2].
-------
3_1_6_5
As we've said before, omitting both start and end makes a copy of the whole list:

myList = [10, 8, 6, 4, 2]
newList = myList[:]
print(newList)
The snippet's output is: [10, 8, 6, 4, 2].
---
The previously described del instruction is able to delete more than just a list's element at once - it can delete slices too:

myList = [10, 8, 6, 4, 2]
del myList[1:3]
print(myList)

Note: in this case, the slice doesn't produce any new list!
The snippet's output is: [10, 4, 2].
---
Deleting all the elements at once is possible too:

myList = [10, 8, 6, 4, 2]
del myList[:]
print(myList)

The list becomes empty, and the output is: [].
---
Removing the slice from the code changes its meaning dramatically.

Take a look:

myList = [10, 8, 6, 4, 2]
del myList
print(myList)

The del instruction will delete the list itself, not its content.

The print() function invocation from the last line of the code will then cause a runtime error.

3_1_6_6
elem in myList returns True or False
elem not in myList returns True or False

myList = [0, 3, 12, 8, 2]

print(5 in myList)
print(5 not in myList)
print(12 in myList)

3_1_6_7
myList = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = myList[0]

for i in range(1, len(myList)):
    if myList[i] > largest:
        largest = myList[i]

print(largest)
---
myList = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = myList[0]

for i in myList[1:]:
    if i > largest:
        largest = i

print(largest)

3_1_6_8
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
toFind = 5 #het getal, niet de positie
found = False

for i in range(len(myList)):
    found = myList[i] == toFind
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")

---
The numbers that have been drawn are: 5, 11, 9, 42, 3, 49.

The question is: how many numbers have you hit?

The program will give you the answer:

drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)


