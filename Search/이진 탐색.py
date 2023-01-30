def binary_serch(array, target, start, end):
    if start>end:
        return None
    mid = (start+end)//2
    if array[mid] > target:
        end= mid-1
    if array[mid] < target:
        start=mid+1
    if array[mid] == target:
        return mid
    return binary_serch(array, target, start, end)
print(binary_serch([0,1,2,3,4,5,6,7,8,9], 4, 0, 9))
