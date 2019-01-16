t = int(input())
while t:
    a,b = list(map(int, input().split()))
    c = a%b
    print(c)
    t -= 1
