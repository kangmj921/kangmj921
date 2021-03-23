coverType = [[[0, 0], [1, 0], [0, 1]],
             [[0, 0], [0, 1], [1, 1]],
             [[0, 0], [1, 0], [1, 1]],
             [[0, 0], [1, 0], [1, -1]]]


def setting(pan, x, y, ty, delta):
    ok = True
    for i in range(0, 3):
        ny = y + coverType[ty][i][0]
        nx = x + coverType[ty][i][1]
        if ny < 0 or ny >= len(pan) or nx < 0 or nx >= len(pan[0]):
            ok = False
        else:
            pan[ny][nx] += delta
            if (pan[ny][nx]) > 1:
                ok = False
    return ok


def bdcover(pan):
    y = -1
    x = -1
    for i in range(0, len(pan)):
        for j in range(0, len(pan[i])):
            if pan[i][j] == 0:
                y = i
                x = j
                break
        if y != -1:
            break
    if y == -1:
        return 1
    ret = 0
    for t in range(0, 4):
        if setting(pan, x, y, t, 1):
            ret += bdcover(pan)
        setting(pan, x, y, t, -1)
    return ret


for n in range(int(input())):
    H, W = map(int, input().split())
    game_pan = [list(map(lambda x: 0 if x == '.' else 1, input()[:W])) for i in range(H)]
    print(bdcover(game_pan))
