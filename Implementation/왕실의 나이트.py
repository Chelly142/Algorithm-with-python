c = [i for i in range(1,9)]
l = [i for i in range(97,105)]

s = input()
result = 0
a = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,1),(2,-1)]

for i in a:
    if ord(s[0])+i[0] in l and int(s[1])+i[1] in c:
        result +=1
print(result)
