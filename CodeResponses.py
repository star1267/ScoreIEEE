from storage_handler import write_json, readjson

def extractResponses(IEEETranscript, partresponses): 



    justresponses = []
    counter= 0
    for response in partresponses: 
        if response['speaker'] == 'speaker_0': 
            justresponses.append(response['text'])
            
        for target in IEEETranscript: 
            if target in response["text"]: 
                counter = counter+1
    print (counter)

    ... 


