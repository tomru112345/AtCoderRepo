import collections

N, M = map(int, input().split())
ab = [map(int, input().split()) for _ in range(M)]
A, B = [list(i) for i in zip(*ab)]

T_a = collections.Counter(A)
T_b = collections.Counter(B)
for i in A:
    if T_a[i] >= 3:
        print("No")
        exit()
for i in B:
    if T_b[i] >= 3:
        print("No")
        exit()

for i in range(M):
    if 1 > A[i] or A[i] > N:
        print("No")
        exit()
    if 1 > B[i] or B[i] > N:
        print("No")
        exit()
    if A[i] > B[i]:
        print("No")
        exit()

print("Yes")
