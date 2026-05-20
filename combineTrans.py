import os 
from storage_handler import readjson
from pathlib import Path

def combineTrans(PNum): 
    folderpath = 'R:\khri-mehta-lab\Experiments\Projects\Kappa Project\HHF_KappaYear2\ParticipantResponses'
    mergetrans = []
    os.chdir(folderpath) #path to participant wav file 
    for i in range(4): 
        blockNum = i +1 
        transcriptname = f"{PNum}{'Block'}{blockNum}{'Clean'}.json"
        Partpath = Path(transcriptname) 
        if Partpath.exists(): #Does the participant json file exist?
            blocktrans = readjson (transcriptname) #if it does read in the json
        else: 
            print ("transcript does not exist")


        for trial in blocktrans: 
            mergetrans.append(trial)

    return(mergetrans)