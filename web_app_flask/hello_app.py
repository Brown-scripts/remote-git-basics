from flask import Flask,render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def hello(name):
    return f'<h1> Hello, {escape(name)}!<h1>'



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')