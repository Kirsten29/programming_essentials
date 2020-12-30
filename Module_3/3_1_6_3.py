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




