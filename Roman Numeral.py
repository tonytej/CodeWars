'''
M = 1000
D = 500
C = 100
L = 50
X = 10
V = 5
'''

def solution(roman):
    roman_num = {'M': 1000, 'D': 500, 'C': 100,
                 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    sums = [0]
    count = 0
    for letter in roman:
        if roman_num[letter] > sums[count]:
            sums[count] = roman_num[letter] - sums[count]
        else:
            sums.append(roman_num[letter])
            count += 1
    return sum(sums)

print solution('MCD') #1400

print solution('MCMXC')

print solution('CD') #400
