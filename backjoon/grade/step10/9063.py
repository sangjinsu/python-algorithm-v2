import math

if __name__ == '__main__':
    n = int(input())

    x_list = list()
    y_list = list()
    for _ in range(n):
        x, y = map(int, input().split())
        x_list.append(x)
        y_list.append(y)
    width = max(x_list) - min(x_list)
    height = max(y_list) - min(y_list)
    square = width * height
    print(square)
