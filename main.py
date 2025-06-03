
from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

import os

# Get Discord webhook URL from secrets
DISCORD_WEBHOOK_URL = os.environ.get('DISCORD_WEBHOOK_URL')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        data = request.json
        message = data.get('message', 'Hello!')
        webhook_url = data.get('webhook_url')
        webhook_name = data.get('webhook_name', 'Bucu0368 Bot')
        
        if not webhook_url:
            return jsonify({"success": False, "error": "Webhook URL is required"})
        
        # Prepare the Discord webhook payload
        payload = {
            "content": message,
            "username": webhook_name if webhook_name else "Bucu0368 Bot"
        }
        
        # Send the message to Discord
        response = requests.post(
            webhook_url,
            data=json.dumps(payload),
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 204:
            return jsonify({"success": True, "message": "Message sent successfully!"})
        else:
            return jsonify({"success": False, "error": "Failed to send message"})
            
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
