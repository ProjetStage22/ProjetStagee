from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = "Cette fonctionnalité est en cours de développement."
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
