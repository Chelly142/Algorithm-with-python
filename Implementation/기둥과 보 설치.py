def solution(n, build_frame):
    answer = []
    for i in build_frame:
        if i[3]==1:#생성
            if i[2]==0:#기둥
                if i[1]==0 or [i[0],i[1],1] in answer or  [i[0]-1,i[1],1] in answer or [i[0],i[1]-1,0] in answer:#기둥생성조건
                    answer.append([i[0],i[1],0])
            else: #보
                if [i[0],i[1]-1,0] in answer or [i[0]+1,i[1]-1,0] in answer or ([i[0]-1,i[1],1] in answer and [i[0]+1,i[1],1] in answer):
                    answer.append([i[0],i[1],1])
        else:#제거
            if i[2]==0:#기둥
                if [i[0],i[1]+1,1] in answer and [i[0]+1,i[1],0] not in answer and [i[0]+1,i[1]+1,1] not in answer:#오른쪽 보가 무너짐
                    continue
                if [i[0]-1,i[1]+1,1] in answer and [i[0]-1,i[1],0] not in answer and [i[0]-2,i[1]+1,1] not in answer:#왼쪽 보가 무너짐
                    continue
                if [i[0]-1,i[1]+1,1] not in answer and [i[0],i[1],1] not in answer and [i[0],i[1]+1,0]  in answer:#위 기둥이 무너짐
                    continue
                answer.remove([i[0],i[1],0])
            else:#보
                if [i[0]+1,i[1],1] in answer and ([i[0]+1,i[1]-1,0] not in answer and [i[0]+2,i[1],0] not in answer): #오른쪽 보가 무너짐
                    continue
                if [i[0]-1,i[1],1] in answer and ([i[0],i[1]-1,0] not in answer and [i[0]-1,i[1],0] not in answer): #왼쪽 보가 무너짐
                    continue
                if [i[0]+1,i[1],1] not in answer and [i[0]+1,i[1]-1,0] not in answer and [i[0]+1,i[1],0] in answer:#오른쪽 위 기둥 무너짐
                    continue
                if [i[0]-1,i[1],1] not in answer and [i[0],i[1]-1,0] not in answer and [i[0],i[1],0] in answer:#왼쪽 위 기둥 무너짐
                    continue
                answer.remove([i[0],i[1],1])
    answer.sort()
    return answer
