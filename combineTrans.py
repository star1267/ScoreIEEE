import os 
from storage_handler import readjson, write_json
from pathlib import Path
import glob 

def combineTrans(PNum, folderpath): 
    #// TODO Make this so that it does not matter how many transcripts there are 

    mergetrans = [] #empty list 
    session1= [] #Empty list of files with session one
    session2=[] #Empty list of files with session two 

    os.chdir(folderpath) #path to participant wav file
    files= glob.glob('*json*') #get list of json files in the transcript folder

    for file in files: #Loop through json files
        if PNum in file: #check if it has the participant number
            if "clean" in file.lower(): #check if its clean
                if 'session1' in file.lower() or 'sessionone' in file.lower(): #group into session 1
                    session1.append(file) #If it has session1 in the name it is added to list
                elif 'session2' in file.lower() or 'sessiontwo' in file.lower(): #group into session 2
                    session2.append(file) #if it has session2 in the name it is added to list

    for i in range(len(session1)): #loop through session 1 files
        keyword = f"{"block"}{i+1}" #First block
        transcriptname = [substring for substring in session1 if keyword in substring.lower()] #If it is this block
        transcriptname= " ".join(transcriptname) #turns this blocks file to string
        Partpath = Path(transcriptname) #makes a variable of the path to the file
        if Partpath.exists(): #Does the participant json file exist?
            blocktrans = readjson (transcriptname) #if it does read in the json
        else: 
            print ("transcript does not exist, Please make transcript") #If not file needs to be made 
        for trial in blocktrans: 
            mergetrans.append(trial) #Adds transcript to list 
            
    for i in range(len(session2)): #does the same for session2 
        keyword = f"{"block"}{i+1}"
        transcriptname = [substring for substring in session2 if keyword in substring.lower()]
        transcriptname= " ".join(transcriptname)
        Partpath = Path(transcriptname) #makes a variable of the path to the file
        if Partpath.exists(): #Does the participant json file exist?
            blocktrans = readjson (transcriptname) #if it does read in the json
        else: 
            print ("transcript does not exist, Please make transcript")
        for trial in blocktrans: 
            mergetrans.append(trial) #Adds transcript to list 

    return(mergetrans) #returns a long list of 720 responses