X = int(input().strip())
N = int(input().strip())
receiptList = [list(map(int, input().strip().split())) for _ in range(N)]

result = 0
for receipt in receiptList:
    price = receipt[0]
    count = receipt[1]
    result += price * count

print('Yes' if result == X else 'No')