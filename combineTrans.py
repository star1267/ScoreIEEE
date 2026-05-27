import os 
from storage_handler import readjson, write_json
from pathlib import Path

def combineTrans(PNum, folderpath): 
    #// TODO Make this so that it does not matter how many transcripts there are 


    mergetrans = [] #empty list 

    os.chdir(folderpath) #path to participant wav file  #// TODO Change this so that it isnt hard coded 
    for i in range(4): #loop through first 4 transcripts 
        blockNum = i +1 # add 1 to each number for 0 indexing
        transcriptname = f"{PNum}{'Session1'}{'Block'}{blockNum}{'Clean'}.json" #Name of transcript 
        Partpath = Path(transcriptname) #makes a variable of the path to the file
        if Partpath.exists(): #Does the participant json file exist?
            blocktrans = readjson (transcriptname) #if it does read in the json
        else: 
            print ("transcript does not exist, Please make transcript")
        for trial in blocktrans: 
            mergetrans.append(trial) #Adds transcript to list 

    for i in range(4): #Loops through blocks of session 2
        blockNum = i +1 #loop through first 4 transcripts 
        transcriptname = f"{PNum}{'Session2'}{'Block'}{blockNum}{'Clean'}.json"#Name of transcript 
        Partpath = Path(transcriptname)#makes a variable of the path to the file
        if Partpath.exists(): #Does the participant json file exist?
            blocktrans = readjson (transcriptname) #if it does read in the json
        else: 
            print ("transcript does not exist")
        for trial in blocktrans: 
            mergetrans.append(trial) #Adds transcript to list 

    return(mergetrans)