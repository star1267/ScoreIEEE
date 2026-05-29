from storage_handler import writecsv, combinecsv
from CodeResponses import scoreResponses
from IEEEHandler import getIEEEtargets
from trialorder import ordertostring
from combineTrans import combineTrans
from cleanTranscript import checkpartlength
from pathlib import Path
import os 

if __name__ == "__main__":

    PNum = input('What is the participant number?') #input participant number
    #PNum = '102'

    stimlist = f"{PNum}{'IEEEList'}.csv" #name of stim struct
    outputname= f"{PNum}{'score'}.csv" #Name of output file 

    currentDir = os.getcwd()
    structpath = os.path.join(currentDir, 'StimList') #Path to folder in directory with stim lists
    transpath  = os.path.join(currentDir, 'cleanTranscripts') #Path to folder in directory with clean transcripts 
    outputpath = os.path.join(currentDir, 'Outputs') #Path to a folder for outputs

    try:
        os.mkdir(transpath) #make "cleanTranscripts" folder 
        print(f"Directory '{transpath}' created successfully.")
    except FileExistsError:
        print(f"Directory '{transpath}' already exists.")
    try: 
        os.mkdir(structpath) #Make 'StimList' folder
        print(f"Directory '{structpath}' created successfully.")
    except:
        print(f"Directory '{structpath}' already exists.")
    
    try:
        os.mkdir(outputpath) #Make "output" folder
        print(f"Directory '{outputpath}' created successfully.")
    except: 
        print(f"Directory '{outputpath}' already exists.")


    IEEETargets = getIEEEtargets()#Load IEEE Sentences 
    partresponses = combineTrans(PNum, transpath) #combine 4 transcripts into one 

    keyOrder = ordertostring(stimlist, structpath) #get the order of trials as strings to input as keys 

    checkpartlength(IEEETargets, partresponses, keyOrder) #Check if the transcript has too many lines
    scoredict= scoreResponses(IEEETargets, partresponses, keyOrder) #Calculate score for each trial 


    fieldnames = ["IEEE Sentences Num", "Response", "Number of Targets", "Targets repeated", "Percent Correct"] #headers for csv

    writecsv(outputname, scoredict, fieldnames, outputpath) # Export CSV of responses
    combinecsv(outputname, stimlist, PNum, outputpath, structpath) #combine struct and scores to one csv