
n,k = list(map(float, input().split(" ")))
count = 0
while n:
    if int(input()) % k == 0:
        count += 1
    n -= 1
    
print(count)
