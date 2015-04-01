def sum_pairs(ints, s):
    lst =[]
    for e in ints:
        for f in ints:
            if e + f == s and ints.index(e) - ints.index(f) <= 0 and [e, f] not in lst:
                lst.append([e, f])
    return lst

print sum_pairs([10, 5, 2, 3, 7, 5],         10)
