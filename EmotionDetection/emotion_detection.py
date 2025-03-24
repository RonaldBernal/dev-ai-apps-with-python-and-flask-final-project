''' 
emotion_detection.py - is a library to analyze emotions on a text using Watson NLP Library.
'''
import json
import requests

def emotion_detector(text_to_analyse):
    ''' 
    Executing this function calls the emotion analysis endpoint for Watson.
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    payload = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    response = requests.post(url, json=payload, headers=header, timeout=15)
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    if response.status_code == 200:
        output = {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': str(max(emotions, key=emotions.get))
        }
        return output

    return None