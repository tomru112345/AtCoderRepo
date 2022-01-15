N, Q = map(int, input().split())
A = list(map(int, input().split()))
x = [int(input()) for _ in range(Q)]

num = 0
min_x = min(x)

new_A = []

for i in A:
    if i >= min_x:
        new_A.append(i)

new_A = sorted(new_A, reverse=True)
N = len(new_A)

for i in x:
    num = 0
    for j in range(N):
        if (i > new_A[j]):
            num = (j)
            print(num)
            break
    if (N != 0 and num == 0):
        print(N)
    else:
        print(0)
