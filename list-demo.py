# lists in python can be heterogenous , unlike Java

data = [1,2,3,'A',10.56,True,3]

print(data[:2])
print(data[2:])
print(data[2:4])

data.append(57)  # adding an element to a python list
data.insert(0,'Python')
for x in data :
    print(x)

# Set in python , {Curly braces}

dataset ={1,2,2,2,3}

print('Printing elements in the set :')
for x in dataset :
    print(x)
