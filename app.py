from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/new-response', methods=['POST'])
def new_response():
    data = request.json  # Get JSON data from Google Forms
    print("Received form response:", data)
    return jsonify({"status": "success", "received": data}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
