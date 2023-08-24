from flask import Flask, request as req, jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    data = req.get_json()
    first = data['first']
    second = data['second']
    result = {
        'result': first+second
    }
    return jsonify(result)


@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = req.get_json()
    first = data['first']
    second = data['second']
    result = {
        'result': first-second
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
