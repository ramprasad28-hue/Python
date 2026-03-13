a=input().split()
d={}
for i in a:
    d[i]=d.get(i,0)+1
rev={}
for k,v in d.items():
    rev[v]=rev.get(v,[])+[k]
print(rev)