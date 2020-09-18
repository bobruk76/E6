import os
from flask import Flask, request, render_template
from service import fib

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fib')
def fib_web():
    num = request.args.get('num', default=10, type=int)
    return '{}-ый член последовательности Фиббоначи равен {}'.format(num, fib(num))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)
