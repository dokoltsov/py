from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({"message":"hello world"})

@app.route('/healthz', methods=['GET'])
def health_check():
    return '', 200

@app.route('/readyz', methods=['GET'])
def readiness_check():
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)