d = [0, 31,28,31,30,31,30,31,31,30,31,30,31]
x, y = map(int,input().split())
s = 0
for i in range(x):
    s += d[i]
s+=y
if s%7==1:
    print("MON")
elif s%7==2:
    print("TUE")
elif s%7==3:
    print("WED")
elif s%7==4:
    print("THU")
elif s%7==5:
    print("FRI")
elif s%7==6:
    print("SAT")
elif s%7==0:
    print("SUN")
