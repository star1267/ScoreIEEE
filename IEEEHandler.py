from storage_handler import write_json, readjson
from bs4 import BeautifulSoup
import requests

def downloadIEEE(): 
    IEEE=[]
    page = requests.get('https://www.cs.columbia.edu/~hgs/audio/harvard.html')
    soup = BeautifulSoup(page.text, "html.parser")
        # Finds all the words that are bold
    HarvardSentences = soup.find_all("li")
    for sentences in HarvardSentences: 
        IEEE.append(sentences.text)
    write_json(f"IEEEsentences.json", IEEE)
    return (IEEE)


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


def reordersentences(order): 
    print (order)
    ...



