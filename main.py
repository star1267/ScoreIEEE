from getTranscript import MakeTranscript
from storage_handler import write_json, readjson
from CodeResponses import extractResponses
from pathlib import Path 
import yaml
from elevenlabs.client import ElevenLabs

if __name__ == "__main__":
    file = "prac" #Name of participants wav file
    IEEEList = "IEEESplit.json"

    def getTranscripts (file): 
        # Create transcript for participant audiofile 
        filelist = [f"{file}.wav"]
        folderpath = 'C:/Users/testarr/Documents/pythoncode/SpeechToText' #path to participant wav file 
        partresponses = MakeTranscript (filelist, folderpath) #make transcript
        write_json(f"{file}.json", partresponses) #Write transcript to json


    #Text to speech a list of IEEE wav files 
        wavfiles = readjson("WavList.json") 
        folderpath = 'C:/Users/testarr/Documents/pythoncode/PitchAnalysis/FixLengthShift' 
        IEEETranscript = MakeTranscript (wavfiles, folderpath)
        write_json(f"{'IEEE'}.json", IEEETranscript) #Write transcript to json
        ... 


    


    with open ('secrets.yaml', 'r') as f:  #opens yaml with apikey
        secrets = yaml.safe_load(f)
    apikey = (secrets ['secrets'] ['elevenlabs']['apikey']) #read and store API key
    elevenlabs = ElevenLabs( #tells 11labs what the api key is 
        api_key= apikey,
    )


    Partpath = Path(f"{"Split"}.wav")
    if Partpath.exists(): 
        partresponses = readjson (f"{file}.json")
    else: 
        partresponses= getTranscripts(file)


    IEEEpath = Path(IEEEList)
    if IEEEpath.exists(): 
        IEEETranscript = readjson (IEEEList)
    else: 
        IEEETranscript = getTranscripts(IEEEList)



    
    

    extractResponses(IEEETranscript, partresponses)