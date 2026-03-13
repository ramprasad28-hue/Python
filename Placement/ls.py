def ls(a,t):
    for i in range(len(a)):
        if a[i]==t:
            return True
    return -1
t=int(input())
a=list(map(int,input().split()))
r=ls(a,t)
print(r)