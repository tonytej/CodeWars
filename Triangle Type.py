__author__ = 'Tony'

def is_triangle(a, b, c):
    return True if a + b > c and b + c > a and a + c > b else False

def triangle_type(a, b , c):
    lst = [a, b, c]
    rank = sorted(lst)
    if is_triangle(a, b, c):
        if (rank[2])**2 == (rank[0])**2 + (rank[1])**2:
            return 2
        if (rank[2])**2 > (rank[0])**2 + (rank[1])**2:
            return 3
        else:
            return 1
    else:
        return 0

print triangletype(2, 4, 6)
print triangletype(8,5,7)
print triangletype(3,4,5)
print triangletype(7,12,8)
'''triangle_type(2, 4, 6) # return 0 (Not triangle)
triangle_type(8, 5, 7) # return 1 (Acute, angles are approx.
triangle_type(3, 4, 5) # return 2 (Right, angles are approx.
triangle_type(7, 12, 8) return 3'''