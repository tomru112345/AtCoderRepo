N = int(input())
p = list(map(int, input().split()))

l = [-1] * N

max_score = max(p)
min_score = min(p)
max_idx = -1
min_idx = -1


def check(N):
    for i in range(N):
        if (i != 0):
            if (p[i] < p[i - 1]):
                return "NO", i
    return "YES", -1


def in_l(i):
    global max_score
    tmp = max_score
    tmp_index = -1
    for t in range(i, N):
        l[t] = p[t]
        if (p[t] != -1 and tmp > p[t]):
            tmp = p[t]
            tmp_index = t
    return tmp_index


def set(N):
    global max_score, min_score, min_idx, max_idx
    for i in range(N):
        if (p[i] == max_score):
            max_idx = i
        if (p[i] == min_score):
            min_idx = i


set(N)
t_bool, index = check(N)
if (t_bool == "YES"):
    print("YES")
else:
    if (max_idx < min_idx):
        tmp = max_score
        p[max_idx] = min_score
        p[min_idx] = tmp
    else:
        tmp_index = in_l(index)
        tmp = p[index - 1]
        p[index - 1] = p[tmp_index]
        p[tmp_index] = tmp
    t_bool, index = check(N)
    print(t_bool)
