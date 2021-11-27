A, B = map(int, input().split())

A_s = str(A)
B_s = str(B)
min_len = min(len(A_s), len(B_s))
max_len = max(len(A_s), len(B_s))

A_list = [0] * len(A_s)
B_list = [0] * len(B_s)

num = 0

for i in reversed(range(len(A_s))):
    A_list[(len(A_s) - 1) - i] = int(A_s[i])

for i in reversed(range(len(B_s))):
    B_list[(len(B_s) - 1) - i] = int(B_s[i])

for i in range(min_len):
    if (A_list[i] + B_list[i] > 9):
        num += 1
        if (num == 1):
            print("Hard")

if (num == 0):
    print("Easy")
