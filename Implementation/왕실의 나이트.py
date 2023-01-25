c = [i for i in range(1,9)]
l = [i for i in range(97,105)]

s = input()
result = 0
a = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,1),(2,-1)]
'''
for i in a:
    if ord(s[0])+i[0] in l and int(s[1])+i[1] in c:
        result +=1
print(result)

s = input()
x = s[0]
y = s[1]


list1 = ['a','h','1','2']
list2 = ['b','g','2','7']
list3 = ['c','d','e','f','3','4','5','6']

if x in list3 and y in list3:
  result = 8
elif x in list1 and y in list1:
  result = 2
elif x in list2 and y in list2:
  result = 4
else:
  result = 3
print(result)'''