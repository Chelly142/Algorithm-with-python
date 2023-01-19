def solution(board, moves):
    l =[]
    answer = 0
    for i in moves:
        j=0
        a=0
        while(a==0 and j<len(board)): 
            a = board[j][i-1]
            j+=1
        board[j-1][i-1] = 0 
        if a!=0:
            l.append(a)
        l.reverse()
        if len(l)>1 and l[0]==l[1]:
            del l[0:2]
            answer+=2
        l.reverse()
    return answer
