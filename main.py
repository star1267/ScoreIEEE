from storage_handler import writecsv, combinecsv
from CodeResponses import scoreResponses
from IEEEHandler import getIEEEtargets
from trialorder import ordertostring
from combineTrans import combineTrans
from cleanTranscript import checkpartlength
import os 

if __name__ == "__main__":
    #// TODO would be great if this could be a command input 

    PNum = '101'

    stimlist = f"{PNum}{'IEEEList'}.csv" #name of stim struct
    outputname= f"{PNum}{'score'}.csv" #Name of output file 

    #// TODO change so that you dont have to change per computer Need to understand how paths actually work 
    #This needs to be changed to a relative path 
    
    structpath = r'R:\khri-mehta-lab\Experiments\Projects\Kappa Project\HHF_KappaYear2\StimListBackups' #path to stim stuct
    transpath = r'R:\khri-mehta-lab\Experiments\Projects\Kappa Project\HHF_KappaYear2\ParticipantResponses'#path to transcript

    IEEETargets = getIEEEtargets()#Load IEEE Sentences 
    partresponses = combineTrans(PNum, transpath) #combine 4 transcripts into one 

    keyOrder = ordertostring(stimlist, structpath) #get the order of trials as strings to input as keys 

    checkpartlength(IEEETargets, partresponses, keyOrder) #Check if the transcript has too many lines
    scoredict= scoreResponses(IEEETargets, partresponses, keyOrder) #Calculate score for each trial 


    fieldnames = ["IEEE Sentences Num", "Response", "Number of Targets", "Targets repeated", "Percent Correct"] #headers for csv
    writecsv(outputname, scoredict, fieldnames) # Export CSV of responses
    combinecsv(outputname, stimlist, PNum) #combine struct and scores to one csv