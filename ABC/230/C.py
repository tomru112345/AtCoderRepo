N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

l_b = [["." for j in range(S - (R - 1))] for i in range(Q - (P - 1))]

min_1 = max(1 - A, 1 - B)
max_1 = min(N - A, N - B)
min_2 = max(1 - A, 1 - N)
max_2 = min(N - A, B - 1)

min_1 = max(min_1, min(1 + (P - 1) - A, 1 + (R - 1) - B))
# max_1 = min(max_1, max(-A + 1 + (P - 1), -B + 1 + (R - 1)))
min_2 = max(min_2, min(-A + 1 + (P - 1), B - 1 - (R - 1)))
# max_2 = min(max_2, max(-A + 1 + (P - 1), B - 1 - (R - 1)))

for k in range(min_1, max_1 + 1):
    l_b[(A + k - 1) - (P - 1)][(B + k - 1) - (R - 1)] = "#"

for k in range(min_2, max_2 + 1):
    l_b[(A + k - 1) - (P - 1)][(B - k - 1) - (R - 1)] = "#"

for i in l_b:
    print(*i, sep='')
