import string, pyperclip

def firstvowel(word):
    '''
    firstvowel returns the index of the firstvowel in a given words

    input : word
    output : index

    return : int
    '''
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    for index, letter in enumerate(list(word)):
        if letter in vowels:
            return index
    return -1

def switch(a, b):
    '''
    switch is a function that just returns two strings that have switched places

    input1 : half one of the word
    input2 : half 2 of the words

    output : the switched word

    return : string
    '''
    a, b = b, a

    return a + b

def punct(letter):
    '''
    punc tests if the provided string is a punctuation mark and returns 1 if true and 0 if false

    input : a string
    output : 1 for true 0 for false

    return : integer
    '''
    if letter in string.punctuation:
        return 1
    return 0

def pig(userinput):
    '''
    pig converts input passed by the user in commandline as piglatin

    input : a parsed string on the user commandline
    output : a piglatin string

    return : string
    '''
    piglatin = []
    for word in userinput.split(' '):
        # create a working word to carry actions on
        workingword = word.lower()
        punctuation = ''
        lastletter = punct( workingword[-1] )
        if lastletter == 1:
            punctuation += workingword[-1]
            workingword = workingword[:-1]
        # getting the position of the first vowel in the word
        vowelindex = firstvowel(workingword)

        # holding the piglatin words
        newword = ''

        if vowelindex == 0:
            # create the piglatin
            newword = workingword + 'yay'
        elif vowelindex > 0:
            firstsec = workingword[:vowelindex]
            secondsec = workingword[vowelindex:]

            # take all letters befor the first vowel and move them to the rear
            changeind = switch(firstsec, secondsec)

            # create the piglatin
            newword = changeind + 'ay'
        if len(punctuation) > 0:
            newword = newword + punctuation
        if word.isupper():
            newword = newword.upper()
            piglatin.append(newword)
        elif word.istitle():
            newword = newword.title()
            piglatin.append(newword)
        else:
            piglatin.append(newword)

    return ' '.join(piglatin)

data = input('Enter a string to be converted to piglatin: ')
pigl = pig(data)
print (pigl)
