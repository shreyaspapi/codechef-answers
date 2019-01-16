a,b=map(float,input().split())
a = int(a)
if(a%5!=0 or a>(b-0.50)):
    print('%.2f'%b)
else:
    print('%.2f'%(b-a-0.50))
