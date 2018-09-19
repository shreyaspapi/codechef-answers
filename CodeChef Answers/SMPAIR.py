t = int(input())
while t:
    n = int(input())
    a = list(map(int, input().split()))
    c = sum(a)
    for i in range(n):
        for j in range(n):
            if i < j:
                b = a[i] + a[j]
                if c > b:
                    c = b
    print(c)
    t-=1
