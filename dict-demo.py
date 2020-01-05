data ={'Apple':30,'Banana':15,'Pumpkin':'28'}


print('Price of apple is {} '.format(data['Apple']))
for x in data.keys() :
    print(x)

for y in data.values() :
    print(y)

# Python == dictionary inside a dictionary is possible

emp ={'name':'Saurabh Chaturvedi','skills':['Spring Boot','Camunda','Jenkins']}


print(emp['skills'])

for e in emp :
    print(e)