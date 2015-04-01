# write the function is_anagram
def is_anagram(test, original):
    if len(test) == len(original):
        for e in test.lower():
         return any(e == f for f in original.lower())
    return False

print is_anagram('dumble', 'bumble')
print is_anagram('sudsa', 'dudududu')
print is_anagram('Creative', 'Reactive')
print is_anagram('ound', 'round')