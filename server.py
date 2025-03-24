''' 
Executing this server initiates the application of emotion
detector to be executed over the Flask channel and deployed on
localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector(text_to_analyse):
    ''' 
    Executing this function initiates the application of emotion
    detector
    '''
    text_to_analyse = request.args.get('textToAnalyze')

    response = emo_detector(text_to_analyse)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid input ! Try again."

    return f"For the given statement, the system response is 'anger': \
{anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. \
The dominant emotion is {dominant_emotion}"


@app.route("/")
def render_index_page():
    '''
    Executing this function renders the index.
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)
