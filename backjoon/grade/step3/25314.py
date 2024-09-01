N: int = int(input().strip())
result: str = 'int'
loop = N // 4
for i in range(loop):
    result = 'long ' + result

print(result)