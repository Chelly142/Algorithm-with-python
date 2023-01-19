def solution(N, stages):
    answer = []
    done = len(stages) #수행중인 애들
    for i in range(1,N+1):
        if(done == 0):
            answer.append((0,i))
            continue
        answer.append((stages.count(i)/done,i))
        done -= stages.count(i)
    a = sorted(answer, key = lambda x:(-x[0],x[1]))
    return [i[1] for i in a]
