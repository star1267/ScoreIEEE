from getTranscript import MakeTranscript
from storage_handler import write_json
from fileLoader import load_audio_files


if __name__ == "__main__":


    file = "prac"

    conversation = MakeTranscript (f"{file}.wav")
    write_json(f"{file}.json", conversation) 

 
    foldername = 'C:/Users/testarr/Documents/pythoncode/PitchAnalysis/FixLengthShift'

 # create a list of audio files 
    audio_files, GibFiles, IEEEFiles= load_audio_files()
    #write_json(f"{"IEEEList"}.json", IEEEFiles) 



