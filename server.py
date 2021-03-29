# import socket

# Pour approfondir - Serveur de plus en plus performant
# fork
# select
# asyncio + uvloop

# Challenge 10K


# Applications particulieres de ces sockets
# Sniffer   - regex - QA testing
# Honeypot (avec ligne directe vers le FBI)
# Convertisseur port série - UDP ou TCP (alternative socat)
# Définir vos propres protocoles de communication (nouvelle application)

# Pas intéressant
# Serveur HTTP, FTP, mail.
# Flask, Django

# socketserver
# http.server, http.client
# Flask


#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind(('', 52000))
#     s.listen(1)
#
#     c, addr = s.accept()  # Bloque la
#     print("Le client {} m'a contacte".format(addr))
#     with c:
#         while True:
#             data = c.recv(4096)  # Bloque ici
#             if not data:
#                 break
#
#             print("Le client a dit: ", repr(data))
#             c.sendall(data)

# import http.server
# import socketserver
#
# # https://docs.python.org/3/library/http.server.html
# # https://docs.python.org/3/library/socketserver.html
# # class MyTCPHandler(socketserver.BaseRequestHandler):
# #     def handle(self):
# #         data = self.request.recv(4096)
# #         print("Le client a dit: ", repr(data))
# #         self.request.sendall(data)
#
# MyHTTPHandler = http.server.SimpleHTTPRequestHandler
#
# # Factory (Patron de programmation)
# # ... Signifie ellipsis dans Python
# with socketserver.TCPServer(("0.0.0.0", 8000), MyHTTPHandler) as server:
#     server.serve_forever()


import flask

# https://pythonbasics.org/flask-tutorial-hello-world/

# Convention over configuration
app = flask.Flask("toto")   # flask.Flask(__name__)


@app.route('/')   # Patron decoration (decoration pattern)
def index():  # Simule une page index.html
    return "<h1>Toto</h1><p>Bonjour le monde</p>"

app.run("0.0.0.0", 8000)



# twisted, django