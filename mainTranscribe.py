from getTranscript import MakeTranscript
from storage_handler import write_json


if __name__ == "__main__":


    file = "prac"


    filewav = f"{file}.wav"

    conversation = MakeTranscript (filewav)
    write_json(f"{file}.json", conversation) 




