#Christopher Becker
#CSC 241 Assignment 3

#1
def printMultiples(n,m):
   """This function takes two parameters from the user and prints the m multiples of n that the user input."""
   for z in range(n, (m+1)*n, n):
        print(z,end=' ')

#2   
def customSpam(a,b,c):
   """Creates a custom spam message based on the three strings input by the
      the user."""
   x=a.title()
   y=b.upper()
   print('Dear',x+',')
   print('We would like to let you know about a great opportunity.')
   print('You can make',end=' ')
   for character in y:
       print(character,end=' ')
   print('dollars in just a few short weeks!')
   print('This is a limited-time offer.')
   print('Please contact us at',c,'for more information.')
   
#3    
def ion2e(f):
    """ion2e takes a string from the user and,if said string ends in ion, it will
       replace the ion ending with an e. If the user inputs a word that does not
       end in ion, the function will return the word input."""
 
    if f[-3:]=='ion':
        return f[:-3] + 'e'
    return f

#4
def numLen(s,n):
    """This function takes a string and a number from a user and provides the number
       of times the letter input corresponds with the amount of characters in the
       phrase input."""
    if (n)<0:
        return 0
    b=0
    for a in s.split():
        if n==len(a):
            b+=1
    return b

#5
def makeNeg(a,b):
    """The function makeNeg takes a list and a number from the user and makes negative
       the index in the list of the number entered."""
    if (b)>= len(a):
        print('That index is not valid. The list was not changed.')
    else:
        if a[b]>0:
            a[b]=-a[b]
    

