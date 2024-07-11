import sys
input = sys.stdin.readline
answer = []
dp = {}
def w(a,b,c):
    if (a,b,c) in dp:
        return dp[(a,b,c)]
    elif a <= 0 or b <= 0 or c <= 0:
        dp[(a,b,c)] = 1
        return 1
    elif a > 20 or b > 20 or c > 20:
        dp[(a,b,c)] = w(20,20,20)
        return dp[(a,b,c)]

    elif a < b and b < c:
        dp[(a,b,c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[(a,b,c)]
    else:
        dp[(a,b,c)] =w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[(a,b,c)]
while True:
    a,b,c = map(int,input().split())
    if a==b==c==-1:
        break
    else:
        answer.append((a,b,c,w(a,b,c)))
for a,b,c,v in answer:
    print(f"w({a}, {b}, {c}) = {v}")