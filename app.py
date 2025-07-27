from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Define chatbot responses
responses = {
    "hello": "Hello! How can I assist you today?",
    "how are you": "I'm just a bot, but I'm doing well. How about you?",
    "what is your name": "I'm a simple chatbot created to assist you.",
    "bye": "Goodbye! Have a great day!",
}
# Define the HTML template
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple AI Chatbot</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .chat-container { width: 300px; margin: auto; padding: 10px; border: 1px solid #ccc; border-radius: 10px; background-color: #f9f9f9; }
        .messages { height: 200px; overflow-y: auto; border-bottom: 1px solid #ddd; margin-bottom: 10px; }
        .message { padding: 5px; border-radius: 5px; margin-bottom: 5px; }
        .user-message { background-color: #d0f0c0; text-align: right; }
        .bot-message { background-color: #f0d0d0; }
        .user-input { width: calc(100% - 80px); padding: 10px; border-radius: 5px; border: 1px solid #ccc; }
        .send-button { width: 70px; padding: 10px; border-radius: 5px; border: 1px solid #ccc; background-color: #4CAF50; color: #fff; cursor: pointer; }
        .send-button:hover { background-color: #45a049; }
    </style>
</head>
<body>
    <div class="chat-container">
        <div class="messages" id="messages"></div>
        <input type="text" id="userInput" class="user-input" placeholder="Type a message...">
        <button id="sendButton" class="send-button">Send</button>
    </div>
    <script>
        const sendButton = document.getElementById('sendButton');
        const userInput = document.getElementById('userInput');
        const messages = document.getElementById('messages');

        function appendMessage(message, type) {
            const messageDiv = document.createElement('div');
            messageDiv.classList.add('message', type);
            messageDiv.textContent = message;
            messages.appendChild(messageDiv);
            messages.scrollTop = messages.scrollHeight;
        }

        function sendMessage() {
            const userMessage = userInput.value.trim();
            if (userMessage) {
                appendMessage(userMessage, 'user-message');
                fetch('/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: userMessage })
                })
                .then(response => response.json())
                .then(data => {
                    appendMessage(data.response, 'bot-message');
                });
                userInput.value = '';
            }
        }

        sendButton.addEventListener('click', sendMessage);
        userInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_template)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '').lower()
    response = responses.get(user_input, "Sorry, I don't understand that.")
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)