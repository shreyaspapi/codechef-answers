t = int(input())
while t:
    m = int(input())
    l = list(map(int, input().split()))
    f=0
 
    k=len(l)//2
	
    if l.count(l[k])>1 or m%2==0 or l[0]!=1 or l[m-1]!=1:
        f=1
    for i in range(len(l)):
        if l[i]!=l[len(l)-i-1] and i!=k:
            f=1
    for i in range(0,len(l)-1,2):
        diff=l[i]-l[i+1]
        if abs(diff)!=1:
            f=1
    print('yes' if f==0  else 'no')
    
    t -= 1
