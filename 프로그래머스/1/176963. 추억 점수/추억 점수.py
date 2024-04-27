def solution(name, yearning, photo):
    answer = []
    dic = {}
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    for p in photo:
        k = 0
        for n in p:
            if n in dic.keys():
                k+=dic[n]
        answer.append(k)
    return answer