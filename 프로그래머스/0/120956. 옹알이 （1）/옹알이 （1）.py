def solution(babbling):
    answer = 0
    
    for b in babbling:
        buffer =""
        for l in b:
            buffer = buffer+l
            #완성이 안된 경우
            if l not in ["a","y","e","w","o","m"] or len(buffer)>3:
                break
            #완성이 된 경우
            if buffer == "aya":
                buffer =""
            if buffer == "ye":
                buffer =""
            if buffer == "woo":
                buffer =""
            if buffer == "ma":
                buffer =""
        else:
            if buffer == "":
                answer+=1
        
            
    return answer