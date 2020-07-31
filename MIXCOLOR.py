t = int(input())
while t:
    ans = 0
    n = int(input())
    n_colors = list(map(int, input().split()))
    dict_n = {}

    if len(n_colors) == len(set(n_colors)):
        print(0)
    else:
        for i in n_colors:
            dict_n[i] = 0
        for _ in n_colors:
            dict_n[i] += 1
        for key,value in dict_n.items():
            ans += value - 1
        print(ans)
    t-=1
