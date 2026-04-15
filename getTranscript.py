from elevenlabs.client import ElevenLabs
import yaml
from dotenv import load_dotenv
from io import BytesIO
import os 


def MakeTranscript(fileName, foldername): 
    '''Makes transcript of wav files'''
    
    def transcribe(audio_file_path, elevenlabs): #input wav files and api key
        os.chdir(foldername) 
        with open(audio_file_path, 'rb') as audio_file:
            result = elevenlabs.speech_to_text.convert(
                file=audio_file,
                model_id='scribe_v2',
                diarize=True,
                timestamps_granularity='word'
            )
            return result
    # Process the response


    def create_conversation_transcript(result):
        """Create a conversation-style transcript with speaker labels"""
        all_words = []
        if hasattr(result, 'words'):
            # Collect all words from all channels
                for word in result.words or []:
                    if word.type == 'word':
                        all_words.append({
                            'text': word.text,
                            'start': word.start,
                            'speaker_id': word.speaker_id,
                        })
        # Sort by timestamp
        all_words.sort(key=lambda w: w['start'])
        # Group consecutive words by speaker
        conversation = []
        current_speaker = None
        current_text = []
        for word in all_words:
            if word['speaker_id'] != current_speaker:
                if current_text:
                    conversation.append({
                        'speaker': current_speaker,
                        'text': ' '.join(current_text)
                    })
                current_speaker = word['speaker_id']
                current_text = [word['text']]
            else:
                current_text.append(word['text'])
        # Add the last segment
        if current_text:
            conversation.append({
                'speaker': current_speaker,
                'text': ' '.join(current_text)
            })
        return conversation
    # Format the output



    with open ('secrets.yaml', 'r') as f:  #opens yaml with apikey
        secrets = yaml.safe_load(f)
    apikey = (secrets ['secrets'] ['elevenlabs']['apikey']) #read and store API key
    elevenlabs = ElevenLabs( #tells 11labs what the api key is 
        api_key= apikey,
    )


    bigtrans =[] #create list of transcripts
    for file in fileName: 
        result = transcribe(file, elevenlabs)
        filetranscript = create_conversation_transcript(result)

        bigtrans.append(filetranscript)

    return (bigtrans)    