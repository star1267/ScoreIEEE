from storage_handler import write_json, readjson
from bs4 import BeautifulSoup
import requests

def downloadIEEE(): 
    IEEE={}
    page = requests.get('https://www.cs.columbia.edu/~hgs/audio/harvard.html')
    soup = BeautifulSoup(page.text, "html.parser")
        # Finds all the words that are bold
    HarvardSentences = soup.find_all("li")
    for i in range (len(HarvardSentences)): 
        key = i +1 
        sentence = HarvardSentences[i].text
        IEEE.update({key:sentence})
    write_json(f"IEEEsentences.json", IEEE)
    return (IEEE)


def getIEEEtargets():
    #read in txt with bolded IEEE
    IEEEsentence= []

    with open("BoldIEEETarget.txt") as file:
        for line in file: 
            words = line.split()
            targetwords = [word for word in words if word[0].isupper()]
            IEEEsentence.append(targetwords)
    return (IEEEsentence)



