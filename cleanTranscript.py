import string 

def checkpartlength(IEEETranscript, justresponses, keyorder):
    #// TODO What Happens if a participant gets a score of zero?? 
    "score responses until it hits a response with a zero"
    "This will help clean the transcripts"
    for i in range (len(justresponses)): #loop through IEEE sentences
        correct= 0 #counter for score
        total = 0 #counter for total words 
        response = justresponses[i]['text'] #response for loop
        
        key = keyorder[i] #key for loop
        targetsentence = IEEETranscript[key-1] #get just the sentence
        
        for target in targetsentence: # loop through words in IEEE sentences
            clean_target = target.translate(str.maketrans('', '', string.punctuation))#get rid of puncuation
            total = total+1 #add to total for each for 
            if clean_target.lower() in response: #If the target word is in the sentences 
                correct = correct+1 #add a point 
            

        percent = correct/total #calculate percent correct for this trial
        if correct == 0: #if the score is zero it will print out the target sentence and the response 
            print (response, i, i/90)
            print (targetsentence)
            return 
