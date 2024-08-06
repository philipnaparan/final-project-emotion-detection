"""
Filename: server.py
Description: Use to run the app.
"""

#Required modules
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_detector_function():
    """
    Function used to render the result.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    #print("RESPONSE DATA: ", response)

    response_text = None

    if response['dominant_dictionary'] is None:
        response_text = "Invalid text! Please try again."
    else:
        response_text = (
            f"For the given statement, the system response is 'anger': {response['anger']}, "
            f"'disgust': {response['disgust']}, 'fear': {response['fear']}, \n"
            f"'joy': {response['joy']}, 'sadness': {response['sadness']}. "
            f"The dominant emotion is {response['dominant_dictionary']}.")

    return response_text


@app.route("/")
def render_index_page():
    """
    Function used to render the default page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
