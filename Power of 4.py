def powerof4(n):
    if type(n) is int:
        return any(4**e == n for e in range(1, n))
    return False

print powerof4(64)