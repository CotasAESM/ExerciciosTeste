a=[2,3,4,5,6]
b=[]
a=[x**3 for x in a ]
print(a)
b=[x for x in a if x%8==0]
print(b)