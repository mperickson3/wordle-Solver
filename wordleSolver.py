
import string


with open('words.txt') as f:
    lines = f.readlines()

for word in lines:
    word[0:-1]

def removeBreak(word):
    return word[0:-1]

def filterWords (word):
    if (lettersInWord in word):
        return True
    else:
        return False


linesFormatted = list(map(removeBreak, lines))

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

print (ord('a')-97)

weightWords = []
for word in linesFormatted:
    prob = 1
    for letter in word:
        prob*=weightLetters[(ord(letter)-97)]
    weightWords.append(prob)

guess1=linesFormatted[weightWords.index(max(weightWords))]
print (guess1)

guess1Result = input('Please enter results: ')

lettersInWord = []

for i in guess1Result:
    print (i)
    if (int(i)>0):
        lettersInWord.append(guess1[int(i)])

print (lettersInWord)

filteredWords = filter(filterWords, linesFormatted)

print (list(filteredWords))

# for word in filteredWords:
#     print (word)