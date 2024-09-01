import sys

T = int(sys.stdin.readline().strip())
nums = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(T)]

for num in nums:
    sys.stdout.write(str(num[0] + num[1]) + '\n')