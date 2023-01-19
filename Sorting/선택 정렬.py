array = [7,5,9,0,3,1,6,2,4,8]
def selction_sort(l):
    for i in range(len(l)):
        min_i = i
        for j in range(i+1,len(l)):
            if l[min_i]>l[j]:
                l[min_i], l[j] = l[j], l[min_i]
    return l
print(selction_sort(array))
