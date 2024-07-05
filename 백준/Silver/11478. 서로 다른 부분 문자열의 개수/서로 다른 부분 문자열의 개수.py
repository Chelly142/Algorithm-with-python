import sys
input = sys.stdin.readline
# n,m = map(int,input().split())
# n = int(input())
s = input().rstrip()
k = set()
answer = 0
for i in range(len(s)):
    for j in range(i,len(s)):
        k.add(s[i:j+1])




print(len(k))