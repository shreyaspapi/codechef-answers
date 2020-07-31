t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())
    s = list(map(int, input().split()))
    count_a = 0
    count_b = 0
    for p in range(n):
        if s[p]%a == 0:
            count_a += 1
        elif s[p]%b == 0:
            count_b += 1
    if count_a > count_b:
        print("BOB")
    else:
        print("ALICE")
"""
2
5 3 2
1 2 3 4 5
5 2 4
1 2 3 4 5
""" 