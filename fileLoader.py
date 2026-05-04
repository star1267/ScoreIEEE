import os 

def load_audio_files(foldername):
    names = ["Bella", "Clancy", "Matt", "River"] #Name of the three voices we are using 
    
    """ This function creates a list of all the Mp3s in a folder"""
    audio_files = [] #empty list
    IEEEFiles = {key: [] for key in names} #Create an IEEE dict with the voices names 
    GibFiles =  {key: [] for key in names} #create an Gib dict with the voices names 

    os.chdir(foldername)
    for filename in os.listdir(path = '.'): #loops through each file
        if filename.endswith(".wav"): #checks if it ends with mp3
            audio_files.append(os.path.join(filename)) #if it is an mp3 it adds it to the list 

# This is redundant 
            if "Gib" in filename: #checks if its a gibberish file 
                for name in names: 
                    if name in filename: 
                        GibFiles[name]. append(filename)
            if "IEEE" in filename: 
                for name in names: 
                    if name in filename: 
                        IEEEFiles[name]. append(filename)                

    return audio_files, GibFiles, IEEEFiles#returns the list

    ...