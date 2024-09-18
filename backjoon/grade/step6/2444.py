num = int(input())
for i in range(num):
    print(' ' * (num - i - 1), end='')
    print('*' * (i * 2 + 1))

for i in range(1, num):
    print(' ' * i, end='')
    print('*' * ((num - i) * 2 - 1))
