a=[[1,4],[2,5],[3,6],[7,10],[8,12]]
res=[]
prev=a[0]
cur=a[1]
for i in range(1,len(a)):
    if prev[1]>=cur[0]:
        prev[1]=max(prev[1],cur[1])
    else:
        res.append(prev)
        prev=cur
    if i+1<len(a):
        cur=a[i+1]  
res.append(prev)
print(res)