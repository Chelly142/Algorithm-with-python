import sys
input = sys.stdin.readline

#12:40 
n, m = map(int,input().split())
trees = list(map(int,input().split()))
start, end = 1, max(trees)
answer = 0
while start<=end:
    mid = (start+end)//2
    tree_container = 0
    for tree in trees:
        if tree>mid:
            tree_container += (tree-mid)
    if tree_container>=m:
        start = mid+1
    else:
        end = mid-1
print(end)