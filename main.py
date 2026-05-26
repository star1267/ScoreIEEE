
from storage_handler import readjson, writecsv, combinecsv
from CodeResponses import scoreResponses
from IEEEHandler import getIEEEtargets
from trialorder import ordertostring
from combineTrans import combineTrans
from pathlib import Path 
import os 

if __name__ == "__main__":
    PNum = '102'

    IEEEList = "IEEEsentences.json" #Name of IEEE sentences json #// TODO need to change this to just the list of target words 
    stimlist = f"{PNum}{'IEEEList'}.csv"
    outputname= f"{PNum}{'merged'}{'score'}.csv"
    structpath = 'R:\khri-mehta-lab\Experiments\Projects\Kappa Project\HHF_KappaYear2\StimListBackups' #// TODO change so that you dont have to change per computer
    folderpath = 'R:\khri-mehta-lab\Experiments\Projects\Kappa Project\HHF_KappaYear2\ParticipantResponses'

    IEEETargets = getIEEEtargets()#Load IEEE Sentences 
    partresponses = combineTrans(PNum)



    os.chdir(structpath) #path to participant wav file 
    keyOrder = ordertostring(stimlist, structpath) #get the order of trials as strings to input as keys 
    scoredict= scoreResponses(IEEETargets, partresponses, keyOrder) #Calculate score for each trial 

    writecsv(outputname, scoredict) # Export CSV of responses
    combinecsv(outputname, stimlist, PNum) 