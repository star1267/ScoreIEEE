
def getIEEEtargets():
    "Takes a list of IEEE where each target word is Bolded and grabs only target words"
    IEEEsentence= [] #empty list 

    with open("BoldIEEETarget.txt") as file: #open txt with IEEE sentences in order 
        for line in file: #one line
            words = line.split() #split the words 
            targetwords = [word for word in words if word[0].isupper()] #take just the upper case ones 
            IEEEsentence.append(targetwords) #add to list
    return (IEEEsentence) #return just target words 




