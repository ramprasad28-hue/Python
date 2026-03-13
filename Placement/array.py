a=[1,0,4,0,0,5,0,6,0,0,2]
i=0
j=1
n=len(a)
while j<n:
    if a[i]!=0:
        i+=1
    else:
        temp=a[i]
        a[i]=a[j]
        a[j]=temp
        j+=1
if j<n and a[j]==0:
    j=+1
print(*a)
