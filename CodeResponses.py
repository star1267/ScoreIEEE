import string 
import numpy as np 

def scoreResponses(IEEETranscript, justresponses, keyorder): 
    '''get percent correct'''

    for i in range (len(justresponses)): #loop through IEEE sentences
        correct= 0 #counter for score
        total = 0 #counter for total words 
        response = justresponses[i] #response for loop
        key = keyorder[i] #key for loop
        targetsentence = IEEETranscript[key] #get just the sentence
        for target in targetsentence: # loop through words in IEEE sentences
            clean_target = target.translate(str.maketrans('', '', string.punctuation))#get rid of puncuation
            total = total+1 #add to total for each for 
            if clean_target in response: #If the target word is in the sentences 
                correct = correct+1 #add a point 
        percent = correct/total #calculate percent correct for this trial
        list = [correct, total, percent] # number correct, total words, and percent saved to a list
        IEEETranscript[key].append(list) #list appended to the dictionary 

  #// TODO Todo save scores in a way that is easier to run analysis on 

    ...