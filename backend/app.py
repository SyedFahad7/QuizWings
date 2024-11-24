from flask import request, jsonify

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()  # Receive the message as JSON
    user_message = data.get('message')
    if user_message:
        # You will add logic here to process the message
        return jsonify({"response": f"Echo: {user_message}"})
    else:
        return jsonify({"error": "No message received"}), 400
