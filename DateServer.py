import socket
import sys
import time

# Cria UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Atrela socket a porta
server_address = ('localhost', 10000)
print ('starting up on %s port %s' % server_address)
sock.bind(server_address)

while True:

    # Recebe dados
    print ('\nwaiting to receive message')
    data, address = sock.recvfrom(4096)

    print ('received %s bytes from %s' % (len(data), address))
    msg: str = str(data.decode("utf-8"))
    print (msg)

    if data:

        # Envia resposta
        millis: int = int(round(time.time() * 1000))
        rep: str = str(millis)
        reply = bytearray(rep, 'ascii')

        sent = sock.sendto(reply, address)
        print ('sent %s bytes back to %s' % (sent, address))