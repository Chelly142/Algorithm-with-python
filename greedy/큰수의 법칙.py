N, M, K = map(int,input().split())
l = list(map(int,input().split()))
l.sort()
s=0
count = M//(K+1)
s += l[-2]*count
s += l[-1]*(M-count)
print(s)


'''
두번째 풀이
n,m,k = map(int,input().split())
data = list(map(int,input().split()))
first = max(data)
data.remove(first)
second = max(data)
if m//k ==0:
  print(m*first)
else :
  print((m//k)*first*k + (m%k)*second)
  '''