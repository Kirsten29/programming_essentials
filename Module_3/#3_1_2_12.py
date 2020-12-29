#3_1_2_12
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

1
2
3
4
else: 5

i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

else: 5

#3_1_2_13
for i in range(5):
    print(i)
else:
    print("else:", i)

0
1
2
3
4
else: 4


i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)

else: 111

"The loop's body won't be executed here at all. Note: we've assigned the i variable before the loop.
"Run the program and check its output.
"When the loop's body isn't executed, the control variable retains the value it had before the loop.
"Note: if the control variable doesn't exist before the loop starts, it won't exist when the execution 
"reaches the else branch.