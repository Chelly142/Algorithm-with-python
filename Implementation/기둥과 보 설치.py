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

from collections import deque
# 작업 무시 할지 안할지 판단하는 함수 can
# 기본적으로 보 기둥 상관없이 디딤이 되는 곳을 저장하는 리스트 check 보 사이 낀 보 조심
def can(now_build):
    for i in now_build:
        x = i[0]
        y = i[1]
        if i[2]==0:
            if y==0 or [x,y-1,0] in now_build or [x,y,1] in now_build or [x-1,y,1] in now_build:
                continue
            else:

                return False
        if i[2]==1:
            if [x,y-1,0] in now_build or [x+1,y-1,0] in now_build: 
                continue
            elif [x-1,y,1] in now_build and [x+1,y,1] in now_build:
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    now_build = []
    bf = deque(build_frame)
    while bf:
        work = bf.popleft()
        w = work[:3]
        if work[3] == 1:
            now_build.append(w)
            if not can(now_build):
                now_build = now_build[:-1]
        if work[3] == 0:
            if w in now_build:
                now_build.remove(w)
                if not can(now_build):
                    now_build.append(w)
    return sorted(now_build)
