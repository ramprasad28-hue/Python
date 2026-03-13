t=int(input())
for _ in range(t):
    n,x,y=map(int,input().split())
    rounds=n.bit_length()-1
    total=(rounds*x)+((rounds-1)*y)
    print(total)