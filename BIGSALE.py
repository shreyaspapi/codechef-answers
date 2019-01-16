t = int(input())
while t:
    n = int(input())
    loss = 0
    for _ in range(n):
        p,q,d = list(map(int, input().split()))
        percent_num = d/100 * p
        sale_price = p + percent_num
        percent_num = d/100 * sale_price
        customer_price = sale_price - percent_num
        l = p - customer_price
        loss += l*q
        
    print(loss)
    t-=1
