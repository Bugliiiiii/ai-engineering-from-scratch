from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(message="AI Dev API is running", status="ok")


@app.route("/health")
def health():
    return jsonify(status="healthy")


@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json()
    return jsonify(received=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
