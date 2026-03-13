n=int(input())
for _ in range(n):
    m=int(input())
    cou=0
    for i in range(1,n+1):
        cou+=bin(i).count('1')
print(cou)
