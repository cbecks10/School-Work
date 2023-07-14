#Lab 6
#Christopher Becker

#1
def average(aFile):
    infile=open(aFile)
    content=infile.read()
    infile.close()
    table=str.maketrans('.,;!?:\n', 7*' ')
    words=content.translate(table).split()
    count=0
    for i in words:
        count+=len(i)    
        
    z=count/len(words)
    print(z)

#2
def duplicates(aFile):
    infile=open(aFile)
    content=infile.read()
    infile.close()
    table=str.maketrans('.,;!?:\n', 7*' ')
    words=content.translate(table).split()
    uniqueLst=[]
    count=0

    for word in content:
        if word not in uniqueLst:
            uniqueLst.append(word)
        else:
            count+=1
    print('False')
            
            
    
