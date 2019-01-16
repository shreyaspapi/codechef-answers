max1,max2 = 0,0
lead1,lead2 = 0,0
s,t = 0,0
n = int(input())
for i in range(n):
    p1,p2 = map(int,input().split())
    s += p1
    t += p2
    if s>t:
        lead1 = s-t
    else:
        lead2 = t-s
    if lead1 > max1:
        max1 = lead1
    elif lead2 > max2:
        max2 = lead2
if (max1>max2):   
    print(1,max1)
else:
    print(2,max2)
