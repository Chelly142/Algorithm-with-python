def solution(s):
    answer= 10000
    for cut in range(1,len(s)//2+1):
        cut_result =""
        cnt = 1
        i = 0
        while i+cut<=len(s):
            if s[i:i+cut]==s[i+cut:i+cut*2]:
                cnt+=1
                i+=cut
            elif cnt>1:
                cut_result += (str(cnt)+s[i:i+cut])
                cnt=1
                i+=cut
            else:
                cut_result += s[i]
                i+=1
                cnt=1
        cut_result += s[i:]
        print(cut_result)
        answer = min(answer,len(cut_result))
    return answer
 def solution(s):
    answer= 10000
    for cut in range(1,len(s)//2+1):
        cut_result =""
        cnt = 1
        l=[]
        for i in range(0,len(s)//cut):
            l.append(s[cut*i:cut*i+cut])
        if -len(s)%cut:
            l.append(s[-(len(s)%cut):])
        
        for i,v in enumerate(l):
            if i != len(l)-1 and v == l[i+1]:
                cnt+=1
                continue
            elif cnt >1:
                cut_result+=str(cnt)+v
                cnt =1
            else:
                cnt = 1
                cut_result+=v 
                
        answer = min(answer,len(cut_result))
    if len(s)==1:
        answer =1
    return answer
