a=[4,5,6,7,0,1,2]
target=1
st=0
end=-1
for i in range(len(a)):
    if a[st]>target:
        st+=1
    elif a[end]>target:
        end-=1
        st+=1
    else:
        print(st,end)
        break
if target==a[st] and a[end]:
    print('True')
else:
    print('False')
#it is only work on a target=1,4 otherwise it will won't work