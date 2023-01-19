N, M, K = map(int,input().split())
l = list(map(int,input().split()))
l.sort()
s=0
count = M//(K+1)
s += l[-2]*count
s += l[-1]*(M-count)
print(s)
