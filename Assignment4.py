#Christopher Becker
#Assignment 4

#1
def partition(lst1,a):
    """This function takes a list of strings and a character as parameters.
       it prints any words that have value a first letter with value greater
       than the character input in the parameters."""
    for i in lst1:
        if a.upper()<=i[0].upper():
            print(i)
#2
def excludeName(lst1,a):
    """This function takes one string representing a list of names and one string
        that is just a name. It will print the names in the list that are not
        equivalent to the charater that is represented by the second."""
    for i in lst1:
        if a.upper()!=i.upper():
            print(i)
            
#3    
def stats(aFile):
    """This function takes a file as a parameter, opens the file, reads it, closes
       it and prints the line count,word count,and character count."""
    a=open(aFile)
    b=a.read()
    a.close()
    lineCount=b.count('\n')
    characterCount=len(b)
    wordCount=len(b.split())
    print('line count:', lineCount)
    print('word count:', wordCount)
    print('character count:', characterCount)
#4    
def printPositive(aFile):
    """This function takes a file as a parameter, reads the numbers from the file
       and prints the values that are greater than zero."""
    a=open(aFile)
    b=a.read()
    a.close()
    for i in b.split():
        if eval(i)>0:
            print(i)
#5            
def payroll(a,b):
    """This function takes an input file and an output file as parameters. It will
       calculate the total pay and write the amount to the output file."""
    aFile=open(a)
    bFile=open(b, 'w')
    x=aFile.readlines()
    for i in x:
        store=i.split()
        result=eval(store[0])*eval(store[1])
        bFile.write(str(result)+'\n')
    aFile.close()
    bFile.close()
    
        
        
    
    
