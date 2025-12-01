import socket

HOST = '0.0.0.0'     # Listen on all network interfaces
PORT = 5001          # Port number

s = socket.socket()
s.bind((HOST, PORT))
s.listen(1)

print("Waiting for sender...")

conn, addr = s.accept()
print(f"Connected with: {addr}")

filename = conn.recv(1024).decode()
print(f"Receiving file: {filename}")

with open(filename, 'wb') as f:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        f.write(data)

print("File received successfully!")
conn.close()
s.close()
