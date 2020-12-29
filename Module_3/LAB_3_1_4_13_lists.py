LAB_3_1_4_13_lists
The Beatles were one of the most popular music group of the 1960s, and the 
best-selling band in history. Some people consider them to be the most influential 
act of the rock era. Indeed, they were included in Time magazine's compilation of the 
20th Century's 100 most influential people.
The band underwent many line-up changes, culminating in 1962 with the line-up of John Lennon, 
Paul McCartney, George Harrison, and Richard Starkey (better known as Ringo Starr).

Write a program that reflects these changes and lets you practice with the concept of lists. 
Your task is to:

step 1: create an empty list named beatles;
step 2: use the append() method to add the following members of the band to the list: John Lennon, 
Paul McCartney, and George Harrison;
step 3: use the for loop and the append() method to prompt the user to add the following members 
of the band to the list: Stu Sutcliffe, and Pete Best;
step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
step 5: use the insert() method to add Ringo Starr to the beginning of the list.

# step 1
print("Step 1:", beatles)

# step 2
print("Step 2:", beatles)

# step 3
print("Step 3:", beatles)

# step 4
print("Step 4:", beatles)

# step 5
print("Step 5:", beatles)


# testing list length
print("The Fab", len(beatles))
---
# step 1
beatles = []
print("Step 1:", beatles)
# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison") #beatles.append("John Lennon, Paul McCartney, 
#George Harrison")is korter, werkt maar  telt dan  maar 1 regel en komt niet uit op Fab 4
print("Step 2:", beatles)
# step 3
for member in range(2):
        beatleName = input("Enter a new Beatle name ")
        beatles.append(beatleName), #range = 2 dus doet dat 2x.
#for i in range(1): 
    #beatles.append("Stu Sutcliffe,Pete Best") user wordt hierbij niet naar input gevraagd. Werkt wel
print("Step 3:", beatles)
# step 4
del beatles[3] #of del[-1]
del beatles[3] #of del[-1] of del[3:5] = meest elegant maar niet meest duidelijk/voor de hand liggend.
#del beatles[-1] werkte ook vw stap 2
print("Step 4:", beatles)
# step 5
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)


# testing list length
print("The Fab", len(beatles))