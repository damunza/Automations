import re

def arrange(sentence):
    '''
    arrange sorts a sentence eg Th1is i2s th3e s4mple in correct order depending on the numbers in each word
    '''

#  checking if the s entence is empty
    try:
        if len(sentence) == 0:
            return sentence
    finally:
        sentencelist = sentence.split(' ')
#  dictionary  to store correct order
        wordlist = {}
#  looping a list made of all the indexes of split sentence
        for word in list(range(len(sentencelist))):
#  find the integer in each word in split sentence
            ind = int(''.join(re.findall(r'\d', sentencelist[word])))

#  appending to the dictionary
            wordlist[ind-1] = sentencelist[word]
#  return the sentence
        return ' '.join( [value for key, value in sorted(wordlist.items())] )
