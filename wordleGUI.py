from tkinter import Button
import PySimpleGUI as sg
import wordleSolverFunctions as WSF
sg.theme('dark grey 9')
# Define the windo`w's contents
layout = [[sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Text("Please enter results: ")],
          [sg.Button('-L1-'), sg.Button('-L2-'), sg.Button('-L3-'), sg.Button('-L4-'), sg.Button('-L5-')],
          [sg.Button('Guess'), sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Window Title', layout)

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





def suggestedGuess(filteredWords):
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
    return suggestedGuess



yellowLetters, grayLetters, greenLettersIndex, yellowLetterIndex, index = [], [], {}, {}, 0
filteredWords = linesFormatted
guessNum, guessedLetters = 0, ''
outPutSuggestion = ''
[Le1,Le2,Le3,Le4,Le5] = [0,0,0,0,0]

# Display and interact with the Window using an Event Loop
while True:


    event, values = window.read()
    
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    
    if event == 'Guess':
        WSF.testFunction()
        outPutSuggestion = suggestedGuess(filteredWords)
        # window['-OUTPUT-'].update('Please try: ' + outPutSuggestion )

        window['-L1-'].update(outPutSuggestion[0])
        window['-L2-'].update(outPutSuggestion[1])
        window['-L3-'].update(outPutSuggestion[2])
        window['-L4-'].update(outPutSuggestion[3])
        window['-L5-'].update(outPutSuggestion[4])
    if event == '-L1-':
        if Le1 == 0:
            Le1 = 1
            window['-L1-'].update(button_color='yellow')
        elif Le1 == 1:
            Le1 = 2
            window['-L1-'].update(button_color='green')
        elif Le1 == 2:
            Le1 = 0
            window['-L1-'].update(button_color='gray')
    if event == '-L2-':
        if Le2 == 0:
            Le2 = 1
            window['-L2-'].update(button_color='yellow')
        elif Le2 == 1:
            Le2 = 2
            window['-L2-'].update(button_color='green')
        elif Le2 == 2:
            Le2 = 0
            window['-L2-'].update(button_color='gray')
    if event == '-L3-':
        if Le3 == 0:
            Le3 = 1
            window['-L3-'].update(button_color='yellow')
        elif Le3 == 1:
            Le3 = 2
            window['-L3-'].update(button_color='green')
        elif Le3 == 2:
            Le3 = 0
            window['-L3-'].update(button_color='gray')
    if event == '-L4-':
        if Le4 == 0:
            Le4 = 1
            window['-L4-'].update(button_color='yellow')
        elif Le4 == 1:
            Le4 = 2
            window['-L4-'].update(button_color='green')
        elif Le4 == 2:
            Le4 = 0
            window['-L4-'].update(button_color='gray')
    if event == '-L5-':
        if Le5 == 0:
            Le5 = 1
            window['-L5-'].update(button_color='yellow')
        elif Le5 == 1:
            Le5 = 2
            window['-L5-'].update(button_color='green')
        elif Le5 == 2:
            Le5 = 0
            window['-L5-'].update(button_color='gray')

    if event == '-L2-':
        print('Hello World')
    if event == '-L3-':
        print('Hello World')
    if event == '-L4-':
        print('Hello World')
    if event == '-L5-':
        print('Hello World')
    
    if event == 'Ok':
        # guessResult = values.values()
        # # print ("GuessResult" + guessResult)
        # guessResult = ''.join(guessResult)
        guessResult2 = ''.join([str(Le1),str(Le2),str(Le3),str(Le4),str(Le5)])
        print(guessResult2 + " " + outPutSuggestion)
        # window['-OUTPUT-'].update('Please try: ' + guessResult )
        
        for index, letterResultNum in enumerate(guessResult2):
            if (int(letterResultNum)>0):
                yellowLetters.append(outPutSuggestion[index])
                if(int(letterResultNum)==1):
                    yellowLetterIndex[outPutSuggestion[index]+str(index)] = index
            elif (int(letterResultNum)==0):
                grayLetters.append(outPutSuggestion[index])
            if (int(letterResultNum)==2):
                greenLettersIndex[outPutSuggestion[index]+str(index)] = index

        filteredWords = list(filter(lambda x: WSF.filterWordsContain(yellowLetters, grayLetters, x), filteredWords))
        filteredWords = list(filter(lambda x: WSF.filterGreenLetters(greenLettersIndex, x), filteredWords))
        filteredWords = list(filter(lambda x: WSF.filterYellowLetterIndex(yellowLetterIndex, x), filteredWords))

        print("\nPossible words:")
        # print(filteredWords)
        outPutSuggestion = suggestedGuess(filteredWords)
        window['-OUTPUT-'].update('Please try: ' + outPutSuggestion )
        window['-L1-'].update(outPutSuggestion[0])
        window['-L2-'].update(outPutSuggestion[1])
        window['-L3-'].update(outPutSuggestion[2])
        window['-L4-'].update(outPutSuggestion[3])
        window['-L5-'].update(outPutSuggestion[4])
        if(guessResult2 == "22222"):
            guessNum=7
            print ("YOU WINNNNNN!!!!!!!!!")
            window['-OUTPUT-'].update('YOU WINNNNNN!!!!!')

        yellowLetters, grayLetters, greenLettersIndex, yellowLetterIndex, index = [], [], {}, {}, 0
        # window['-OUTPUT-'].update('Please try: ' + outPutSuggestion )



# Finish up by removing from the screen
window.close()