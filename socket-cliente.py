import socket
import sys
from datetime import datetime
import time
import os
import commands

# Cria UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('horario local: %s' % str(datetime.now()))

server_address = ('10.10.3.103', 10000)
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
    msg = str(data.decode("utf-8"))
    serverTime = int(msg)
    currentServerTime = serverTime + (round(time.time() * 1000) - timeNow)
    print('horario do server: %s' % datetime.fromtimestamp(currentServerTime/1000.0))
    delta = currentServerTime - timeNow
    timestamp = ((round(time.time() * 1000) + delta) / 1000.0)
    print('horario local ajustado: %s' % datetime.fromtimestamp(timestamp))
    os.system("date +%s -s @" + str(timestamp))
    # print(str(currentServerTime))
finally:
    print('closing socket')
    sock.close()