import itertools

nums = [1, 2, 3]
print(list(itertools.combinations(nums, 2)))

from collections import defaultdict
d = defaultdict(int)
d["a"] += 1
print(d)


from collections import deque
dq = deque([1, 2, 3])
dq.appendleft(0)
print(dq)
from itertools import cycle

colors = ["red", "blue"]
for c in cycle(colors):
    print(c)
    break
from itertools import repeat

for i in repeat(10, 5):
    print(i)

from itertools import permutations

print(list(permutations([1,2,3], 2)))

from itertools import accumulate

print(list(accumulate([1,2,3,4])))
