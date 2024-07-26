from flask import Flask, render_template, request
from chatbottask import ask_gemini  
import pyttsx3


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    question = None
    answer = None

    if request.method == 'POST':
        question = request.form['user_question']
        answer = ask_gemini(question)
        engine = pyttsx3.init()
        engine.say(answer)
        engine.runAndWait()

    return render_template('speech.html', question=question, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)