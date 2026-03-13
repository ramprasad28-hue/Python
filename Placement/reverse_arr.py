n=[1,2,3,4]
st=0
end=-1
for i in range(len(n)):
    temp=n[st]
    n[st]=n[end]
    n[end]=temp
    end-=1
    st+=1
    print(*n)