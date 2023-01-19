def solution(n, arr1, arr2):
    answer = []
    m1 = []
    m2 = []
    for i in arr1:
        s=''
        for j in range(n-1,-1,-1):
            if i//(2**j):
                s=s+'1'
            else:
                s=s+'0'
            i = i%(2**j) 
        m1.append(s)
    for i in arr2:
        s=''
        for j in range(n-1,-1,-1):
            if i//(2**j):
                s=s+'1'
            else:
                s=s+'0'
            i = i%(2**j)
        m2.append(s)
    for i,j in zip(m1,m2):
        s=''
        for a,b in zip(list(i),list(j)):
            if a=='1' or b=='1':
                s=s+'#'
            else:
                s=s+' '
        answer.append(s)

    return answer
