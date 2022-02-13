from socketserver import UDPServer, DatagramRequestHandler


class UDPHandler(DatagramRequestHandler):
    def handle(self):
        self.wfile.write(b"Ola, cliente\n")
        while True:
            # a função "strip" divide a linha com espaços
            data = print(self.rfile.readline().strip().decode("UTF-8"))
            if not data:
                break
            print(data)


if __name__ == "__main__":
    server_adress = ("localhost", 9090)
    with UDPServer(server_adress, UDPHandler) as server:
        # a função serve_forever() faz com que o servidor fique rodando até que a
        # requisição acabe ou a conexão termine.
        server.serve_forever()
