# Exercício 1: O primeiro server que iremos utilizar é o nosso velho amigo HTTP,
# na camada de aplicação. Você pode tanto criar um, como utilizar um dos projetos
# ou exercícios dos módulos anteriores. A ideia é utilizarmos os conhecimentos do
# conteúdo e a ferramenta cURL para realizarmos uma chamada HTTP para ele.

# 1 - Faça uma chamada GET, utilizando o cURL.

curl localhost:3000

# ou

curl -X GET localhost:3000

# 2 - Faça uma chamada POST, utilizando o cURL, passando um JSON no body da requisição.

curl -X POST \
  -H 'Content-Type: application/json' \
  -d '{ "foo": "bar" }' \
  localhost:3000

# 3 - Faça uma chamada qualquer, utilizando o cURL, passando um header na requisição.

curl --request POST \
  --header 'Content-Type: application/json' \
  --header 'Authorization: ApiKey EXAMPLE-TOKEN' \
  --data '{ "foo": "bar" }' \
  localhost:3000

# Exercício 2: Ainda utilizando o cURL, vamos explorar mais alguns conceitos do
# HTTP, relembre que falamos que o HTTP organiza e dá significado aos dados
# encapsulados nessa camada, por exemplo, ao vermos um 200 tanto nós como um
# client HTTP sabe que aquela request foi realizada com sucesso, vamos explorar
# isso com o cURL.

# 1 - Faça uma chamada GET, utilizando o cURL, para "google.com".

curl google.com

# 2 -Perceba que foi retornado um 301 , isso quer dizer que existem diversos
# redirecionamentos que nos encaminha para o lugar certo, no caso, o caminho
# certo para a página do google é www.google.com . Ao acessarmos pelo navegador,
# não percebemos isso porquê ele faz o redirecionamento para a página certa
# para nós ao encontrar o 301 , porém, se você inspecionar a network você irá
# identificar esse redirecionamento. Faça uma nova chamada a "google.com",
# porém agora utilizando o parâmetro -L que serve para "seguir redirecionamentos".

curl -L google.com

# Exercício 3: Agora utilizando o wget, pegue o conteúdo da página do site da
# Trybe, depois abra o arquivo HTML baixado em seu navegador. Faça o mesmo
# processo com outras páginas web.

wget betrybe.com

# Exercício 4: Agora iremos para a camada de transporte. Crie um servidor
# TCP usando o módulo socketserver que já vem embutido com o Python. Nosso
# servidor TCP deverá:

# 1 - Responder com um "Olá, client", logo quando estabelecer uma conexão.
# 2 - Imprimir no console todo dado recebido.
# 3 - Responder com os dados recebidos (como um eco).
# 4 - Utilize a porta 8085.

# Perceba que o servidor sozinho não faz nada. Ele precisa que alguém se
# conecte a ele, então para testá-lo você pode utilizar o comando telnet
# localhost 8085 , onde telnet é a aplicação que iremos utilizar, localhost
# é o local onde o servidor está (no caso, o seu próprio PC) e 8085 é a
# porta em que o servidor está escutando conexões.

# Dicas:

# * a documentação do módulo traz exemplos de como instanciar seu servidor TCP
# * na mesma documentação, temos exemplos de classes para responder as requisições
# * os dados na requisição vêm em bytes -- não strings! bytes podem ser decodificados
# em string com a codificação correta
# * do mesmo jeito, para responder você pode precisar codificar strings em bytes
# * telnet sempre envia ASCII, já o netcat envia no encoding do sistema (em Linux,
# geralmente utf-8, mas confirme com o comando locale)

from socketserver import TCPServer, StreamRequestHandler

ADDRESS = "", 8085


class EchoHandler(StreamRequestHandler):
    """Responde requisições repetindo o que foi recebido."""

    def handle(self):
        # Usar b'' é um jeito literal de escrever bytes em ascii
        self.wfile.write(b"Hello, World!\n")
        # self.wfile e self.rfile são canais de entrada e saída
        # programados para ter a mesma interface de arquivos!
        for line in self.rfile:
            # esta linha responde o cliente
            self.wfile.write(line)
            # esta linha imprime no console
            print(line.decode('ascii').strip())

if __name__ == "__main__":
    # usando with nosso TCPServer vai arrumar a casa direitinho quando encerrado
    with TCPServer(ADDRESS, EchoHandler) as server:
        server.serve_forever()

# Exercício 5: Utilizando o comando telnet ou o Netcat (nc):

# 1 - Conecte no server do exercício anterior e envie informações, o server
# deverá imprimir as mensagens enviadas no console.
# 2 - Pare o servidor e verifique o que aconteceu com a conexão que estava
# aberta com o comando telnet ou nc.

nc -t 127.0.0.1 8085

# ou

telnet 127.0.0.1 8085

# Exercício 6: Reinicie o servidor TCP e agora faça uma requisição utilizando
# o cURL (HTTP), perceba o que é exibido no console do server já que não
# estamos utilizando o HTTP nele, perceba também que o comando cURL não
# recebe uma resposta HTTP com sentido (um status code 200, por exemplo),
# de modo que ele não sabe que aquela requisição chegou ao fim.

curl localhost:8085

# uma request mais legal:

curl --request POST \
    --data "{ \"foo\": \"bar\" }" \
    --header 'Content-Type: application/json' \
    --header 'Foo-Bar-Header: foo-bar' \
    localhost:8085/foo-bar
