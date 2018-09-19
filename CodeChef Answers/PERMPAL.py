import re
from itertools import permutations
t = int(input())

def find_index(string, g):
    num = []
    d = {}
    for i in string:
        d[i] = [m.start() for m in re.finditer(i, g)] 
    for i in range(len(string)):
        num.append(d[string[i]][0] + 1)
        del d[string[i]][0]
    num = list(map(str, num))
    
    return " ".join(num)
        
    
while t:
    a = input()
    per = [''.join(p) for p in permutations(a)]
    
    for i in per:
        if i == i[::-1]:
            print(find_index(i, a))
            break
    else:
        print(-1)
    t -= 1
