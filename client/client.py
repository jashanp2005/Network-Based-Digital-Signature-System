import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 9999))

operation = input("Enter operation (SIGN or VERIFY): ")
client_socket.send(operation.encode('utf-8'))

if operation == "SIGN":
    print(client_socket.recv(1024).decode('utf-8'))
    message = input("Enter message to sign: ")
    client_socket.send(message.encode('utf-8'))
    
    signature = client_socket.recv(1024)
    print("Signature:", signature.hex())

elif operation == "VERIFY":
    print(client_socket.recv(1024).decode('utf-8'))
    message = input("Enter message to verify: ")
    client_socket.send(message.encode('utf-8'))
    
    print(client_socket.recv(1024).decode('utf-8'))
    signature = bytes.fromhex(input("Enter signature (in hex): "))
    client_socket.send(signature)
    
    result = client_socket.recv(1024).decode('utf-8')
    print(result)

client_socket.close()
