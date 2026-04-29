from getTranscript import MakeTranscript
from storage_handler import write_json, readjson
from CodeResponses import extractResponses, scoreResponses
from IEEEHandler import removearticles, reordersentences, downloadIEEE
from pathlib import Path 

if __name__ == "__main__":
    file = "TessResponses" #Name of participants wav file
    IEEEList = "IEEEsentences.json" #Name of IEEE sentences json
    speakernum = 'speaker_0' #Which speaker does elevenlabs say the participant is? 

    orderlist = [1,4,270,30,7]

    def getTranscripts (file, folderpath): 
        # Create transcript for participant audiofile 
        filelist = [f"{file}.wav"]
        partresponses = MakeTranscript (filelist, folderpath) #make transcript
        write_json(f"{file}.json", partresponses) #Write transcript to json
        ... 


    Partpath = Path(f"{file}.json") 
    folderpath = 'C:/Users/testarr/Documents/pythoncode/SpeechToText' #path to participant wav file 
    if Partpath.exists(): #Does the participant json file exist?
        partresponses = readjson (f"{file}.json") #if it does read in the json
    else: 
        partresponses= getTranscripts(file, folderpath) #if not make the transcript 


    IEEEpath = Path(f"IEEEsentences.json") #Path to IEEEsentence json - this file is in the original order
    if IEEEpath.exists(): 
        IEEEsentences = readjson(IEEEList) #read in IEEE transcript 
    else: 
        IEEEsentences=downloadIEEE() #If IEEE file isnt in folder it will download the IEEE sentences and write a json

    IEEETargets = removearticles(IEEEsentences) #function to remove extra words from the IEEE sentences 
    print(IEEETargets[0])
    reordersentences(orderlist, IEEETargets)

    justresponses =extractResponses(partresponses, speakernum) #Extract just the participants responses 
    scoreResponses(IEEETargets, justresponses) 



