from collections import Counter

def solution(participant, completion):
    a = Counter(participant)
    b = Counter(completion)
    for k,v in a.items():
        if b[k]!=v:
            answer = k
    return answer
