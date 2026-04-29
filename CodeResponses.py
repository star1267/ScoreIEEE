
def extractResponses(partresponses, speakernum): 
    justresponses = [] #Empty list that will be just the participants responses 
    for response in partresponses: #loop through transcript
        if response['speaker'] == speakernum: #if its speaker 0 add to new list 
            justresponses.append(response['text']) #Add to new list 
    return justresponses


def scoreResponses(IEEETranscript, justresponses): 
    counter= 0 #counter for score
    for i in range (len(justresponses)): #loop through IEEE sentences
        targetsentence = IEEETranscript[i] #get just the sentence
        for target in targetsentence: # loop through words in IEEE sentences
            if target in justresponses[i]: #If the target word is in the sentences 
                counter = counter+1 #add a point 
    print (counter)
    ...