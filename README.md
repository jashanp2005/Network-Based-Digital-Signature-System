### Network Based Digital Signature System


This project implements a Network-Based Digital Signature System that allows users to securely sign and verify digital messages using RSA cryptography. 
The system is built on a client-server architecture, where the server is responsible for signing messages with its private key and verifying signatures with its public key. 
The client interacts with the server through a socket-based communication protocol, sending requests for signing or verifying messages. 

The project integrates a graphical user interface (GUI) using Tkinter, allowing users to input messages, sign them, and verify the authenticity of signatures in an intuitive and interactive manner. 
The digital signature is generated using RSA encryption, where the server’s private key is used to sign a message, and the public key is used to verify the integrity and authenticity of the signed message. 

The system operates over a local network, ensuring that digital messages are protected against tampering and impersonation, thus enabling secure communication in distributed environments. 
This project demonstrates the practical use of RSA public-key cryptography in a networked application, providing both security and usability. 

Key Features: 

1) RSA Digital Signature: Secure signing and verification using RSA keys (2048-bit). 
2) Client-Server Architecture: The client communicates with the server to request message 
signing or verification. 
3) Graphical User Interface (GUI): Intuitive interface for signing and verifying messages. 
4) Socket Communication: Real-time message exchange between client and server. 

This system is suitable for applications requiring message authenticity and non-repudiation, such 
as in secure communications, digital contract signing, and authentication services. 
