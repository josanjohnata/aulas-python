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
