from flask import Flask, jsonify, request
from flask_cors import CORS
from model import run
import json

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    data = {
        "message":"Hello Dara"
    }
    return jsonify(data), 200

@app.post("/chat")
def start_chat():
    
    data = request.get_json()
    if not data or "text" not in data:
        # Return 400 error if "text" is not provided in the request
        return jsonify({"error": "Bad request", "message": "'text' is required"}), 400
        
    query = data.get("text")
    result={}
    if query:
        result = run(query)
    else:
        result =  run("")
        
        # Debugging: print types of each part of the data
 
    
        
    return jsonify(result), 200
   

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)

