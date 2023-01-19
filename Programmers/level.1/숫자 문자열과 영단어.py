def solution(s):
    num = [str(i) for i in range(0,10)]
    str_num =["zero","one","two","three","four","five","six","seven","eight","nine"]
    tkn =""
    answer=[]
    for i in s:
        tkn = tkn + i
        if tkn in num:
            answer.append(num.index(tkn))
            tkn=""
        if tkn in str_num:
            answer.append(str_num.index(tkn))
            tkn=""
    return sum(answer[i]*(10**(len(answer)-i-1)) for i in range(len(answer)))



num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
