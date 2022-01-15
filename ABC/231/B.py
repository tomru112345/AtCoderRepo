import collections

N = int(input())
S = []
for _ in range(N):
    S.append(input())

T = collections.Counter(S)
num = 0
sr = ""
for i in S:
    if num < T[i]:
        num = int(T[i])
        sr = i
print(sr)
