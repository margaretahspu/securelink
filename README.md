# SecureLink

SecureLink is a Python program designed to encrypt and decrypt data transmissions on Windows, ensuring secure and private communication. It utilizes symmetric encryption provided by the `cryptography` library to protect the integrity and confidentiality of messages.

## Features

- Generate a cryptographic key for encryption and decryption.
- Encrypt plain text messages to ensure secure transmission.
- Decrypt encrypted messages back to their original form.

## Requirements

- Python 3.6 or higher
- `cryptography` library

## Installation

First, ensure you have Python 3.6 or higher installed. Then, install the `cryptography` library using pip:

```bash
pip install cryptography
```

## Usage

1. Clone the repository or download the `secure_link.py` file.
2. Run the program using Python:

```bash
python secure_link.py
```

3. Follow the on-screen instructions to either encrypt or decrypt a message.

## How It Works

- **Encryption**: Converts a plain text message into an encrypted byte string using a symmetric key.
- **Decryption**: Converts the encrypted byte string back into the original plain text message using the same key.

The program automatically generates and saves a cryptographic key (`secure_link.key`) upon the first run. This key is necessary for both the encryption and decryption processes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

SecureLink is intended for educational purposes. While it uses industry-standard encryption methods, it comes with no guarantees. Use it at your own risk.