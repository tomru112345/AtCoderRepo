N, W = map(int, input().split())
ab = [map(int, input().split()) for _ in range(N)]
A, B = [list(i) for i in zip(*ab)]

L = []

for i in range(N):
    L.append([A[i], B[i]])

L = sorted(L, key=lambda x: x[0], reverse=True)

score = 0

for i in range(N):
    min_g = min(W, L[i][1])
    W -= min_g
    score += L[i][0] * min_g
    if (W <= 0):
        print(score)
        exit()

print(score)
