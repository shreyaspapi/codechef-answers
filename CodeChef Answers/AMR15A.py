n = int(input())
even = []
odd = []

a = list(map(int, input().split()))
for i in a:
  if i%2 == 0:
    even.append(i)
  else:
    odd.append(i)

if len(even) > len(odd):
  print("READY FOR BATTLE")
else:
  print("NOT READY")
