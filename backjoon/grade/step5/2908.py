import sys

A, B = sys.stdin.readline().split()
result = ''
for i in range(2, -1, -1):
    if int(A[i]) > int(B[i]):
        result = A
        break
    elif int(B[i]) > int(A[i]):
        result = B
        break

if result == '':
    result = A

print(result[::-1])
