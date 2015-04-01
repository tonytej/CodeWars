def digital_root(n):
    lst = [int(digit) for digit in str(n)]
    while sum(lst) > 9:
        lst = [int(digit) for digit in str(sum(lst))]
    return sum(lst)

print digital_root('')