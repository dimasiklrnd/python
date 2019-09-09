if g[0][0] == g[0][1] == g[0][2]:
        return g[0][0]
    elif g[0][0] == g[1][1] == g[2][2]:
        return g[0][0]
    elif g[0][0] == g[1][0] == g[2][0]:
        return g[0][0]
    elif g[0][1] == g[1][1] == g[2][1]:
        return g[0][1]
    elif g[0][2] == g[1][2] == g[2][2]:
        return g[0][2]
    elif g[0][2] == g[1][1] == g[2][0]:
        return g[0][2]
    elif g[1][0] == g[1][1] == g[1][2]:
        return g[1][0]
    elif g[2][0] == g[2][1] == g[2][2]:
        return g[2][0]
    else:
        return "D"