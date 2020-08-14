n = int(input())
s = list(str(n))
s.sort(reverse =True)
a = 0
answer=""
for i in s:
    a += int(i)
if a%3==0 and '0' in s:
    for i in s:
        answer+=i
    print(int(answer))
else:
    print(-1)
            
