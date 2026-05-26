from storage_handler import readcsv
import os 

def ordertostring(csvname, path):
    os.chdir(path)
    trailorder = readcsv(csvname)

    return (trailorder)