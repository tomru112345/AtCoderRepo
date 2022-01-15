N, X = map(int, input().split())
A = list(map(int, input().split()))

new_A = sorted(A, reverse=True)
print(new_A)
num = 0
num_dai = 0
for i in range(N):
    if new_A[i] <= X:
        num += (X // new_A)


print(num)
