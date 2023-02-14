from itertools import combinations
def solution(numbers, target):
    answer = 0
    s = sum(numbers)
    new_target = s - target
    for i in range(1,s):
        combi = list(combinations(numbers,i))

        for c in combi:
            if target == s - 2*sum(c):
                answer+=1
    return answer
