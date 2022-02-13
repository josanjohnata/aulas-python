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