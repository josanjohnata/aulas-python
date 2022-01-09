# Números inteiros (int)
# O primeiros dos tipos numéricos é o int , que representa um número inteiro, isto é, escrito sem parte fracionária.
# O método type(operando) corresponde ao operador typeof operando do JavaScript.
a = 5
type(a)

# Números fracionários (float)
# O segundo tipo numérico é o float , também conhecido por ponto flutuante, que representa um número decimal ou fracionário.
a = 5.0
type(a)

# Números complexos (complex)
# Como novidade e último tipo numérico, temos o complex .
# Já vimos como representar números inteiros ou fracionários, mas sabia que números complexos podem ser representados também?
# Basta colocar o número real acrescido da sua parte imaginária, trocando o i por j.
3 + 4j # saída: (3+4j)
# Operações matemáticas podem ser feitas da mesma maneira com números complexos.
(3 + 4j) + 4 # saída: (7+4j)
a = 5j
type(a)

# Strings (str)
# Além dos tipos numéricos, temos o tipo de sequência de texto str , que representa uma cadeia de caracteres ou, como popularmente conhecida, uma string. As strings são definidas envolvendo um valor com aspas simples ou duplas.

# Booleanos (bool)
# Os valores booleanos True e False pertencem ao tipo embutido bool . Aqui devemos ficar atentos ao início maiúsculo dessas palavras reservadas.
# E temos ainda estruturas do tipo sequência( list , tuple , range ), conjuntos( set , frozenset ), mapeamento( dict ), sequências binárias( bytes , bytearray , memoryview ) e mais um monte!

# Listas (list)
# Sequência mutável e ordenada de elementos. Pode armazenar elementos heterogêneos, tem seu tamanho variável e cresce a medida que itens são adicionados.
# Sintaxe:
fruits = ["orange", "apple", "grape", "pineapple"]  # elementos são definidos separados por vírgula, envolvidos por colchetes

fruits[0]  # o acesso é feito por indices iniciados em 0

fruits[-1]  # o acesso também pode ser negativo

fruits.append("banana")  # adicionando uma nova fruta

fruits.remove("pineapple")  # removendo uma fruta

fruits.extend(["pear", "melon", "kiwi"])  # acrescenta uma lista de frutas a lista original

fruits.index("apple")  # retorna o índice onde a fruta está localizada, neste caso 1
 em seu programa
fruits.sort()  # ordena a lista de frutas