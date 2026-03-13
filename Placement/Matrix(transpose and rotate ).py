n=int(input())
a=[]
b=[]
for _ in range(n):
    num=input().split()
    a.append(num)
for i in range(n):
    r=[]
    for j in range(n):
        r.append(a[j][i])
    b.append(r)
for row in b:
    print(row[-1::-1])