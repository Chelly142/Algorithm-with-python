array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

c =[0]*(max(array)+1)
for i in array:
    c[i]+=1
for i in range(len(c)):
    for j in range(c[i]):
        print(i,end=" ")
