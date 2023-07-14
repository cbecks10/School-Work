#csc 241 Assignment 7 Solutions

#1
def unique(dList):
    mySet = set()
    for item in dList:
        for num in item:
           mySet.add(num)

    return len(mySet)

#2
def ticker(fileName):

    try:
        theFile = open(fileName)
        contents = theFile.readlines()
    except:
        print('File not found')
        return

    symbols = {}
    isKey = True
    key = ''

    #method One
##    for i in contents:
##        if isKey == True:
##            key = i.replace('\n', '')
##            symbols[key] = ''
##            
##            isKey = False
##        else:
##            symbols[key] = i.replace('\n','')
##            isKey = True

    #method Two
    for i in range(0,len(contents)-1):
        if i % 2 == 0:
            symbols[contents[i].replace('\n','')] = contents[i+1]

    print(symbols)
    
    cName = 'p'
    

    while True:
        cName = input('Enter company name: ')
        if len(cName) == 0:
            break
        cName = cName.upper()
        for name in symbols:
            if name.find(cName) > -1:
                cName = name
        try:
            print(symbols[cName])
        except:
            print('The company {} is not found'.format(cName))

    print('Thanks for using this')
    
#3
def vote(aList):
    ballot = {}
    for item in aList:
        ballot[item.lower()] = 0

    ballot['Unknown'] = 0

    theVote = ''

    while True:
        theVote = input('Enter a vote: ')
        if len(theVote) == 0:
            break

        if theVote.lower() not in ballot:
            ballot['Unknown'] +=1
            continue
        for person in ballot:
            if theVote.lower() == person.lower():
                ballot[person] += 1
                

    for person in ballot:
        if ballot[person] == 1:
            print('There was {} vote for {}'.format(ballot[person], person.title()))
        else:
            print('There were {} votes for {}'.format(ballot[person], person.title()))
        

#4
import random
def game(aNum):
    counter = 0
    numCorrect = 0
    trigger = True
    while counter < aNum:
        if trigger == True:
            num1 = random.randint(0,9)
            num2 = random.randint(0,9)

        print('{} + {}'.format(num1, num2))
        try:
            answer = eval(input('Enter answer: '))
            if answer == num1+num2:
                print('Correct')
                numCorrect +=1
            else:
                print('Incorrect')

            counter += 1
            trigger= True
            
        except:
            trigger = False
            print('Enter a valid number')

    print('You got {} out of {} correct'.format(numCorrect, aNum))
              

    
