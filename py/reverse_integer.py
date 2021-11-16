def reverse(x: int) -> int:
    x = str(x)[::-1]
    if x[-1] == '-':
        x = -int(x[:-1])
    else:
        x = int(x)
    return x if x>-2**31 and x<2**31 else 0

print(reverse(786))
