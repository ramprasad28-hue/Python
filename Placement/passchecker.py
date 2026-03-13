import string
pas=input()
sym=string.punctuation
st=0
if len(pas)>=8:
    st+=1
if any(i.isdigit() for i in pas):
    st+=1
if any(i.isupper() for i in pas) and any(i.islower() for i in pas):
    st+=1
if any(i in sym for i in pas):
    st+=1
if st<=1:
    print("weak")
elif st==2:
    print("Medium")
elif st==3:
    print("Strong")
else:
    print("Very Strong")


