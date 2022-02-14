# Exercício 1: Defina uma regra de firewall utilizando o comando
# iptables -A que bloqueie (block ou REJECT/DROP) toda a entrada
# (in ou INPUT) de pacotes utilizando o protocolo ICMP, impedindo
# assim que a máquina responda ao comando ping. Lembre-se, você
# pode executar o comando ping para validar se sua regra está
# funcionando corretamente: ping 127.0.0.1 (você pode adicionar
# o parâmetro -O para exibir os pings rejeitados também).

iptables -A INPUT -p icmp -j REJECT

# Exercício 2: Exclua a regra anterior utilizando o parâmetro -D (Linux).

iptables -D INPUT -p icmp -j REJECT

# Exercício 3: Agora vamos criar uma regra para bloquear o tráfego
# HTTPS. Para isso iremos bloquear a saída de pacotes (out ou OUTPUT).
# Lembre-se, a porta padrão para esse protocolo é a 443, para
# especificá-la utilize o parâmetro --sport (Linux), ele utiliza
# também o protocolo tcp . Para testar sua regra, tente acessar um
# site pelo navegador que use o protocolo, como o Youtube, o Google
# ou o Facebook (via curl, se estiver rodando no docker).

iptables -A OUTPUT -p tcp --sport 443 -j REJECT

# Exercício 4: Bloqueie agora o tráfego de saída para HTTP.
# Lembre-se, também é utilizado o protocolo tcp e a porta 80.
# Para testar sua regra, tente acessar um site pelo navegador
# que use HTTP .

iptables -A OUTPUT -p tcp --sport 80 -j REJECT

# Exercício 5 : Para finalizar, vamos limpar todas as regras.
# Para isso, utilize o comando --flush do iptables (Linux).

iptables --flush

# Exercício 6: Agora, vamos utilizar um tipo de proxy bem legal
# que pode ser bastante útil no nosso dia como pessoas
# desenvolvedoras o NGROK , com ele conseguimos criar um túnel
# para o nosso localhost .

# 1 - Crie um servidor HTTP em sua máquina executando na porta 80,
# pode ser um frontend ou um backend criado em aulas anteriores.
# Python é um brinquedo que vem com todos os acessórios, lembra?
# Claro que ele vem com um servidor http pronto pra usar! Vamos
# criar um diretório novo e rodar o servidor lá dentro!

mkdir diretorio && cd diretorio
python3 -m http.server 80

# 2 - Baixe o ngrok e extraia o arquivo baixado em uma pasta de
# sua preferência, conforme instruções no site oficial.

unzip /path/to/ngrok.zip

# 3 - Conforme instruções do site, crie um túnel para a porta 80 de sua máquina.

./ngrok http 80

# 4 - Acesse o o link disponibilizado em seu navegador. Utilize ele para acessar
# de outros dispositivos, como seu smartphone ou outro computador.

./ngrok http 80

# Exercício 7: No conteúdo vimos o que são os protocolos SSL e TLS, vamos subir
# nosso próprio servidor HTTPS, utilizando nosso próprio certificado.

# 1 - Vamos utilizar a ferramenta OpenSSL para gerar nossos certificados.
# Ela já vem instalada na maioria das distros Linux. No Docker, no entanto,
# você vai precisar executar:

apt-get update && apt-get install python3 openssl

# Pra conferir se está instalado:

openssl -v

# 2 - Para gerar nosso próprio certificado auto-assinado, utilize os
# comandos abaixo. Lembrando que como nós estamos gerando o certificado,
# ele não será reconhecido por nenhuma entidade certificadora, de modo
# que ele só nos servirá para utilizar o protocolo TLS com o HTTPS, não
# sendo capaz de ser aceito pelo navegador, por exemplo, que não irá
# aceitá-lo, por não ter sido aprovado por nenhuma entidade reconhecida
# por ele.

openssl genrsa -out key.pem
openssl req -new -key key.pem -out csr.pem
openssl x509 -req -days 9999 -in csr.pem -signkey key.pem -out cert.pem
rm csr.pem

# 3 - Acabamos de gerar dois arquivos, o cert.pem (o certificado) e o
# key.pem (chave privada). Copie os dois arquivos para um diretório
# onde iremos criar nosso servidor HTTPS.

mkdir /some-dir/https-server
mv key.pem /some-dir/https-server
mv cert.pem /some-dir/https-server
cd /some-dir/https-server

# 4 - Agora vamos escrever um servidor https usando os módulos nativos
# do python ssl e http.server. Embora esses módulos tenham muitos muitos
# recursos (muitos mesmo), nós vamos usar apenas alguns. Tente seguir as
# instruções a seguir:
# 4.1 Crie um contexto SSL com a classe SSLContext, usando o protocolo
# de versão mais alta disponível para servidores. (dica: as opções estão
# listadas na documentação).
# 4.2 Carregue no contexto SSL a cadeia de certificação, passando tanto
# a o arquivo de certificação quanto a sua chave. (dica: existe um método
# para isso).
# 4.3 Crie uma instância de HTTPServer. O endereço deve ser uma tupla
# ('localhost', 8000) e para responder as requisições, use
# SimpleHTTPRequestHandler. (dica: apesar do exemplo na documentação,
# não use with.)
# 4.4 Crie um socket server-side usando o método wrap_socket do seu
# contexto SSL. Passe como parâmetro o socket do servidor (server.socket).
# 4.5 Substitua o socket do servidor pelo socket que vc acabou de criar.
# 4.6 Execute o servidor com o método serve_forever .

import ssl
from http.server import HTTPServer, SimpleHTTPRequestHandler

ssl_context = ssl.SSLContext()
ssl_context.load_cert_chain("cert.pem", keyfile="key.pem")

server_address = ("0.0.0.0", 8000)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)

httpd.serve_forever()

# Acesse o servidor utilizando o navegador. Perceba que ele irá informar
# que o certificado não é reconhecido por ele, pois não foi assinado por
# nenhuma entidade da confiança dele.
# Acesse o servidor novamente, porém, desta vez utilizando cURL (de fora
# do Docker, se vc estiver usando).

curl https://localhost:8000

# Por último, vamos utilizar um recurso do cURL, somente para testes
# (somente utilize, caso realmente você esteja esperando por aquilo),
# que é o parâmetro -k ou --insecure. Com ele, falamos para o nosso
# cURL prosseguir a request mesmo sabendo que a conexão não é "confiável".

curl --insecure https://localhost:8000
