
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

    stimlist = f"{PNum}{'IEEEList'}.csv"
    outputname= f"{PNum}{'merged'}{'score'}.csv"
    structpath = r'R:\khri-mehta-lab\Experiments\Projects\Kappa Project\HHF_KappaYear2\StimListBackups' #// TODO change so that you dont have to change per computer
    folderpath = r'R:\khri-mehta-lab\Experiments\Projects\Kappa Project\HHF_KappaYear2\ParticipantResponses'
    datafolder = r'R:\khri-mehta-lab\Experiments\Projects\Kappa Project\HHF_KappaYear2\DataOutputs'

    IEEETargets = getIEEEtargets()#Load IEEE Sentences 
    partresponses = combineTrans(PNum)

    os.chdir(structpath) #path to participant wav file 
    keyOrder = ordertostring(stimlist, structpath) #get the order of trials as strings to input as keys 

    checkpartlength(IEEETargets, partresponses, keyOrder)
    scoredict= scoreResponses(IEEETargets, partresponses, keyOrder) #Calculate score for each trial 

    
    writecsv(outputname, scoredict) # Export CSV of responses
    combinecsv(outputname, stimlist, PNum) 