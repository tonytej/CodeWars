

def maxSequence(arr):
    summ = []
    for num in arr:
        n = len(arr)
        while n != arr.index(num):
            summ.append(sum(arr[arr.index(num):n]))
            n -= 1
    return max(summ) if len(arr) > 0 else 0

a = [-1,-2,4,-1,2,5,-11,-2,5,7]
print maxSequence(a)
print sum(a)
print maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print maxSequence([])
# should be 6: [4, -1, 2, 1]