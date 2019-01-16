c = int(input())
for _ in range(c):
    d = int(input())
    n = input().split()
    a = []
    for i in n:
        a.append(int(i))
    b = min(a)
    l = d - 1
    print(b * l)
