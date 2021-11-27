S1 = input()
S2 = input()

map_s = [[S1[0], S1[1]], [S2[0], S2[1]]]

b = [False] * 4

if (S1[0] == "#" and S1[1] == "#"):
    b[0] = True
if (S1[0] == "#" and S2[0] == "#"):
    b[1] = True
if (S2[0] == "#" and S2[1] == "#"):
    b[2] = True
if (S1[1] == "#" and S2[1] == "#"):
    b[3] = True

if (S1[0] == "#" and S2[1] == "#") and (S1[0] == "." and S2[1] == "."):
    print("No")
elif (S1[1] == "#" and S2[0] == "#") and (S1[1] == "." and S2[0] == "."):
    print("No")
else:
    num = 0
    for i in b:
        if (i):
            num += 1
            if (num == 1):
                print("Yes")
    if (num == 0):
        print("No")
