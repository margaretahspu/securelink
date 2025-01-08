import os
from cryptography.fernet import Fernet

class SecureLink:
    def __init__(self, key_file='secure_link.key'):
        self.key_file = key_file
        self.key = self.load_key()

    def generate_key(self):
        key = Fernet.generate_key()
        with open(self.key_file, 'wb') as key_file:
            key_file.write(key)
        print("New encryption key generated and saved.")

    def load_key(self):
        if not os.path.exists(self.key_file):
            self.generate_key()
        with open(self.key_file, 'rb') as key_file:
            key = key_file.read()
        return key

    def encrypt_message(self, message: str) -> bytes:
        fernet = Fernet(self.key)
        encrypted_message = fernet.encrypt(message.encode())
        return encrypted_message

    def decrypt_message(self, encrypted_message: bytes) -> str:
        fernet = Fernet(self.key)
        decrypted_message = fernet.decrypt(encrypted_message).decode()
        return decrypted_message

def main():
    secure_link = SecureLink()
    
    while True:
        print("\nSecureLink - Secure Data Transmission")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            encrypted = secure_link.encrypt_message(message)
            print(f"Encrypted message: {encrypted}")

        elif choice == '2':
            encrypted_message = input("Enter the encrypted message: ")
            try:
                decrypted = secure_link.decrypt_message(encrypted_message.encode())
                print(f"Decrypted message: {decrypted}")
            except Exception as e:
                print(f"Error in decryption: {e}")

        elif choice == '3':
            print("Exiting SecureLink.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()