import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)

# Import your cryptography functions here
from crypto_utils.crypto_utils import generate_key, load_key, encrypt, decrypt

class CryptoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cryptography App")
        
        # Initialize key file path
        self.key_file_path = None
        
        # Create and place widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Generate key button
        self.generate_key_button = tk.Button(self.root, text="Generate Key", command=self.generate_key)
        self.generate_key_button.pack(pady=10)

        # Load key button
        self.load_key_button = tk.Button(self.root, text="Load Key", command=self.load_key)
        self.load_key_button.pack(pady=10)

        # Encrypt/decrypt frame
        self.encrypt_decrypt_frame = tk.Frame(self.root)
        self.encrypt_decrypt_frame.pack(pady=10)

        # Message entry
        self.message_entry = tk.Entry(self.encrypt_decrypt_frame, width=50)
        self.message_entry.grid(row=0, column=0, padx=5, pady=5)

        # Buttons for encrypting and decrypting
        self.encrypt_button = tk.Button(self.encrypt_decrypt_frame, text="Encrypt", command=self.encrypt_message)
        self.encrypt_button.grid(row=0, column=1, padx=5, pady=5)

        self.decrypt_button = tk.Button(self.encrypt_decrypt_frame, text="Decrypt", command=self.decrypt_message)
        self.decrypt_button.grid(row=0, column=2, padx=5, pady=5)

        # Result text widget
        self.result_text = tk.Text(self.root, height=15, width=80)
        self.result_text.pack(pady=10)
        self.result_text.config(state=tk.DISABLED)  # Initially disabled to prevent user editing

    def generate_key(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".key", filetypes=[("Key Files", "*.key")])
        if file_path:
            try:
                generate_key(file_path)
                self.update_result_text(f"Success: Key generated and saved to {file_path}")
            except Exception as e:
                LOGGER.exception("Failed to generate key")
                self.update_result_text(f"Error: Failed to generate key: {e}")

    def load_key(self):
        file_path = filedialog.askopenfilename(filetypes=[("Key Files", "*.key")])
        if file_path:
            try:
                self.key_file_path = file_path
                self.update_result_text(f"Success: Key loaded from {file_path}")
            except Exception as e:
                LOGGER.exception("Failed to load key")
                self.update_result_text(f"Error: Failed to load key: {e}")

    def encrypt_message(self):
        if not self.key_file_path:
            self.update_result_text("Error: No key file loaded.")
            return

        message = self.message_entry.get()
        if not message:
            self.update_result_text("Warning: No message to encrypt.")
            return

        try:
            encrypted_message = encrypt(message, self.key_file_path)
            encrypted_message_str = encrypted_message.decode()  # Convert bytes to string
            self.update_result_text(f"Encrypted message:\n{encrypted_message_str}")
        except Exception as e:
            LOGGER.exception("Failed to encrypt message")
            self.update_result_text(f"Error: Failed to encrypt message: {e}")

    def decrypt_message(self):
        if not self.key_file_path:
            self.update_result_text("Error: No key file loaded.")
            return

        encrypted_message_str = self.message_entry.get()
        if not encrypted_message_str:
            self.update_result_text("Warning: No message to decrypt.")
            return

        try:
            encrypted_message = encrypted_message_str.encode()  # Convert string to bytes
            decrypted_message = decrypt(encrypted_message, self.key_file_path)
            self.update_result_text(f"Decrypted message:\n{decrypted_message}")
        except Exception as e:
            LOGGER.exception("Failed to decrypt message")
            self.update_result_text(f"Error: Failed to decrypt message: {e}")

    def update_result_text(self, text):
        self.result_text.config(state=tk.NORMAL)  # Enable editing to update text
        self.result_text.insert(tk.END, text + "\n")  # Insert new text with a newline
        self.result_text.yview(tk.END)  # Scroll to the end of the text widget
        self.result_text.config(state=tk.DISABLED)  # Disable editing again

if __name__ == "__main__":
    root = tk.Tk()
    app = CryptoApp(root)
    root.mainloop()
