N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

r = [0] * (N + 1)
for i in range(N):
    r[i] = B[i]

num = 0
for i in range(N + 1):
    if (i > 0):
        if ((r[i] + r[i - 1]) >= A[i]):
            if (A[i] - r[i - 1]) > 0:
                tmp = A[i] - r[i - 1]
                r[i - 1] = 0
                if (tmp - r[i]) > 0:
                    num += (r[i] + r[i - 1])
                    r[i] = 0
                else:
                    num += A[i]
                    r[i] = r[i] - tmp
            else:
                r[i - 1] = r[i - 1] - A[i]
                num += A[i]
        else:
            num += (r[i] + r[i - 1])
            r[i] = 0
    else:
        if (r[i] - A[i] >= 0):
            r[i] = r[i] - A[i]
            num += A[i]
        else:
            num += r[i]
            r[i] = 0

print(num)
