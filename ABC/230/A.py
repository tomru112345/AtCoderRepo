N = int(input())

if (N >= 42):
    N += 1

N_s = str(N)
num = (3 - len(N_s)) * "0"
print("AGC" + num + N_s)
