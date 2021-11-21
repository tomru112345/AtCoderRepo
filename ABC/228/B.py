N, X = map(int, input().split())
A = list(map(int, input().split()))

L = [False] * len(A)
check = False
check_idx = X
num = 1
L[check_idx - 1] = True
while(check == False):
    next_idx = A[check_idx - 1]
    check = L[next_idx - 1]
    if (check == False):
        L[next_idx - 1] = True
        num += 1
    check_idx = next_idx
    check = False

print(num)
