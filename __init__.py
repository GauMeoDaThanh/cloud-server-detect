from flask import Flask
from cloud_server_socket import ServerSocket

server_socket = ServerSocket()
server_socket.run()
