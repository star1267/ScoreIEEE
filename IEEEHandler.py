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


def removearticles(IEEE): 
    targets ={}
    for key in IEEE: 
        articles = { 'on', 'to', 'of', 'is', 'was', 'were',  'in', 'at', 'the', 'a', 'and', 'who', 'us', 'from' , 'it', 'out', 'you', 'him', 'will', 'he'
                    'this', 'are' ,'than', 'but', 'us' }
        
        #// TODO sentence 4 THESE doesnt count 

        rest = []
        text = IEEE[key]
        for word in text.split():
            if word.lower() not in articles: 
                rest.append(word)
        targets.update({key: rest})
    write_json(f"Targetwords.json", targets)
    return (targets)


def reordersentences(order): 
    print (order)
    ...



