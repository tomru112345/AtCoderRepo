S = input()
T = input()

s_L = []
a_l = []

for i in range(97, 123):
    a_l.append(chr(i))

for i in range(len(S)):
    a = a_l.index(S[i])
    b = a_l.index(T[i])
    t = a - b
    s_L.append(t)
print(s_L)
s_L = list(set(s_L))

if(len(s_L) == 1):
    print("Yes")
else:
    for i in range(len(s_L)):
        if (s_L[i] > 0):
            s_L[i] -= 26
    s_L = list(set(s_L))
    if(len(s_L) == 1):
        print("Yes")
    else:
        print("No")
