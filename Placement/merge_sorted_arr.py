a=[1,2,3,4]
b=[5,6,7,8]
n=len(a)
m=len(b)
x=[]
for i in range(n):
    for j in range(m):
        if a[i]<b[j]:
            x.append(a[i])
            x.append(b[j])
print(x)