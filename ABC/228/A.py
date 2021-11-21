S, T, X = map(int, input().split())

if (S > T):
    T += 24
if (S > X):
    X += 24
if (X >= S and (X + 1) <= T):
    print("Yes")
else:
    print("No")
