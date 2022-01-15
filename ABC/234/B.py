N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]


class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def diff_cal(self, p2):
        tmp = ((p2.x - self.x) ** 2 + (p2.y - self.y) ** 2) ** (1 / 2)
        if (tmp < 0):
            tmp = - 1 * tmp
        return tmp

    # def print_self(self):
    #     print(f"{self.x}, {self.y}")


point_li = []

for i in range(N):
    point_li.append(Point(x[i], y[i]))
max_num = 0

for i in range(N):
    for j in range(N):
        if (i != j):
            tmp = point_li[i].diff_cal(point_li[j])
            if (max_num < tmp):
                max_num = tmp


print(max_num)
