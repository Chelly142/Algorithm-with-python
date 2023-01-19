def solution(array, commands):
    answer = []
    for i in commands:
        k = array[i[0]-1:i[1]]
        k.sort()
        answer.append(k[i[2]-1])
    return answer
