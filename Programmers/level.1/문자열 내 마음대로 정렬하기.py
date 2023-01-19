def solution(strings, n):
    answer = []
    for i in strings:
        i = i[n] + i
        answer.append(i)
    answer.sort()
    answer = [j[1:] for j in answer]
    return answer
