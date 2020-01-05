try:
    data ={'A':1,'B':3,'C':3}
    print(10/0)
except KeyError :
    print('Exception has occured while accessing dictionary using key')
except ZeroDivisionError :
    print('Divide by Zero Exception ')
finally:
    print('Finally clean-up will always get executed')