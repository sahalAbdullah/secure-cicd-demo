from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def index():
    return jsonify(message="Hello from the secure pipeline")

@app.get("/health")
def health():
    return jsonify(status="ok")
