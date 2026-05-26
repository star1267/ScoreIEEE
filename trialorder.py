from storage_handler import readcsv
import os 

def ordertostring(csvname, path):
    os.chdir(path) #Change to folder with stimuli csv
    trailorder = readcsv(csvname) #read in csv

    return (trailorder) #return csv