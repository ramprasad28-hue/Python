T = int(input())  # Number of test cases
for _ in range(T):
    N = int(input())
    count = 0
    for i in range(1, N + 1):
        count += bin(i).count('1')  # Convert to binary and count 1s
    print(count)