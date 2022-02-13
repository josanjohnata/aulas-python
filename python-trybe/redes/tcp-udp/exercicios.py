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