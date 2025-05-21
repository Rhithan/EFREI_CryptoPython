from flask import Flask, request, jsonify

app = Flask(__name__)

# Fonction simple de chiffrement
def encrypt(text, key):
    result = ''
    for char in text:
        result += chr((ord(char) + key) % 256)
    return result

def decrypt(text, key):
    result = ''
    for char in text:
        result += chr((ord(char) - key) % 256)
    return result

@app.route('/')
def home():
    return "Bienvenue sur l'API de cryptage/décryptage !"

@app.route('/encrypt/', methods=['POST'])
def api_encrypt():
    data = request.get_json()
    plain_text = data.get('text')
    key = data.get('key')

    if plain_text is None or key is None:
        return jsonify({'error': 'Paramètres manquants'}), 400

    try:
        key = int(key)
    except ValueError:
        return jsonify({'error': 'La clé doit être un entier'}), 400

    encrypted = encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted})

@app.route('/decrypt/', methods=['POST'])
def api_decrypt():
    data = request.get_json()
    encrypted_text = data.get('text')
    key = data.get('key')

    if encrypted_text is None or key is None:
        return jsonify({'error': 'Paramètres manquants'}), 400

    try:
        key = int(key)
    except ValueError:
        return jsonify({'error': 'La clé doit être un entier'}), 400

    decrypted = decrypt(encrypted_text, key)
    return jsonify({'decrypted_text': decrypted})

if __name__ == '__main__':
    app.run(debug=True)
