a=list(map(int,input().split()))
target=int(input())
low=a[0]
high=a[-1]
ans=[]
for i in range(len(a)):
    mid=(low+high)//2
    if mid>target:
        mid+=1
        break
    elif mid==target:
        ans.append(mid)
        break
    else:
        low+=1
print(*ans)