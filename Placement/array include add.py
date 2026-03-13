a = []
for i in range(5):
    try:
        num = int(input())
        a.append(num)
    except EOFError:
        break
print(a)
if len(a) > 2:  
    result = a[0] + a[2]
    print(result)
else:
    print("Not enough elements")
