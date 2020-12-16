x = float(input("Enter value for x: "))

# put your code here

print("y =", y)
#sample input 1, 10, 100, -5
#i:
x = float(input("Enter value for x: "))
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)

#Lab_2_1_6_11
"Your task is to prepare a simple code able to evaluate the end time of a period" 
"of time, given as a number of minutes (it could be arbitrarily large). The start time" 
"is given as a pair of hours (0..23) and minutes (0..59). The result has to be printed" 
"to the console."
#Sample input:
12
17
59
#Expected output: 13:16

#Sample input:
23
58
642
#Expected output: 10:40

#Sample input:
0
1
2939
#Expected output: 1:0


hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
# put your code here

mins = mins + dura
#print(mins % 60) 
#print(mins // 60)
hour = hour + mins // 60
print(hour % 24, ":", mins % 60, sep = "")