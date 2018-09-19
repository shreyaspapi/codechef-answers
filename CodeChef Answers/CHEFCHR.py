t = int(input())
while t:
    a = input()
    count = 0
    li = []
    ans = 0
    for i in range(4,len(a)+1):
        li.append(a[count:i])
        count += 1
        
    for i in li:
        if "c" in i and "h" in i and "e" in i and "f" in i:
            ans += 1
    if ans == 0:
        print("normal")
    else:
        print("lovely",ans)
    
    t -= 1
