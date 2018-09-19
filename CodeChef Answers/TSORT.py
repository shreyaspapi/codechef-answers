t = int(input())
lst = []
while t:
    lst.append(int(input()))
    t -= 1
lst = sorted(lst)
for i in lst:
    print(i)
