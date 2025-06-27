from flask import Flask
import os

app = Flask(__name__)

RUN_MODE = os.environ.get('RUN_MODE')

@app.route('/')
def hello():
    return f"Hello, World! (RUN_MODE={RUN_MODE})"

if __name__ == '__main__':
    app.run()