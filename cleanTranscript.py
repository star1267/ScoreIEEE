import string 

def checkpartlength(IEEETranscript, justresponses, keyorder):
    for i in range (len(justresponses)): #loop through IEEE sentences
        correct= 0 #counter for score
        total = 0 #counter for total words 
        response = justresponses[i]['text'] #response for loop
        
        #will score the first 720 response lines
        key = keyorder[i] #key for loop
        targetsentence = IEEETranscript[key-1] #get just the sentence
        for target in targetsentence: # loop through words in IEEE sentences
            clean_target = target.translate(str.maketrans('', '', string.punctuation))#get rid of puncuation
            total = total+1 #add to total for each for 
            if clean_target.lower() in response: #If the target word is in the sentences 
                correct = correct+1 #add a point 

        percent = correct/total #calculate percent correct for this trial
        if correct == 0: 

            print (response, i, i/90)
            print (targetsentence)

            raise Exception("Check Transcript")
            ...
