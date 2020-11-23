def solution(clothes):
    answer = 1
    a =[]
    clothes.sort(key = lambda x:x[1])
    k=clothes[0][1]
    c=0
    for i in clothes:
        if i[1] != k:
            a.append(c)
            k =i[1]
            c = 1
        else:
            c+=1    
    a.append(c)
    for i in a:
        answer = answer*(i+1)
    return answer-1
