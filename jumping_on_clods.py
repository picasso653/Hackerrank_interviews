def jumpingOnClouds(c):
    moves = 0
    i = 0
    while i < len(c) - 1:
        if i + 2 < len(c) and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        moves += 1
    return moves


print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))