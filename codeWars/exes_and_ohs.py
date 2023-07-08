def xo(s):
    s = str(s)
    return True if s.count("x") + s.count("X") == s.count("O") + s.count("o") else False
