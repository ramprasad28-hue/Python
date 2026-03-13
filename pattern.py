n=int(input())
for i in range(1,n):
    num=i
    for j in range(1,i+1):
        if i%2==0:
             print(num,end=" ")
             num+=2
        else:
            print(num,end=' ')
            num+=2
    print()