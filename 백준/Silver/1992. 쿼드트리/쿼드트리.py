import sys
input = sys.stdin.readline

#3:02
n = int(input())
image = [list(map(int,list(input().rstrip()))) for _ in range(n)]

def is_zippable(point, side_len):
    x,y = point
    pixel_sum =0
    for i in range(x,x+side_len):
        for j in range(y,y+side_len):
            pixel_sum+=image[i][j]
    return True if pixel_sum in [0,side_len**2] else False

def dnc(point, side_len):
    x,y = point
    
    if is_zippable(point, side_len):
        return str(image[x][y])
    
    next_side_len = side_len//2
    s1 = dnc((x,y), next_side_len)
    s2 = dnc((x,y+next_side_len), next_side_len)
    s3 =dnc((x+next_side_len,y), next_side_len)
    s4 = dnc((x+next_side_len,y+next_side_len), next_side_len)

    return "("+s1+s2+s3+s4+")"
    
print(dnc((0,0), n))
