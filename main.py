from getTranscript import MakeTranscript
from storage_handler import write_json, readjson
from CodeResponses import extractResponses
from pathlib import Path 

if __name__ == "__main__":
    file = "TessResponses" #Name of participants wav file
    IEEEList = "Samplecheck.json"

    def getTranscripts (file, folderpath): 
        # Create transcript for participant audiofile 
        filelist = [f"{file}.wav"]
        partresponses = MakeTranscript (filelist, folderpath) #make transcript
        write_json(f"{file}.json", partresponses) #Write transcript to json

        ... 



    Partpath = Path(f"{file}.json")
    folderpath = 'C:/Users/testarr/Documents/pythoncode/SpeechToText' #path to participant wav file 
    if Partpath.exists(): 
        partresponses = readjson (f"{file}.json")
    else: 
        partresponses= getTranscripts(file, folderpath)

    

    IEEEpath = Path(IEEEList)
    if IEEEpath.exists(): 
        IEEETranscript = readjson (IEEEList)
    else: 
        IEEETranscript = getTranscripts(IEEEList)



    extractResponses(IEEETranscript, partresponses)