import string 
import pandas as pd

def scoreResponses(IEEETranscript, justresponses, keyorder): 
    list= []
    '''get percent correct'''

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
        #list = [correct, total, percent, response, targetsentence] # number correct, total words, and percent saved to a list

        #fieldnames = ["IEEE sentences", "Number of Targets", "Targets repeated", "Percent Correct"]


        dict = { "IEEE Sentences Num": key, 
                "Response": response, 
                "Number of Targets": total, 
                "Targets repeated": correct, 
                "Percent Correct": percent}
        list.append (dict) 
        
  #// TODO Todo save scores in a way that is easier to run analysis on 

    return (list)