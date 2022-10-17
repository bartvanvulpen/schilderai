from flask import Flask, render_template, request
import time
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():  # put application's code here
    if request.method == 'POST':
        prompt = request.form['text']
        processed_text = prompt.lower()
        return render_template('index.html', variable=processed_text)

    return render_template('index.html')


@app.route('/clicked', methods=['POST'])
def show_img():  # put application's code here
    return "IMG HERE"

if __name__ == '__main__':
    app.run()
