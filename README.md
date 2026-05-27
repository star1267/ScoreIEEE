# Project Description 
This project loads in a json file of participants responses to the Harvard IEEE sentences and scores them. The code reads through each response from the participant and checks if each target word is in the response. 
For each target word the participant scores one point. 

## Files 
- store_handler - read, write and manipulate json and csv files
- CodeResponses - reads in participant responses and target words and gives points for each target word repeated
- IEEEHandler - Uses a txt of bolded IEEE sentences and grabs only the target words
- trialorder - gets trial order form stim csv
- combineTrans - combined the 16 seperate transcripts into one transcript
- checkpartlength - checks to see if any trials have a score of zero to see if the transcripts got messed up 
