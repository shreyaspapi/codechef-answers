n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

num_of_pairs = n + m - 1

li = []

def compare(g, l):
    return any(i[2] == g for i in l)

for item_ in a:
    if len(li) >= num_of_pairs:
        break
    for item in b:
        if [item_, item, item_ + item] not in li and compare(
            item_ + item, li
        ) == False:
            li.append([item_, item, item_ + item])

c = num_of_pairs

for i in li:
    if c == 0:
        break
    print(a.index(i[0]), b.index(i[1]))
    c = c - 1
