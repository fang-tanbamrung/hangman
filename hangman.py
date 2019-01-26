import json
from termcolor import colored
import colorama

colorama.init()
# category
def printCate(cate):
    for i, v in enumerate(cate):
        print colored(i+1,'yellow'),colored(':','yellow'),colored(v,'yellow')

# get value from list
def getList(lista):
    listb = []
    for i in lista:
        listb.append(i)
    return listb
# calculate score
def getScore(score, remainWrongGuess, arrayOfIndex):
    if remainWrongGuess < 0:
        remainWrongGuess = 0
    if arrayOfIndex == -1:
        return score
    score = score + ((1 + remainWrongGuess)*len(arrayOfIndex))
    return score


# load data from json file
def callSource(fileName):
    return json.load(open(fileName+'.json'))

# convert word to array of '_' for word length
def firstArray(word):
    b = []
    for i in range(len(word)):
        if ord(word[i]) >= 97 and ord(word[i]) <= 122:
            b.append('_')
        else:
            b.append(word[i])
    return b

# find if there's character in word and return index of charater in word,
# return empty array if could found in word or return -1 if input more than
# 1 character or not a alphabet 
def findIndex(guess, word):
    if len(guess) == 1:
        if ord(guess) >= 97 and ord(guess) <= 122:
            array = []
            for counter, value in enumerate(word):
                if value == guess:
                    array.append(counter)
            return array
    print colored('input must be a-z or more than 1 character','red')
    return -1

# replace '_' with input character 
def replaceChar(arrayOfIndex, char, arrayOfWord):
    if arrayOfIndex == -1:
        return arrayOfWord
    for t in arrayOfIndex:
        arrayOfWord.pop(t)
        arrayOfWord.insert(t,char)
    return arrayOfWord

# print the array, score, remain wrong guess and wrong character in the same line
def printResult(arrayOfWord, hint, score, remainWrongGuess, wrongChar):
    if arrayOfWord == -1:
        return
    print hint
    for i in range(len(arrayOfWord)):
        print colored(arrayOfWord[i],'green'),
    print 'score',colored(score,'cyan'),
    print 'remain wrong guess :',colored(remainWrongGuess,'yellow'),
    print 'wrong character :',colored(wrongChar,'yellow')

# convert word to array for template to check if all in word was correct
def convert2Array(word):
    array = []
    for i in word:
        array.append(i)
    return array

# clear variable
def clearVar(index, score, word, remainWrongGuess):
    index = 0
    score = 0
    remainWrongGuess = 5
    word = ''
    return index, score, word, remainWrongGuess

# main program
if __name__ == "__main__":
    initCate = json.load(open('category.json'))['cate']
    cate = getList(initCate)
    while True:
        print colored('you can exit by type "exit"','cyan')
        printCate(cate)
        
        while True:
            typ = raw_input('enter number of category : ')
            if typ == 'exit':
                exit()
            try:
                typ = int(typ)
                if typ-1 not in range(len(cate)):
                    print colored('enter number of category from above','red')
                else:
                    break
            except ValueError:
                print colored('enter number of category from above','red')
            
        
        print colored('category :','green'),colored(cate[typ-1],'green')
        data = cate[typ-1]
        dataSource = callSource(data)
        cate.pop(typ-1)
        index = 0
        score = 0
        mainProg = False
        while True:
            if mainProg == True:
                break
            mainProg = False
            word = dataSource[index]['word'].lower()
            hint = dataSource[index]['hint'].lower()
            c = firstArray(word)
            remainWrongGuess = 5
            wrongCharacter = []
            printResult(c, hint, score, remainWrongGuess, wrongCharacter)

            currentWord = convert2Array(word)
            while True:
                if remainWrongGuess == 0:
                    print colored('remain wrong guess is empty','red')
                    break
                if c == currentWord:
                    index += 1
                    wrongCharacter = []
                    remainWrongGuess = 5
                    if index >= len(dataSource):
                        print colored('your score is :','green'),colored(score,'green')
                        print colored('well done, out of word','red')
                        mainProg = True
                        break
                    break
                guessChar = raw_input('guess char : ')
                if guessChar == 'exit':
                    print colored('your score is :','green'),colored(score,'green')
                    print 'you will exit'
                    exit() 
                arrayOfIndex = findIndex(guessChar.lower(), word)
                if arrayOfIndex == []:
                    if not guessChar in wrongCharacter:
                        wrongCharacter.append(guessChar)
                        remainWrongGuess -=1
                c = replaceChar(arrayOfIndex, guessChar, c)
                score = getScore(score, remainWrongGuess, arrayOfIndex)
                printResult(c, hint, score, remainWrongGuess, wrongCharacter)
            if remainWrongGuess == 0:
                while True:
                    restart = raw_input(colored('want to re-start(y/n) : ','yellow')).lower()
                    if restart == 'y' or restart == 'yes':
                        index = 0
                        score = 0
                        remainWrongGuess = 10
                        word = ''
                        cate = getList(initCate)
                        print initCate
                        break
                    elif restart == 'n' or restart == 'no':
                        exit()
                break
    

