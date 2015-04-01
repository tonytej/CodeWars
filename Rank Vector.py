def ranks(a):
    lst = sorted(a, reverse=True)
    rank = []
    for e in a:
        rank.append(lst.index(e) + 1)
    return rank

print ranks([])
print ranks([2])
print ranks([3,3,3,3,3,5,1])
'''Test.assert_equals(ranks([]), [])
Test.assert_equals(ranks([2]), [1])
Test.assert_equals(ranks([2,2]), [1,1])'''