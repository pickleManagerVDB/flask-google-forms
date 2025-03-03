"""
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/new-response', methods=['POST'])
def new_response():
    data = request.json  # Get JSON data from Google Forms
    print("Received form response:", data)
    return jsonify({"status": "success", "received": data}), 200




@app.route('/cool')
def cool():
    
    print("ur him", data)





if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
"""

from flask import Flask

# Initialize Flask app
app = Flask(__name__)

# Define a simple route to test if the server is working
@app.route('/')  
def test_server():
    return "The server works!"  # This message will be displayed in the browser

# Run the app (only when executed locally, not on Render)
if __name__ == '__main__':
    app.run(debug=True)

