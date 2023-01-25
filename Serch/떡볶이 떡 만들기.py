n, m = map(int,input().split())
d = list(map(int,input().split()))
start=0
end = max(d)
while start<=end:
    s=0
    mid = (start+end)//2
    for i in d:
        if i>mid:
            s+=(i-mid)
    if s<m:
        end = mid-1
    else:
        result = mid
        start = mid +1

print(result)
#일정한 범위내에서 최대값을 구하는경우는 이진탐색을 이용하는 것을 고려
#재귀로 구현하지말고 반복문으로 구현해야 수월 함
#반복 학습할 것

n,m = map(int,input().split())
dd = list(map(int,input().split()))
def bs(array,target):
  end = max(array)
  start = 0
  answer = 0
  while start<=end:   
    sum = 0
    mid = (start+end)//2
    for i in array:
      cut_dd = i-mid
      if cut_dd<0:
        cut_dd = 0
      sum += cut_dd
    if m > sum:
      end = mid - 1    
    else:
      answer = mid
      start = mid + 1
      
  return answer
print(bs(dd,m))
