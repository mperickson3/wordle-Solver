def filterGreenLetters(greenLettersIndex, word):
    count = 0
    for key in greenLettersIndex:
        if (key[0] == word[greenLettersIndex[key]]):
            count+=1
    return True if count == len(greenLettersIndex) else False

def testFunction():
    print ("test")

def filterYellowLetterIndex(yellowLetterIndex, word):
    count = 0
    for key in yellowLetterIndex:
        if (key[0] == word[yellowLetterIndex[key]]):
            count+=1
    return True if count == 0 else False

def filterWordsContain (yellowLetters, grayLetters, word):
    yellowLetterCount, grayLetterCount = 0, 0
    copyYellowLetters = yellowLetters[:]
    copyGrayLetters = grayLetters[:]
    copyWord= word[:]
    for character in copyWord:
        for letter in copyYellowLetters:
            if (letter==character):
                copyYellowLetters.remove(letter)
                word = word.replace(letter,'',1)
                yellowLetterCount+=1
    for character in word:
        for letter in copyGrayLetters:
            if (letter==character):
                copyGrayLetters.remove(letter)
                word = word.replace(letter,'',1)
                grayLetterCount+=1
    return True if(yellowLetterCount==len(yellowLetters) and grayLetterCount==0) else False