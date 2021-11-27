A, B = map(int, input().split())

A_s = str(A)[::-1]
B_s = str(B)[::-1]

min_len = min(len(A_s), len(B_s))

flag = False

for i in range(min_len):
    if (int(A_s[i]) + int(B_s[i]) > 9):
        flag = True
        if (flag):
            print("Hard")
            break

if (not flag):
    print("Easy")
