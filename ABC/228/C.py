N, K = map(int, input().split())
P = [list(map(int, input().split())) for l in range(N)]

L = [0] * N
num = 0
True_L = ["No"] * N

for i in P:
    L[num] = [i[0] + i[1] + i[2], num]
    num += 1

L = sorted(L, key=lambda x: x[0], reverse=True)

border = L[K - 1][0]

for i in range(len(L)):
    if (L[i][0]) >= border:
        True_L[L[i][1]] = "Yes"
    else:
        if (L[i][0] + 300) >= border:
            True_L[L[i][1]] = "Yes"

for i in range(len(True_L)):
    print(True_L[i])
