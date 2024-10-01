class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    x, y, w, h = map(int, input().split())
    user_point = Point(x, y)
    distance_list = [abs(user_point.x - w), abs(user_point.y - h), user_point.x, user_point.y]

    print(min(distance_list))
