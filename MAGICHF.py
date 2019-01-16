t = int(input())

while t:
    n,x,s = list(map(int, input().split()))

    for _ in range(s):
        a, b = list(map(int, input().split()))
        if a == x:
            x = b
        elif b == x:
            x = a

    print(x)
    t -= 1
