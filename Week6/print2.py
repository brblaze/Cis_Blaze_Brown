def printmessage1(): 
    print ("I was called first")
    printmessage2()
    
def printmessage2():
    print('I was called from printmessage1')
printmessage1()