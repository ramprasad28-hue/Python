n = int(input())
arr = list(map(int, input().split()))
from collections import Counter
freq = Counter(arr)
print(n, end=" ")
if all(freq[x] == 1 for x in arr):
    for i in range(n - 1, -1, -1):
        print(i, end=" ")
else:
    for i in range(n):
        if freq[i] == 1:
            print(i, end=" ")
        else:
            print(0, end=" ")