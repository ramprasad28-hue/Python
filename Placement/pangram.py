sen=input()
ch='aeiou'
f=0
for i in range(len(ch)):
    if str(i) in sen:
        f+=1
    else:
        pass
if f==1:
    print('True')
else:
    print('False')