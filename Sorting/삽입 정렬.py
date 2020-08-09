array = [7,5,9,0,3,1,6,2,4,8]

def insertion_sort(l):
    k =[l[0]]
    for i in range(1,len(l)):
        for j in range(i,0,-1):
            if l[j]<l[j-1]:
                l[j], l[j-1] = l[j-1], l[j]
            else:
                break
    return l
print(insertion_sort(array))
#두번째 요소 부터 비교 시작 왼쪽은 기본적으로 모두 정렬되어있다고 가정하고 왼쪽으로 한칸씩 비교해 만약 
#현재 비교 값이 더 작다면 바꿔 줌 만약 더 크다면 반복을 멈추고 다음 비교 시작 이중 반복문을 사용했으므로 
#시간 복잡도는 O(N^2)이지만 정렬이 어느정도 되어있는 경우에는 굉장히 빠름 
