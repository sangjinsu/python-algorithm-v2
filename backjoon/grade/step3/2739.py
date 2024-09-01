N = int(input().strip())

if N < 1 or N > 9:
    raise ValueError('N is out of range')

for i in range(1, 10):
    print(f'{N} * {i} = {N * i}')
