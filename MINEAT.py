import math

t = int(input())

for _ in range(t):
    n, h = list(map(int, input().split()))
    n_space = list(map(int, input().split()))
    if h == len(n_space):
        print(max(n_space))
        continue
    sum_n_space = sum(n_space)
    average = math.ceil(sum_n_space/n)
    devide_hr = math.floor(sum_n_space/h)
    
    for i in range(devide_hr, average+10000000):
        new_list = []
        for j in n_space:
            while j > i:
                j = j - i
                new_list.append(i)
        if len(new_list)+n <= h:
            print(i)
            break
