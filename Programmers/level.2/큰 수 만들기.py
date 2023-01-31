def solution(number, k):
    n_list=[]
    answer = []
    for i in number:
        n_list.append(int(i))
    for v in n_list:  
        if k<=0:
            answer.append(v)
            continue
        t=1
        while k>=0:
            if k>0 and len(answer)-t>=0 and v > answer[len(answer)-t]:
                t+=1
                k-=1
            elif t!=1:
                answer[len(answer)-t+1] = v
                answer = answer[:len(answer)-t+2]
                break
            else:
                answer.append(v)
                break

    j =""                
    for i in answer:
        j+=str(i)
    if k>0:
        j=j[0:-k]
    return j
  '''
  큐와 스택을 사용해서 다시 푸세요
  '''
