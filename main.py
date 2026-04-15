from getTranscript import MakeTranscript
from storage_handler import write_json, readjson

if __name__ == "__main__":


# Create transcript for participant audiofile 
    file = "prac" #Name of participants wav file
    filelist = [f"{file}.wav"]
    folderpath = 'C:/Users/testarr/Documents/pythoncode/SpeechToText' #path to participant wav file 
    conversation = MakeTranscript (filelist, folderpath) #make transcript
    write_json(f"{file}.json", conversation) #Write transcript to json


#Text to speech a list of IEEE wav files 
    wavfiles = readjson("WavList.json") 
    folderpath = 'C:/Users/testarr/Documents/pythoncode/PitchAnalysis/FixLengthShift' 
    IEEETranscript = MakeTranscript (wavfiles, folderpath)
    write_json(f"{'IEEE'}.json", IEEETranscript) #Write transcript to json
