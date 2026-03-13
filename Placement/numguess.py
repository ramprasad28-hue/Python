import random
s=random.randint(1,100)
while True:
    n=int(input())
    if n<s:
        print("Too Low")
    elif n>s:
        print("Too high")
    else:
        print("correct")
        break
