import string 
def extractResponses(partresponses, speakernum): 
    '''get just the participants responses'''
    justresponses = [] #Empty list that will be just the participants responses 
    for response in partresponses: #loop through transcript
        if response['speaker'] == speakernum: #if its speaker 0 add to new list 
            justresponses.append(response['text']) #Add to new list 
    return justresponses


def scoreResponses(IEEETranscript, justresponses): 
    '''get percent correct'''
    orderofkeys = "1", "2", "3", "4" #Will need a document with the order of the sentences

    correct= 0 #counter for score
    total = 0
    for i in range (len(justresponses)): #loop through IEEE sentences
        response = justresponses[i]
        key = orderofkeys[i]
        targetsentence = IEEETranscript[key] #get just the sentence
        for target in targetsentence: # loop through words in IEEE sentences
            clean_target = target.translate(str.maketrans('', '', string.punctuation))#get rid of puncuation
            total = total+1
            if clean_target in response: #If the target word is in the sentences 
                correct = correct+1 #add a point 
    
    print(correct/total)
    ...