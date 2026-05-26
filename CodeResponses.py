import string 
import pandas as pd

def scoreResponses(IEEETranscript, justresponses, keyorder): 
    list= [] #empty list 

    for i in range (len(justresponses)): #loop through IEEE sentences
        correct= 0 #counter for score
        total = 0 #counter for total words 
        response = justresponses[i]['text'] #response for loop

        if i <= 719: #will score the first 720 response lines
            key = keyorder[i] #key = what number the IEEE sentence is 
            targetsentence = IEEETranscript[key-1] #get just the sentence
            for target in targetsentence: # loop through words in IEEE sentences
                clean_target = target.translate(str.maketrans('', '', string.punctuation))#get rid of puncuation
                total = total+1 #add to total for each for 
                if clean_target.lower() in response: #If the target word is in the sentences 
                    correct = correct+1 #add a point 

            percent = correct/total #calculate percent correct for this trial

            #creates a dict with the below information
            dict = { "IEEE Sentences Num": key, 
            "Response": response, 
            "Number of Targets": total, 
            "Targets repeated": correct, 
            "Percent Correct": percent}
        else: 
            #creates a dict with the below information
            dict = { "IEEE Sentences Num": "NA", 
            "Response": response, 
            "Number of Targets": "NA", 
            "Targets repeated": "NA", 
            "Percent Correct": "NA"}

        list.append (dict) #Adds dict to the list 
        
    return (list)