def solution(arr):
    answer = []
    a = -1
    for i in arr:
        if a!= i:
            answer.append(i)
            a = i
    return answer
