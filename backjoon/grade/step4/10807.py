N: int = int(input())
nums: list[int] = list(map(int, input().split()))
v: int = int(input())

result = 0
for num in nums:
    if num == v:
        result += 1

print(result)
