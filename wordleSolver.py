
from copy import copy
import string

def filterWordsIndex(word):
    count = 0
    for key in letterIndex:
        if (key[0] == word[letterIndex[key]]):
            count+=1
    if(count == len(letterIndex)):
        return True
    else:
        return False

def filterWordsContain (word):
    #print (all([letters in word for letters in lettersInWord]))
    countIn = 0
    countNot = 0
    copyLettersInWord = lettersInWord[:]
    copyLettersNotInWord = lettersNotInWord[:]

    wordCopy= word[:]
    for character in wordCopy:
        for letter in copyLettersInWord:
            if (letter==character):
                #print(lettersInWord)
                copyLettersInWord.remove(letter)
                word = word.replace(letter,'',1)
                # print(word)
                countIn+=1
                break

    for character in word:
        for letter in copyLettersNotInWord:
            if (letter==character):
                # print (word)
                # print(lettersNotInWord)
                copyLettersNotInWord.remove(letter)
                word = word.replace(letter,'',1)
                countNot+=1
                break

    
    # print (countNot)
    if countIn == len(lettersInWord) and countNot == 0:
         return True 
    else:
        return False



with open('words.txt') as f:
    lines = f.readlines()

for word in lines:
    word[0:-1]

def removeBreak(word):
    return word[0:-1]




linesFormatted = list(map(removeBreak, lines))

# linesFormatted = ['apses', 'arses', 'ashes', 'asses', 'asset', 'bases', 'beses', 'bests', 'bises', 'bless', 'buses', 'cases', 'chess', 'coses', 'cress', 'desks', 'doses', 'dress', 'eases', 'easts', 'erses', 'esnes', 'essay', 'esses', 'eyass', 'fesse', 'fests', 'fosse', 'fuses', 'gases', 'gesso', 'gests', 'guess', 'hests', 'hoses', 'isles', 'issei', 'issue', 'jesse', 'jests', 'lases', 'leses', 'loess', 'loses', 'lyses', 'masse', 'mesas', 'messy', 'mises', 'muses', 'nests', 'noses', 'oases', 'pases', 'passe', 'pesos', 'pests', 'poses', 'posse', 'press', 'puses', 'rases', 'rests', 'rises', 'roses', 'ruses', 'sabes', 'sades', 'safes', 'sages', 'sakes', 'sales', 'sanes', 'sates', 'saves', 'saxes', 'seals', 'seams', 'sears', 'seats', 'sects', 'seeds', 'seeks', 'seels', 'seems', 'seeps', 'seers', 'segos', 'seifs', 'seise', 'seism', 'selfs', 'sells', 'semes', 'semis', 
# 'sends', 'sensa', 'sense', 'septs', 'seres', 'serfs', 'setts', 'sexes', 'sexts', 'sheas', 'sheds', 'shews', 'shies', 'shoes', 'sices', 'sides', 'sikes', 'sines', 'sipes', 'sires', 'sises', 'sites', 'sixes', 'sizes', 'skees', 'skegs', 'skeps', 'skews', 'skies', 'sleds', 'slews', 'sloes', 'slues', 'smews', 'sneds', 'snyes', 'sokes', 'soles', 'sones', 'sores', 'souse', 'spaes', 'specs', 'spews', 'spies', 'spues', 'stems', 'steps', 'stets', 'stews', 'sties', 'styes', 'suers', 'suets', 'supes', 'syces', 'sykes', 'tasse', 'tests', 'tress', 'users', 'vases', 'vests', 'vises', 'wests', 'wises', 'yeses', 'zests']
#print (linesFormatted)
alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# print (letters)
i=0
count = [0] * 26

print (count)
for c in alph:
    for word in linesFormatted:
        if (c in word):
            count[i]+=1
    i+=1

print (count)
wordCount = len(linesFormatted)

weightLetters =[]

for n in count:
    weightLetters.append(n/wordCount)

print (max(weightLetters))
filteredWords = linesFormatted

# print (ord('a')-97)
for i in range(0,6):

    weightWords = []
    for word in filteredWords:
        prob = 1
        for letter in word:
            prob*=weightLetters[(ord(letter)-97)]
        weightWords.append(prob)

    guess1=filteredWords[weightWords.index(max(weightWords))]
    print (guess1)

    print(type(linesFormatted))

    word = "Hello"
    word.replace('H', '')
    print(word)

    guess1Result = input('Please enter results: ')

    lettersInWord = []
    lettersNotInWord = []
    letterIndex = {}

    index = 0

    for i in guess1Result:
        #print (i)
        if (int(i)>0):
            lettersInWord.append(guess1[index])
        elif (int(i)==0):
            lettersNotInWord.append(guess1[index])
        if (int(i)==2):
            letterIndex[guess1[index]+str(index)] = index

        index+=1

    print(letterIndex)
    print (lettersInWord)
    print (lettersNotInWord)




    filteredWords = list(filter(filterWordsContain, filteredWords))
    filteredWords = list(filter(filterWordsIndex, filteredWords))

    print(filteredWords)
