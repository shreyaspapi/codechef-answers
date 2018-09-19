t = int(input())
while t:

    num = list(map(int, input().split()))
    num.remove(max(num))
    print(max(num))
    t -= 1
