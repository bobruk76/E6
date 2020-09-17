import os
from flask import Flask
from service import fib

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

@app.route('/')
def hello_world():
    return '{}'.format(fib(10))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)
