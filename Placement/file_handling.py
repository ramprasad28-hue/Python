import os
'''with open('input.txt','r') as file:
    text=file.read()
print(text)
with open('bio.txt','w') as f:
    t=f.write('my name is Ram')
print(t)
with open('bio.txt','a') as f:
    t=f.write('CSE')
print(t)'''
'''if os.path.exists('ini.py'):
    os.remove('ini.py')
    print('File Removed successfully')
else:
    print('File doesnt exsits')'''
'''with open('ini.py','x')as file:
    with open('in.py','w') as file:
        t=file.write('Hi')
print(t)'''
'''with open('input.txt','r') as file:
    text=file.read()
print(text)'''
with open("file1.txt","w") as file1:
    text=file1.write("This is a sample file.")
lst=[]
for i in range(4):
    name=input("Enter the name of the employee:")
    lst.append(name+'\n')
print("Data is writtern into the file successfully")