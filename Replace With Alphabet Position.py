def alphabet_position(input):
    alphabets = {chr(97+i) : i+1 for i in range(26)}
    lst = [str(alphabets[e]) for e in input.lower() if e in alphabets]
    return ' '.join(lst)




print alphabet_position('Hello my name is botzzzz1234''12')