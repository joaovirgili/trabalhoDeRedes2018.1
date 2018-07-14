import socket
import sys
import time

# Cria UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Atrela socket a porta
server_address = ('10.10.3.103', 10000)
print ('starting up on %s port %s' % server_address)
sock.bind(server_address)

while True:

    # Recebe dados
    print ('\nwaiting to receive message')
    data, address = sock.recvfrom(4096)

    print ('received %s bytes from %s' % (len(data), address))
    msg = str(data.decode("utf-8"))
    print (msg)

    if data:

        # Envia resposta
        millis = int(round(time.time() * 1000))
        rep = str(millis)
        # rep = str(0000000000)
        reply = bytearray(rep, 'ascii')

        sent = sock.sendto(reply, address)
        print ('sent %s bytes back to %s' % (sent, address))