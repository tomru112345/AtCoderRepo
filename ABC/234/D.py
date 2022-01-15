N, K = map(int, input().split())
P = list(map(int, input().split()))

P_sec_max_list = []
tmp = sorted(set(P[0: K]))[-K]
P_sec_max_list.append(tmp)
# print(sorted(set(P[0: i]))[-K])
print(tmp)
for i in range(K + 1, N + 1):
    tmp = P_sec_max_list[i - K - 1]
    if (tmp < P[i - 1]):
        tmp = sorted(set(P[0: i]))[-K]
        P_sec_max_list.append(tmp)
        print(tmp)
    else:
        P_sec_max_list.append(tmp)
        print(tmp)

# print(P_sec_max_list)
