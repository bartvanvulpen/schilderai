from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def hello_world():  # put application's code here
    print('test')
    return render_template('templates/index.html')


if __name__ == '__main__':
    app.run()
