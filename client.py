#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys


# Cliente UDP simple.

# Dirección IP del servidor.
SERVER = sys.argv[1]
PORT = int(sys.argv[2])

# Contenido que vamos a enviar
LINE = ""
for word in sys.argv[3:]:
        # Comprobamos si tenemos un 'register'
        if sys.argv[3] = 'register'
                LINE = 'REGISTER sip:' + sys.argv[4] + ' SIP/2.0\r\n\r\n'
        else
                LINE += word + " "

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, PORT))

# Enviamos un string
print "Enviando: " + LINE
my_socket.send(LINE + '\r\n')

# Recibimos datos del servidor
data = my_socket.recv(1024)
print 'Recibido -- ', data
print "Terminando socket..."

# Cerramos todo
my_socket.close()
print "Fin."
