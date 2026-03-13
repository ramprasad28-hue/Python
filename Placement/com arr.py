a1 = [10,20,30,40,50]
a2 = [1,2,3,3,4,50]
f = False
for i in range(len(a1)):
    if a1[i] in a2:
        print(a1[i], end=" ")
        f = True
if not f:
    print(-1)