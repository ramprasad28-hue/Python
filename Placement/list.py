f=("Apple","orange","grapes")
fl=list(f)
fl[1]="Banana"
f=tuple(fl)
print(f)

a=(1,2,3)
b=list(a)
b[1]=100
a=tuple(b)
print(a)
