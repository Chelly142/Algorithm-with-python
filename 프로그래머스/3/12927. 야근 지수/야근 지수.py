import heapq
def solution(n, works):
    answer = 0
    hq = []
    for w in works:
        heapq.heappush(hq,w*-1)
    for i in range(n):
        m = heapq.heappop(hq)
        heapq.heappush(hq,m+1)
    for w in hq:
        if w<0:
            answer+=w*w
    return answer