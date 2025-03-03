"""
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/new-response', methods=['POST'])
def new_response():
    data = request.json  # Get JSON data from Google Forms
    print("Received form response:", data)
    return jsonify({"status": "success", "received": data}), 200



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)

"""

from flask import Flask, request

app = Flask(__name__)

@app.route("/submit", methods=["POST"])
def handle_submission():
    data = request.json  # Receive JSON from Google Apps Script

    # Format the key-value pairs into a multi-line string
    formatted_data = "\n".join([f"{key}: {value}" for key, value in data.items()])

    print("Received data:\n", formatted_data)  # Log to console

    return f"Form submission received!\n\n{formatted_data}"

if __name__ == "__main__":
    app.run(debug=True)
