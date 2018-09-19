t = int(input())
while t:
  n,k = list(map(int, input().split()))
  a = list(map(int, input().split()))
  a = sorted(a)
  l = n + k
  l=(l+1)//2 - 1
  print(a[l])
  t-=1
