t = int(input())
while t:
  a = str(input())
  if a == a[::-1]:
    print("wins")
  else:
    print("losses")
  
  t -= 1
