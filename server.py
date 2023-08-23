from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    if request.headers['Content-Type'] != 'application/json':
        return 'Content-Type must be application/json', 400
    
    data = request.json
    first = data.get('first')
    second = data.get('second')
    if first is None or second is None:
        return 'Both "first" and "second" numbers are required in the request body', 400
    result = first + second
    return jsonify({"result": result}), 200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    if request.headers['Content-Type'] != 'application/json':
        return 'Content-Type must be application/json', 400
    
    data = request.json
    first = data.get('first')
    second = data.get('second')
    if first is None or second is None:
        return 'Both "first" and "second" numbers are required in the request body', 400
    result = first - second
    return jsonify({"result": result}), 200

if __name__ == '__main__':
    app.run(port=8080)
