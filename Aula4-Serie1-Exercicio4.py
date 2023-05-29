mat=[[2,3,4],[7,9,10],[12,13,14]]
list=[]
list=[y for x in mat for y in x if y%2==0]
print(list)