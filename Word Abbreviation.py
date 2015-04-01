def abbreviate(s):
    lst = []
    for e in s.split():
        if len(e) >= 4:
            if any('-' in x and len(x) > 1 for x in e.split()):
                new_list = e.replace('-', ' ').split(' ')
                lst.append("{0}{1}{2}-{3}{4}{5}".format(new_list[0][0], len(new_list[0]) - 2, e[len(new_list[0]) - 1],
                                                        new_list[1][0], len(new_list[1]) - 2, e[len(new_list[1]) - 1]))
            else:
                lst.append("{0}{1}{2}".format(e[0], len(e) - 2, e[len(e) - 1]))
    return ' '.join(lst)



print abbreviate('elephant-ride and internationalization')