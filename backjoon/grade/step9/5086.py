def solve(num1: int, num2: int) -> str:
    if num2 % num1 == 0:
        return 'factor'
    if num1 % num2 == 0:
        return 'multiple'
    return 'neither'


if __name__ == '__main__':
    while True:
        num, num2 = map(int, input().split())
        if num == 0 and num2 == 0:
            break
        print(solve(num, num2))
