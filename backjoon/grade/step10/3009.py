class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


if __name__ == '__main__':
    T = 3

    point_list = []
    for _ in range(T):
        x, y = map(int, input().split())
        point_list.append(Point(x, y))

    x_list = []
    for point in point_list:
        x_list.append(point.x)

    y_list = []
    for point in point_list:
        y_list.append(point.y)

    x = list(filter(lambda x: x_list.count(x) == 1, x_list))[0]
    y = list(filter(lambda x: y_list.count(x) == 1, y_list))[0]

    print(x, y)
