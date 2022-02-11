import socket

sock = socket.socket()
sock.bind(("localhost", 9090))
sock.listen(1)
conn, addr = sock.accept()
print('connected:', addr)
f = open('txt.txt', 'w')
while True:
    data = conn.recv(1024)
    f.write(data.decode())
    if not data:
        break
    conn.send(data.upper())
conn.close()
f.close()
