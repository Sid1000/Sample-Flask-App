from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify({
        'greeting': 'Hello, my name is Siddhant Patil'
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)