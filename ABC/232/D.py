H, W = map(int, input().split())
C = [list(input()) for l in range(H)]

x = 0
y = 0
C[y][x] = '#'
num = 1

while(True):
    if (x < W and y < H):
        if x + 1 < W and C[y][x + 1] == '.':
            C[y][x + 1] = '#'
            x += 1
            num += 1
            continue
        elif y + 1 < H and C[y + 1][x] == '.':
            C[y + 1][x] = '#'
            y += 1
            num += 1
            continue
        else:
            break
    else:
        break
print(num)
