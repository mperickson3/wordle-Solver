def filterGreenLetters(word):
    count = 0
    for key in greenLettersIndex:
        if (key[0] == word[greenLettersIndex[key]]):
            count+=1
    return True if count == len(greenLettersIndex) else False

def testFunction():
    print ("test")

def filterYellowLetterIndex(word):
    count = 0
    for key in yellowLetterIndex:
        if (key[0] == word[yellowLetterIndex[key]]):
            count+=1
    return True if count == 0 else False

def filterWordsContain (word):
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


with open('words.txt') as f:
    lines = f.readlines()

for word in lines:
    word[0:-1]

def removeBreak(word):
    return word[0:-1]

linesFormatted = list(map(removeBreak, lines))

alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
i, count, weightLetters, wordCount = 0, [0]*26, [], len(linesFormatted)

for c in alph:
    for word in linesFormatted:
        if (c in word):
            count[i]+=1
    i+=1

for n in count:
    weightLetters.append(n/wordCount)

filteredWords = linesFormatted
guessNum, guessedLetters = 0, ''
while guessNum < 6:
    weightWords = []
    for word in filteredWords:
        prob = 1
        weightLettersCopy = weightLetters[:]
        for letter in word:
            prob*=weightLettersCopy[(ord(letter)-97)]
            #Penalize repeated leters
            weightLettersCopy[(ord(letter)-97)] *= 0.6

        weightWords.append(prob)

    suggestedGuess=filteredWords[weightWords.index(max(weightWords))]
    print ("\nPLEASE TRY: " + suggestedGuess)
    guessedLetters += suggestedGuess


    print ("\n  Format: \n  Grey == 0 \n  Yellow == 1 \n  Green == 2 \n")
    guessResult = input('Please enter results: ')

    yellowLetters, grayLetters, greenLettersIndex, yellowLetterIndex, index = [], [], {}, {}, 0

    for letterResultNum in guessResult:
        if (int(letterResultNum)>0):
            yellowLetters.append(suggestedGuess[index])
            if(int(letterResultNum)==1):
                yellowLetterIndex[suggestedGuess[index]+str(index)] = index
        elif (int(letterResultNum)==0):
            grayLetters.append(suggestedGuess[index])
        if (int(letterResultNum)==2):
            greenLettersIndex[suggestedGuess[index]+str(index)] = index
        index+=1

    filteredWords = list(filter(filterWordsContain, filteredWords))
    filteredWords = list(filter(filterGreenLetters, filteredWords))
    filteredWords = list(filter(filterYellowLetterIndex, filteredWords))
    print("\nPossible words:")
    print(filteredWords)

    if(guessResult == "22222"):
        guessNum=7
        print ("YOU WINNNNNN!!!!!!!!!")

