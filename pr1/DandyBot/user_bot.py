def script(check, x, y):
    if check("gold", x, y):
            return "take"
    if ~check("wall", x+1, y):
            return "right"
    elif ~check("wall", x, y+1):
        return "down"
    return "pass"
