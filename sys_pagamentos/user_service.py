from flask import Flask, request, jsonify

app = Flask(__name__)
users = []
@app.route('/register', methods=['Post'])

def register_user():
    data = request.get_json()
    users.append(data)
    return jsonify({"mensagem": "Usuário registrado com sucesso!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)