
from ast import Break
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

def filterWordsWrongIndex(word):
    count = 0
    for key in letterWrongIndex:
        if (key[0] == word[letterWrongIndex[key]]):
            count+=1
    if(count == 0):
        return True
    else:
        return False

#Add index filter to remove words that have letter index incorrectly

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

alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
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
guessNum = 0
while guessNum < 6:

    weightWords = []
    for word in filteredWords:
        prob = 1
        weightLettersCopy = weightLetters[:]
        for letter in word:
            prob*=weightLettersCopy[(ord(letter)-97)]
            #Penalize repeated leters
            weightLettersCopy[(ord(letter)-97)] = weightLettersCopy[(ord(letter)-97)] * 0.6
        weightWords.append(prob)

    guess1=filteredWords[weightWords.index(max(weightWords))]
    print (guess1)

    #print(type(linesFormatted))


    guess1Result = input('Please enter results: ')

    if(guess1Result == "22222"):
        guessNum=7
        print ("YOU WINNNNNN!!!!!!!!!")
        Break

    lettersInWord = []
    lettersNotInWord = []
    letterIndex = {}
    letterWrongIndex = {}

    index = 0

    for j in guess1Result:
        if (int(j)>0):
            lettersInWord.append(guess1[index])
            if(int(j)==1):
                letterWrongIndex[guess1[index]+str(index)] = index
        elif (int(j)==0):
            lettersNotInWord.append(guess1[index])
        if (int(j)==2):
            letterIndex[guess1[index]+str(index)] = index

        index+=1

    # print(letterIndex)
    # print (lettersInWord)
    # print (lettersNotInWord)




    filteredWords = list(filter(filterWordsContain, filteredWords))
    filteredWords = list(filter(filterWordsIndex, filteredWords))
    filteredWords = list(filter(filterWordsWrongIndex, filteredWords))
    print(filteredWords)


