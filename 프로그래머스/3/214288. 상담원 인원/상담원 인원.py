#12:50
from itertools import product
import heapq as hq
def simulation(mento_by_type, reqs):
    mento = [[0]*x for x in mento_by_type]
    waiting = 0
    for s,d,t in reqs:
        e = hq.heappop(mento[t-1])
        if s>=e:
            hq.heappush(mento[t-1],s+d)
        else:
            waiting+=(e-s)
            hq.heappush(mento[t-1],e+d)
    return waiting
def solution(k, n, reqs):
    mento_by_types = [ x for x in product(range(1,n+1),repeat = k) if sum(x)==n]    
    answer = 1e9
    for c in mento_by_types:
        answer = min(answer,simulation(c,reqs))
    return answer