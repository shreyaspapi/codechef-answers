t = int(input())
while t:
    n = int(input())
    n_hand = list(map(int, input().split()))
    n_glove = list(map(int, input().split()))
    front = 0
    back = 0

    for i in range(n):
        if n_hand[i] <= n_glove[i]:
            front += 1
        if n_hand[i] <= n_glove[n-1-i]:
            back += 1

    if front == n == back:
        print("both")
    elif front == n:
        print("front")
    elif back == n:
        print("back")
    else:
        print("none")
    t-=1
