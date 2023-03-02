from flask import Flask
from flask import make_response
app = Flask(__name__)



@app.route('/ping')
def hello_world():
    return 'pong'

if __name__ == '__main__':
    app.run(debug=True)
