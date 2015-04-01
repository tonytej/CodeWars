import re

def to_camel_case(text):
    lst = re.split('[-_]', text)
    for e in lst[1:]:
        lst[lst.index(e)] = lst[lst.index(e)].title()
    return ''.join(lst)

print to_camel_case('the_stealth-aaa')
