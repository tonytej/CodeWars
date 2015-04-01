def is_prime(num):
    for i in xrange(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
    
def divisors(integer):
    lst = []
    for e in range(2, integer):
        if integer % e == 0:
            lst.append(e)
    return str(integer) + ' is prime' if is_prime(integer) else lst

print divisors(15)
print divisors(12)
print divisors(13)

'''
Test.assert_equals(divisors(15), [3, 5]);
Test.assert_equals(divisors(12), [2, 3, 4, 6]);
Test.assert_equals(divisors(13), "13 is prime");
'''