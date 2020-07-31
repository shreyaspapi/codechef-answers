t = int(input())
while t:
    n=int(input())
    c=s=e=m=h=0
    for _ in range(n):
        a = input()
        if a == "cakewalk":
            c += 1
        elif a == "simple":
            s += 1
        elif a == "easy":
            e += 1
        elif a in ["easy-medium", "medium"]:
            m += 1
        else:
            h+= 1
    if c and s and e and m and h:
        print("Yes")
    else:
        print("No")
    t-=1
