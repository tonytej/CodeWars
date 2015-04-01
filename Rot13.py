import timeit


start = timeit.default_timer()


def rot13(message):
    abc = 'abcdefghijklmnopqrstuvwxyz'*2
    ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'*2
    lst = []
    for e in message:
        if e in abc:
            lst.append(abc[abc.find(e) + (13 % 26)])
        elif e in ABC:
            lst.append(ABC[ABC.find(e) + (13 % 26)])
        elif e == ' ':
            lst.append(' ')
        else:
            lst.append(e)
    return ''.join(lst)

print rot13('wgoblok'
            'what?')

stop = timeit.default_timer()

print stop - start

