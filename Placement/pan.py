def digit_sum(n):
    while n>=10:
        n = sum(int(digit) for digit in str(n))
    return n
n=int(input())
arr=list(map(int, input().split()))
res=''
for num in arr:
    d=digit_sum(num)
    if d%2!=0:
        res+=chr(d+96)
    else:
        res+=str(d)
print(res)