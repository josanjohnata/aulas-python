from socketserver import TCPServer, StreamRequestHandler


class TCPHandler(StreamRequestHandler):
    def handle(self):
        self.wfile.write(b"Ola, cliente\n")
        while True:
            # a função "strip" divide a linha com espaços
            data = print(self.rfile.readline().strip().decode("UTF-8"))
            if not data:
                self.wfile.write(b"Cliente desconectado\n")
                break
            print(data)


server_adress = ("localhost", 8080)
with TCPServer(server_adress, TCPHandler) as server:
    print("Server TCP ativo")
    # a função serve_forever() faz com que o servidor fique rodando até que a
    # requisição acabe ou a conexão termine.
    server.serve_forever()
