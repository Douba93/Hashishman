from main import hashman, unhashman, keygen, encrypt_key
from flask import Flask, request, jsonify
from flask_cors import CORS
from random import randint
import os

app = Flask(__name__)
CORS(app)


@app.route('/encrypt_password', methods=['POST'])
def encrypt_password():
    data = request.get_json()
    password = data.get('password')
    secret_key = keygen()
    encrypted_pass = hashman(password, secret_key)
    return jsonify({
        "message": "Password encrypted successfully",
        "encrypted_password": encrypted_pass,
        "secret_key": encrypt_key(secret_key, 10)
    })


@app.route('/decrypt_password', methods=['POST'])
def decrypt_password():
    data = request.get_json()
    encrypted_pass = data.get('encrypted_password')
    secret_key = data.get('secret_key')
    decrypted_pass = unhashman(secret_key, encrypted_pass)
    return jsonify({
        "message": "Password decrypted successfully",
        "decrypted_password": decrypted_pass
    })


if __name__ == '__main__':
    app.run(debug=True)