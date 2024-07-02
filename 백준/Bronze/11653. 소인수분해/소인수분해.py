import sys
input = sys.stdin.readline

# a, b, c = map(int, input().split())

n= int(input())
d=2
while d <=n:
    if n%d==0:
        print(d)
        n=n//d
    else:
        d+=1
