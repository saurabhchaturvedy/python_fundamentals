x = 10
y = 20

if x>y :
    print('X is greater than Y')
else:
    print('X is smaller')

'''
If marks>=60 print First Division
If marks>=50 print Second Division
If marks>35 print Third Division
Else print Failed
'''

marks = input('Enter your marks')
marks = int(marks)
if marks >=60 :
    print('You have first division')
elif marks >=50 :
    print('You have second division')
elif marks >=35 :
    print('You have Third division')
else:
    print('Failed !')

# While loops in Python

data = 1

while data<=10 :
    print(data)
    data = data+1

# continue and break statements in python

data = [1,2,3,4,5]

a = 1
for x in data :
    if x==4 :
        continue
    a = a*x
    print("value of a is {} ".format(a))

datax = [6,7,8,9,10]
search = 8

for x in datax :
    if search==x :
        print('Value is found')
        break


        print('Outside the loop')



