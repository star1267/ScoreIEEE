from getTranscript import MakeTranscript
from storage_handler import write_json, readjson
from CodeResponses import extractResponses, scoreResponses
from pathlib import Path 

if __name__ == "__main__":
    file = "TessResponses" #Name of participants wav file
    IEEEList = "IEEEsentences.json"

    def getTranscripts (file, folderpath): 
        # Create transcript for participant audiofile 
        filelist = [f"{file}.wav"]
        partresponses = MakeTranscript (filelist, folderpath) #make transcript
        write_json(f"{file}.json", partresponses) #Write transcript to json

        ... 

    def removearticles(IEEETranscript): 
        targets =[]
        for text in IEEETranscript: 
            articles = { 'on', 'to', 'of', 'is', 'was', 'were',  'in', 'at', 'the', 'a', 'and' }
            rest = []
            for word in text.split():
                if word.lower() not in articles: 
                    rest.append(word)
            targets.append(rest)
        write_json(f"Targetwords.json", targets)
        return (targets)
        


    Partpath = Path(f"{file}.json")
    folderpath = 'C:/Users/testarr/Documents/pythoncode/SpeechToText' #path to participant wav file 
    if Partpath.exists(): 
        partresponses = readjson (f"{file}.json")
    else: 
        partresponses= getTranscripts(file, folderpath)


    IEEEpath = Path(IEEEList)
    if IEEEpath.exists(): 
        IEEETranscript = readjson(IEEEList)
    else: 
        IEEETranscript = getTranscripts(IEEEList)
    
    IEEETargets = removearticles(IEEETranscript)


    

    justresponses =extractResponses(partresponses)
    scoreResponses(IEEETargets, justresponses)



