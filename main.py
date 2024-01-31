from flask import jsonify, request
from flask import Flask
from firebase_admin import credentials, initialize_app, db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

service_account_key = './cert.json'
cred = credentials.Certificate(service_account_key)
initialize_app(cred, {'databaseURL': ''})

@app.route('/addMessage', methods=['POST'])
def addMessage(request):

    if request.method == "OPTIONS":
        # Allows requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Max-Age": "3600",
        }

        return ("", 204, headers)

    headers = {"Access-Control-Allow-Origin": "*"}
    
    try:
        
        
        message = request.get_json()  
        
        new_message_ref = db.reference('/chat-messages').push()
        new_message_ref.set({
            'username': message['username'],
            'text': message['text'],
            'timestamp': server_timestamp(),
        })

        return jsonify({"result": "Message added successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def server_timestamp():
    return {'.sv': 'timestamp'}

if __name__ == '__main__':
    app.run(port=8888)
