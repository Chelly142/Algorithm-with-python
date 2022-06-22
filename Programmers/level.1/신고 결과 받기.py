def solution(id_list, report, k):
    answer = [0]*len(id_list)
    report = set(report)
    reporter =[]
    reported= []
    warned = []
    for i in report:
        a = i.split(' ')
        reporter.append(a[0])
        reported.append(a[1])
    for i in id_list:
        if k<=reported.count(i):
            warned.append(i)
    
    for i,j in zip(reporter,reported):
        if j in warned:
            answer[id_list.index(i)] +=1
        
    
    return answer
