#Christopher Becker
#Assignment 6

#1
import random

def getRollValue():
    '''This series of function creates a platform a user to play craps '''
    diceOneValue = random.randint(1,6)
    diceTwoValue = random.randint(1,6)
    rollValue = diceOneValue + diceTwoValue
    print('Dice 1 rolled {}, Dice 2 rolled {}.  Total roll is {}'.format(diceOneValue, diceTwoValue, rollValue))
    return [diceOneValue, diceTwoValue]


def placeBets(table, bet, wager):

    betFound = False
    for item in table:
        theBet = item[0]
        if theBet.lower() == bet.lower():
            betFound = True
            theOdds = item[1]
            currentBets = item[2]
            currentBets.append(wager)
    
    if betFound == False:
        print('Sorry bet not found')
        
    return table
        

def main():

    players={'Tim':True,'Brian':False,'Chris':False,'Sam':False,'Bob':False}

    table = [['3', 16/1,[]],
            ['4', 2/1,[]],
            ['5', 2/1,[]],
            ['6', 2/1,[]],
            ['7', 5/4, []],
            ['8', 2/1,[]],
            ['9', 2/1,[]],
            ['10', 2/1,[]],
            ['11', 16/1,[]],
            ['snake eyes', 31/1,[]],
            ['hard 4', 8/1,[]],
            ['hard 6', 10/1,[]],
            ['hard 8', 10/1,[]],
            ['hard 10', 8/1,[]],
            ['boxcar', 31/1,[]]]
    
    while True:
        print("Please select an option: ")
        print("Enter 'p' to place a bet")
        print("Enter 's' to show availavle bets")
        print("'Enter 'b' to show currently placed bets")
        print("Enter 'r' to roll")
        print("Enter 'quit' to quit")

        for i in players:
            if players[i]==True:
                print("{} currently has the dice".format(i))
        inp=input("Please enter an option: ").upper()
        if inp=='Q' or inp=='QUIT':
            break
        if inp=='P':
            bet = input('Please enter the bet: ')
            if len(bet) > 0:
                wager = input('Please enter wager: ')
                try:
                    wager = eval(wager)
                    table = placeBets(table,bet,wager)
                except:
                    print('Wager not valid')
        if inp=='S':
            print('The current available bets are:')
            for bets in table:
                print('{} with odds {}'.format(bets[0], bets[1]))
        if inp=='B':
            for bets in table:
                print('{} has bets {}'.format(bets[0], bets[2]))
        if inp=='R':
            z=getRollValue()
            print("Dice 1 rolled {}, Dice 2 rolled {}. Total roll is {}".format(z[0], z[1], sum(z)))
            
            if sum(z)==7 or sum(z)==11:
                players={'Tim':False,'Brian':True,'Chris':False,'Sam':False,'Bob':False}

                
            


#2
def inversions(aString):
    '''This function returns the number of inversions in a given sequence '''
    counter=0
    
    for i in range(len(aString)):
        for j in range(i,(len(aString))):
            if aString[i]>aString[j]:
                counter+=1
    return counter

#3
def printTwoLargest():
    '''This function takes a series of numbers from a user and prints the
       two largest of those numbers.''' 
    var=set()

    while True:

        try:
            inp=eval(input("Please enter a number: "))
            if inp<=0:
                break
            var.add(inp)
            

        except:
            print("That was not a valid number. Please try again.")
    if len(var)<2:
        print("Fewer than two positive numbers were entered.")
    else:
        print("The largest is {}".format(max(var)))
        var.remove(max(var))
        print("The second largest is {}".format((max(var))))
        
        
              
        
            

#4

def letter2Number(aString):
    '''This function takes a letter from the user and returns the corresponding
       grade point associated with that letter'''
    d1={'A':4,'B':3,'C':2,'D':1,'F':0}
    if aString[0].upper() not in d1:
        return "unknown grade"
    var=d1[aString[0].upper()]
    if len(aString)==2:
        if aString[1]=='+':
            var+=0.3
        elif aString[1]=='-':
            var-=0.3
    return var
    
    
    
    
    

