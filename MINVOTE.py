t = int(input())

while t:
    n = int(input())
    n_space = list(map(int, input().split()))
    new_list = []
    for _ in range(n):
        new_list.append(0)
    
    for i in range(n):
        for j in range(i+1, n):
            if i+1 == j:
                new_list[j] += 1
            elif n_space[i] >= sum(n_space[i+1:j]):
                new_list[j] += 1
            else:
                break
    
    n_space = n_space[::-1]
    
    for i in range(n):
        for j in range(i+1, n):
            if i+1 == j:
                new_list[n-(j+1)] += 1
            elif n_space[i] >= sum(n_space[i+1:j]):
                new_list[n-(j+1)] += 1
            else:
                break
    print(*new_list)
    t-=1
