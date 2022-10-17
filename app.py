from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def hello_world():  # put application's code here

    if request.method == 'POST':
        prompt = request.form['text']
        processed_text = prompt.lower()
        return render_template('index.html', variable=processed_text)

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
