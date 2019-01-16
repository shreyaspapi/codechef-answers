t = int(input())

while t:
    num1, num2 = list(map(int, input().split()))
    i, temp = 10, 0
    total = num1 + num2
    while num1 or num2:
        if (num1 % 10) + (num2 % 10) > 9: temp += i
        num1, num2, i = num1 // 10, num2 // 10, i * 10
    print(total - temp)
    t-=1
