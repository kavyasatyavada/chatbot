
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    data = request.get_json()
    message = data.get('message', '').strip().lower()

    print("User:", message)

    if message in ['hi', 'hello', 'hey']:
        reply = "Hey there! 😊 How are you?"

    elif 'how are you' in message:
        reply = "I'm doing great! Thanks for asking. How about you?"

    elif 'your name' in message:
        reply = "I'm Chat Buddy, your friendly chatbot! ❤️"

    elif 'joke' in message:
        reply = "Why did the computer go to the doctor? Because it had a virus! 😂"

    elif 'thank' in message:
        reply = "You're always welcome! 😊"

    elif 'bye' in message:
        reply = "Goodbye! Have a wonderful day! ❤️"

    elif 'good morning' in message:
        reply = "Good morning! Hope you have a beautiful day! ☀️"

    else:
        reply = "That's interesting! Tell me more. 😊"

    print("Bot:", reply)

    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)

