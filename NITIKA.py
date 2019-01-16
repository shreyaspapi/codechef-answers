t = int(input())
while t:
    n = input().split(" ")
    a = ""
    for i in range(len(n) - 1):
        a = a + n[i][0].title() + ". "
    a += n[-1].title()
    print(a)
    t-=1
