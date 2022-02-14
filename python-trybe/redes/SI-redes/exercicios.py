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
