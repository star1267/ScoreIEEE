import json
import os
import csv 
import pandas as pd

def write_json(path, content):
    """This creates a json file and write the dict to that file."""
    #
    with open(path, "w") as output:
        json.dump(content, output, indent=2)

    ...

def readjson(path):
    """This function checks to see if there is already a json file under the name. If so it reads the file and returns the content of the file."""

    # Checks if the json file exists. If not it returns nothing and the function is done
    if not os.path.exists(path):
        return None

    #  if the json file does exist it moves on to this
    else:
        # Opens the json file and reads the content
        with open(path, "r") as input:
            # Puts the content from the json in the dict filecontent
            filecontent = json.load(input)
            # returns the filecontent
            return filecontent
    ...

def readcsv (filename): 
    data = pd.read_csv(filename)
    IEEEorder = data['itemNum'].tolist()
    return (IEEEorder)



def writecsv(filename, data, fieldnames, outputpath): 
    os.chdir(outputpath)
    """Write data to a csv"""
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    ... 

def combinecsv(scorename, stimlist, PNum, outputpath, strucpath): 
    """Combing 2 csv into 1 by adding columns"""
    score = pd.read_csv(scorename) #read in csv
    os.chdir(strucpath)
    stim = pd.read_csv(stimlist)
    os.chdir(outputpath)
    result = pd.concat([stim, score], axis=1) #concatonate

    outputname = f"{PNum}{'scoreandstim'}.csv" #name
    # Save to a new CSV
    result.to_csv(outputname, index=False)

    ... 