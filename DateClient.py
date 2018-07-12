import socket
import sys
from datetime import datetime
import time

# Cria UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('horario local: %s' % str(datetime.now()))

server_address = ('localhost', 10000)
message = 'GET_TIME'
req = bytearray(message, 'ascii')
try:

    # Envia dados
    print('sending ' "%s" % message)
    sent = sock.sendto(req, server_address)

    # Recebe resposta
    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    timeNow = int(round(time.time() * 1000))
    msg: str = str(data.decode("utf-8"))
    serverTime: int = int(msg)
    currentServerTime: int = serverTime + (round(time.time() * 1000) - timeNow)
    print('horario do server: %s' % datetime.fromtimestamp(currentServerTime/1000.0))
    delta: int = currentServerTime - timeNow
    print('horario local ajustado: %s' % datetime.fromtimestamp(((round(time.time() * 1000) + delta) / 1000.0)))

finally:
    print('closing socket')
    sock.close()