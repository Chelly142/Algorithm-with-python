s = input()
l = list(map(int,s))
result = 0
for i in l:
    if i<=1 or result<= 1:
        result += i
    else:
        result *= i

print(result)
