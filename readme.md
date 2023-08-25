# Password Encryption and Decryption with Secret Key

This Python program allows you to securely encrypt and decrypt passwords using a generated secret key. It also includes an API and a basic front-end for testing the encryption and decryption processes.

## Features

- Encrypt passwords with a unique secret key
- Decrypt encrypted passwords using the same secret key
- API endpoints for encrypting and decrypting passwords
- Simple front-end interface for testing the functionality

## Usage

1. Run `main.py` to interact with the encryption and decryption functions through the terminal.
2. Access the API by running `api.py` and making POST requests to `/encrypt_password` and `/decrypt_password` endpoints.
3. Use the `index.html` file for a user-friendly web-based testing interface.

## How it Works

1. Generate a secret key and save it to a file.
2. Encrypt passwords by shifting characters based on the secret key.
3. Decrypt encrypted passwords using the secret key to reverse the encryption process.

## Contributing

Contributions are welcome! If you'd like to improve the encryption algorithm, enhance the API, or refine the front-end, feel free to submit pull requests.

## License

This project is licensed under the MIT License.

## Disclaimer

This project is intended for educational purposes. Use encryption responsibly and follow best practices for security.