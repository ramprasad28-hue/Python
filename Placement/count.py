from collections import Counter
arr = list(map(int, input().split()))
freq = Counter(arr)
print(freq)