t = int(input())

while t:
    a,b = list(map(int, input().split()))
    if a > b:
        b = a + b
        print(a,b)
    else:
        a = a + b
        print(b,a)
    t -= 1
