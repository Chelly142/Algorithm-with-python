s = input()
l = list(map(int,s))
result = 0
for i in l:
    if i<=1 or result<= 1:
        result += i
    else:
        result *= i

print(result)

s = input()
answer = 0
for c in s:
  n = int(c)
  answer = max(answer*n,answer+n)
print(answer)
