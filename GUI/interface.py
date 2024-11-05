import tkinter as tk
from tkinter import messagebox
import socket

# Client-side networking code
class NetworkClient:
    def __init__(self, server_ip='localhost', server_port=9999):
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_socket = None
    
    def connect(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.server_ip, self.server_port))

    def send_request(self, request_type, message=None, signature=None):
        self.connect()
        self.client_socket.send(request_type.encode('utf-8'))
        
        if request_type == "SIGN":
            response = self.client_socket.recv(1024).decode('utf-8')
            print(response)  # Expecting "Send the message to sign"
            self.client_socket.send(message.encode('utf-8'))
            signature = self.client_socket.recv(1024)
            return signature.hex()

        elif request_type == "VERIFY":
            response = self.client_socket.recv(1024).decode('utf-8')
            print(response)  # Expecting "Send the message to verify"
            self.client_socket.send(message.encode('utf-8'))
            
            response = self.client_socket.recv(1024).decode('utf-8')
            print(response)  # Expecting "Send the signature"
            self.client_socket.send(bytes.fromhex(signature))
            verification_result = self.client_socket.recv(1024).decode('utf-8')
            return verification_result

        self.client_socket.close()


# GUI Application Code
class DigitalSignatureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Network-Based Digital Signature System")
        self.root.geometry("500x500")
        
        # Network Client
        self.network_client = NetworkClient()

        # UI Elements
        self.create_widgets()

    def create_widgets(self):
        # Message Input
        self.message_label = tk.Label(self.root, text="Message:")
        self.message_label.pack()
        self.message_entry = tk.Entry(self.root, width=50)
        self.message_entry.pack(pady=10)

        # Sign Button
        self.sign_button = tk.Button(self.root, text="Sign Message", command=self.sign_message)
        self.sign_button.pack(pady=10)

        # Signature Output
        self.signature_label = tk.Label(self.root, text="Signature:")
        self.signature_label.pack()
        self.signature_text = tk.Text(self.root, height=4, width=50)
        self.signature_text.pack(pady=10)

        # Verify Button
        self.verify_button = tk.Button(self.root, text="Verify Signature", command=self.verify_signature)
        self.verify_button.pack(pady=10)

        # Verification Result
        self.verify_result_label = tk.Label(self.root, text="Verification Result:")
        self.verify_result_label.pack()
        self.verify_result_text = tk.Text(self.root, height=2, width=50)
        self.verify_result_text.pack(pady=10)

    def sign_message(self):
        message = self.message_entry.get()
        if not message:
            messagebox.showwarning("Input Error", "Please enter a message.")
            return
        try:
            signature = self.network_client.send_request("SIGN", message=message)
            self.signature_text.delete(1.0, tk.END)
            self.signature_text.insert(tk.END, signature)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to sign message: {e}")

    def verify_signature(self):
        message = self.message_entry.get()
        signature = self.signature_text.get(1.0, tk.END).strip()
        if not message or not signature:
            messagebox.showwarning("Input Error", "Please enter both the message and signature.")
            return
        try:
            result = self.network_client.send_request("VERIFY", message=message, signature=signature)
            self.verify_result_text.delete(1.0, tk.END)
            self.verify_result_text.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to verify signature: {e}")

# Run the application
root = tk.Tk()
app = DigitalSignatureApp(root)
root.mainloop()
