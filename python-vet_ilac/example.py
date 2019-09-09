from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Flask does not work in NameCheapp is a false."

if __name__ == '__main__':
    app.run(host='0.0.0.0')
