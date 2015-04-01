import re
import string



def title_case(title, minor_words=None):
    if title == '':
        return ''
    else:
        wordList = re.sub("[^\w]", " ",  title.lower()).split()
        wordList[0] = wordList[0].upper()
        print wordList
        if minor_words != None:
            exceptionList = re.sub("[^\w]", " ",  minor_words.lower()).split()
            for e in wordList:
                if e not in exceptionList:
                    wordList[wordList.index(e)] = string.capwords(e)
            return ' '.join(wordList)
        else:
            for e in wordList:
                    wordList[wordList.index(e)] = string.capwords(e)
            return ' '.join(wordList)


print title_case('a clash of KINGS', 'a an the of')
print title_case('')
print title_case('THE WIND IN THE WILLOWS', 'The in')
print title_case('the quick brown fox')


'''
Test.assert_equals(title_case(''), '')
Test.assert_equals(title_case('a clash of KINGS', 'a an the of'), 'A Clash of Kings')
Test.assert_equals(title_case('THE WIND IN THE WILLOWS', 'The In'), 'The Wind in the Willows')
Test.assert_equals(title_case('the quick brown fox'), 'The Quick Brown Fox')

'''