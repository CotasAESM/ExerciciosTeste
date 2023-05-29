import enum
# class Days(enum.Enum):
#     Sun=1
#     Mon=2
#     Tue=3
#
# print ('The enum member as a string is: ',end='')
# print (Days.Mon)
#
# print ('The enum member as a repr is: ',end='')
# print (repr(Days.Sun))
#
# print ('The typo of enum member as a string is: ',end='')
# print (type(Days.Mon))
#
#
# print ('The name of enum member as a string is: ',end='')
# print (Days.Tue.name)

class Animal(enum.Enum):
    dog=1
    cat=2
    lion=3

print ('The enum member associated with value 2 is: ',end='')
print (Animal(2))
mem=Animal.dog #Recebe os dois valores da class o 1 e o dog

print ('The enum member associated with name lion is: ',end='')
print (Animal['lion'])

print ('The value associated with dog is: ',end='')
print (mem.value)


print ('The name associated with 1 is: ',end='')
print (mem.name)

if Animal.dog is Animal.cat:
    print('Dog and cat are same animals')
else:
    print('Dog and cat are diferent animals')

if Animal.lion != Animal.cat:
    print('Lion and cat are diferent')
else:
    print('Lion and cat are same')
