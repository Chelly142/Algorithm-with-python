n = int(input())
array = []
for i in range(n):
    name ,s = input().split()
    array.append((name,s))
def k(data):
    return int(data[1])
array.sort(key = k)
for i in array:
    print(i[0],end=' ')
