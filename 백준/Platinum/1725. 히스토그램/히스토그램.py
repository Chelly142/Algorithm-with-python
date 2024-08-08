import sys
input = sys.stdin.readline

n = int(input())
histogram = []
for _ in range(n):
    histogram.append(int(input()))

stack = []
maximum_area = [0]*n
answer = 0
for i in range(n):
    while stack and histogram[stack[-1]]>histogram[i]:
        histogram_index = stack.pop()
        maximum_area[histogram_index] += histogram[histogram_index]*(i-histogram_index-1)
    if stack:
        maximum_area[i] = histogram[i]*(i-stack[-1])
    else:
        maximum_area[i] = histogram[i]*(i+1)


    stack.append(i)
    # print(stack)
    # print(maximum_area)

while stack:
        histogram_index = stack.pop()
        maximum_area[histogram_index] += histogram[histogram_index]*(n-histogram_index-1)

    
print(max(maximum_area))
