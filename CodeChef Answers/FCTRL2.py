t = int(input())
while t:
    count = 1
    for i in range(1,int(input())+1):
        count *= i
    print(count)
    t -= 1
