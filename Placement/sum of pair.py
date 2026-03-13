a=[1,2,3,4,5]
target=1
start=0
end=-1
for i in range(len(a)):
    ans=a[start]+a[end]
    if ans==target:
        print(ans)
        break
    elif ans<target:
        start+=1
    else:
        end-=1

