import socket
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 9999))
server_socket.listen(5)

key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

print("Server is running and waiting for clients...")

def sign_message(message):
    hash_obj = SHA256.new(message.encode('utf-8'))
    signature = pkcs1_15.new(private_key).sign(hash_obj)
    return signature

def verify_signature(message, signature):
    hash_obj = SHA256.new(message.encode('utf-8'))
    try:
        pkcs1_15.new(public_key).verify(hash_obj, signature)
        return "Valid Signature"
    except (ValueError, TypeError):
        return "Invalid Signature"

while True:
    client_socket, addr = server_socket.accept()
    print(f"Client {addr} connected.")

    client_request = client_socket.recv(1024).decode('utf-8')

    if client_request == "SIGN":
        client_socket.send("Send the message to sign".encode('utf-8'))
        message = client_socket.recv(1024).decode('utf-8')
        signature = sign_message(message)
        client_socket.send(signature)
    
    elif client_request == "VERIFY":
        client_socket.send("Send the message to verify".encode('utf-8'))
        message = client_socket.recv(1024).decode('utf-8')
        client_socket.send("Send the signature".encode('utf-8'))
        signature = client_socket.recv(1024)
        result = verify_signature(message, signature)
        client_socket.send(result.encode('utf-8'))
    
    client_socket.close()
