# 길이 별로 하나의 단어에서 나올 수있는 코스 후보 뽑고 사용 코스에 스트링으로 저장(set 사용)
# orders
from itertools import combinations

def has_candi(c,o):
    for i in c:
        if i not in o:
            return False
    return True

def solution(orders, course):
    answer = []
    d = {}
    for c in course:
        d[c] = []
        
    # 각 코스 길이 별 후보 코스 
    for o in orders:
        for c in course:
            if len(o)<c:
                continue
            d[c]+=list(combinations(sorted(o),c)) 
    # 코스 길이별 대회
    for c in course:
        max_count = 0
        winners =set()
        for candi in d[c]:
            count = 0
            for o in orders:
                if has_candi(candi, o):
                    count+=1
            if count>1:
                if max_count <count:
                        winners = set([candi])
                        max_count = count
                elif max_count == count:
                    winners.add(candi)
        answer+=list(sorted(winners))

    for i in range(len(answer)):
        s = ""
        for c in answer[i]:
            s+=c
        answer[i] = s

    
    return  sorted(answer)