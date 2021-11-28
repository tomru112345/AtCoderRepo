N, W = map(int, input().split())
ab = [map(int, input().split()) for _ in range(N)]
A, B = [list(i) for i in zip(*ab)]

L = []

for i in range(N):
    L.append([A[i], B[i]])

L = sorted(L, key=lambda x: x[0], reverse=True)

score = 0

for i in range(N):
    if L[i][1] <= W:
        W -= L[i][1]
        score += L[i][0] * L[i][1]
    else:
        score += L[i][0] * W
        print(score)
        exit()
print(score)
