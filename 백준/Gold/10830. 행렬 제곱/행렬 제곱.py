import sys
import copy
input = sys.stdin.readline

n, b= map(int,input().split())
A = [list(map(int,input().split())) for _ in range(n)]
def matrix_multiplication(a,b):
    answer = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            x=0
            for k in range(n):
                x += (a[i][k]*b[k][j])%1000
            answer[i][j] = x%1000
    return answer

def dnc(a, power):
    if power == 1:
        for i in range(n):
            for j in range(n):
                A[i][j] %= 1000
        return A
    x = dnc(a,power//2) 

    if power%2==0:
        return matrix_multiplication(x,x)
    else:
        return matrix_multiplication(matrix_multiplication(x,x),A)

for i in dnc(A,b):
    print(*i)