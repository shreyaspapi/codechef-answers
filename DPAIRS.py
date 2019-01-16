n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

num_of_pairs = n + m - 1

li = []

def compare(g, l):
    for i in l:
        if i[2] == g:
            return True
    return False

for i in range(len(a)):
    if len(li) >= num_of_pairs:
        break
    for j in range(len(b)):
        if ([a[i], b[j], a[i] + b[j]] not in li) and compare(a[i] + b[j] ,li) == False:
            li.append([a[i], b[j], a[i] + b[j]])

c = num_of_pairs

for i in li:
    if c == 0:
        break
    print(a.index(i[0]), b.index(i[1]))
    c = c - 1
