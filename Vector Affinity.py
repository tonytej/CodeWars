

def vector_affinity(a, b):
    lst = (a, b)
    count = 0
    if len(max(lst)) != 0:
        for e in max(lst):
            if e in min(lst):
                count += 1
        return float(count) / len(max(lst))
    return 0.0

print vector_affinity([1,2,3,4,5,6] ,[1,2,3])