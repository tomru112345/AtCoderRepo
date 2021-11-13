N, K, A = map(int, input().split())
# N 人
# A 番目
# K 枚
tmp = 0

if ((K - ((N - A) + 1)) > 0):
    tmp = (K - ((N - A) + 1))
    if (tmp > N):
        while(tmp > N):
            tmp = tmp % N
    if (tmp == 0):
        tmp = N
else:
    tmp = A + K - 1

print(tmp)
