t = int(input())


def f_x(x):
    return x ** 2 + 2 * x + 3


print(f_x(f_x(f_x(t) + t) + f_x(f_x(t))))
