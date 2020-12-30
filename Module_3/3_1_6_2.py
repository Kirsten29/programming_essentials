3_1_6_2
A slice is an element of Python syntax that allows you to make a brand new copy of a list, 
or parts of a list.

It actually copies the list's contents, not the list's name.

list1 = [1]
list2 = list1[:]
list1[0] = 2
print(list2)

ts output is [1].

This inconspicuous part of the code described as [:] is able to produce a brand new list.

One of the most general forms of the slice looks as follows:

myList[start:end]

As you can see, it resembles indexing, but the colon inside makes a big difference.

A slice of this form makes a new (target) list, taking elements from the source list - 
the elements of the indices from start to end - 1.

Note: not to end but to end - 1. An element with an index equal to end is the first element 
which does not take part in the slicing.

Using negative values for both start and end is possible (just like in indexing).

Take a look at the snippet:

myList = [10, 8, 6, 4, 2]
newList = myList[1:3]
print(newList)

The newList list will have end - start (3 - 1 = 2) elements - the ones with indices equal 
to 1 and 2 (but not 3).

The snippet's output is: [8, 6]

# Copying the whole list
list1 = [1]
list2 = list1[:]
list1[0] = 2
print(list2)

# Copying part of the list
myList = [10, 8, 6, 4, 2]
newList = myList[1:3]
print(newList)

[1]
[8, 6]

