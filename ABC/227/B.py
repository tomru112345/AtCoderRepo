N = int(input())
S = list(map(int, input().split()))

max_num = max(S)
a = 1
b = 1

shiki = 4 * (a * b) + 3 * (a + b)

while(len(S) > 0 and shiki <= max_num):
    shiki = 4 * (a * b) + 3 * (a + b)
    t = len(S)
    for i in range(t):
        if (shiki == S[i]):
            tmp = S[i]
            S = [tmp for tmp in S if tmp != shiki]
            t = len(S)
            break
    b += 1
    shiki = 4 * (a * b) + 3 * (a + b)
    if (shiki > max_num):
        b = 1
        a += 1
    shiki = 4 * (a * b) + 3 * (a + b)

print(len(S))
