
from storage_handler import write_json, readjson
from CodeResponses import scoreResponses
from IEEEHandler import removearticles, reordersentences, downloadIEEE
from trialorder import ordertostring
from pathlib import Path 
import os 

if __name__ == "__main__":
    file = "101Block1clean" #Name of participants wav file 
    IEEEList = "IEEEsentences.json" #Name of IEEE sentences json #// TODO need to change this to just the list of target words 
    struct = "101IEEEList.csv"
    csvname = "101IEEEList.csv"
    structpath = 'R:\khri-mehta-lab\Experiments\Projects\Kappa Project\HHF_KappaYear2\StimListBackups'


    Partpath = Path(f"{file}.json") 
    folderpath = 'R:\khri-mehta-lab\Experiments\Projects\Kappa Project\HHF_KappaYear2\ParticipantResponses'
    os.chdir(folderpath) #path to participant wav file 
    if Partpath.exists(): #Does the participant json file exist?
        partresponses = readjson (f"{file}.json") #if it does read in the json
    else: 
        print ("transcript does not exist")

    IEEEpath = Path(f"IEEEsentences.json") #Path to IEEEsentence json - this file is in the original order
    if IEEEpath.exists(): 
        IEEEsentences = readjson(IEEEList) #read in IEEE transcript 
    else: 
        IEEEsentences=downloadIEEE() #If IEEE file isnt in folder it will download the IEEE sentences and write a json


    IEEETargets = removearticles(IEEEsentences) #function to remove extra words from the IEEE sentences 
    keyOrder=ordertostring(csvname, structpath) #get the order of trials as strings to input as keys 
    scoreResponses(IEEETargets, partresponses, keyOrder) #Calculate score for each trial 
