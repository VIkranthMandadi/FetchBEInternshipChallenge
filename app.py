from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "CORS-enabled Flask backend!"})

if __name__ == '__main__':
    app.run(port=8000, debug=True)