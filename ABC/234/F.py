import itertools

S = input()
P = []
for i in range(1, len(S) + 1):
    P += list(itertools.permutations(S, i))

P = list(set(P))
print(len(P) % 998244353)
