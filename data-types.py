x = 10
y = 10.5

isManager = True

singleQuotes = 'This is india'
doubleQuotes ="This is java"
tripleQuotes_multiline ='''Saurabh Chaturvedi
XYZ Enclave , Flat no. 305
WhiteFields , Bangalore
'''

singleQuotes = singleQuotes.upper()

print(singleQuotes)
print(doubleQuotes)
print(tripleQuotes_multiline)

devOps_options = "Docker Kubernetes Jenkins".split()

for devops_option in devOps_options:
    print(devops_option)
    print('ansible')
    print('terraform')
    print()

    print('Outside of loop')

# slicing in python

x = 'Unhappy'

print(x[2:])
print(x[2:5])

y = '12345678'
print(y[::2])   # printing alternate numbers in the list