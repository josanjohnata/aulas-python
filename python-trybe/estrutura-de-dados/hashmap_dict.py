class Employee:
    def __init__(self, id_num, name):
        self.id_num = id_num
        self.name = name


class HashMap:
    def __init__(self):
        self._buckets = [[] for i in range(10)]

    def get_address(self, id_num):
        return id_num % 10

    def insert(self, employee):
        address = self.get_address(employee.id_num)
        self._buckets[address].append(employee)

    def get_value(self, id_num):
        address = self.get_address(id_num)
        for item in self._buckets[address]:
            if item.id_num == id_num:
                return item.name
        return None

    def has(self, id_num):
        address = self.get_address(id_num)
        return self._buckets[address] is not None

    def update_value(self, id_num, new_name):
        address = self.get_address(id_num)
        employee = self. _buckets[address]
        employee.name = new_name


if __name__ == "__main__":
    employees = [(14, 'name1'), (23, 'name2'), (10, 'name3'), (9, 'name4')]
    registry = HashMap()

    for id_num, name in employees:
        employee = Employee(id_num, name)
        registry.insert(employee)

    print(registry.get_value(23))

    print(registry.get_value(10))
    registry.update_value(10, 'name30')
    print(registry.get_value(10))

# Tente descobrir qual técnica de tratamento de colisão é utilizada pelo Dict,
# de Python e o HashMap, do Java. Em inglês, o termo de busca é "collision
# resolution".

# Solução

# A classe Dict utiliza o Open Addressing e Java utiliza Separate Chaining.
# Vamos entender isso com mais detalhes.
# A classe Dict, de Python, utiliza a técnica de tratamento de colisão chamada
# Open Addressing e busca o próximo espaço vazio em duas fases. Ambas as fases
# utilizam a representação binária da chave e aplicam fórmulas matemáticas
# para definir o próximo índice a ser visitado.
# A classe HashMap, de Java, utiliza a técnica de Separate Chaining, mas
# quando a lista do bucket começa a ficar grande, Java substitui essa lista
# por uma Árvore Binária de Busca, uma estrutura de dados que diferente, que
# não veremos no curso, mas já posso adiantar que é mais eficiente do que uma
# lista para operações de busca.


# Como as diferentes implementações afetam a performance? Quais são os prós e
# contras da implementação de cada linguagem?

# Solução

# A solução do Python determina o próximo índice a ser visitado de maneira
# relativamente randômica e resulta em uma complexidade assintótica de tempo
# de O(1). Por outro lado, para evitar que o vetor buckets fique rapidamente
# sem espaço, um Dict é inicializado com uma lista de tamanho 2**15 ints. Como
# em Python cada int ocupa 24 bytes, no mínimo, o uso de memória é
# considerável.
# Em Java, o tamanho inicial é menor, uma vez que o que tende a crescer são as
# chains de cada bucket e não a lista de buckets. Por outro lado, temos o
# trade-off com o custo de tempo. Para cada consulta, o tempo de busca é
# proporcional à quantidade de itens naquele bucket que, sendo uma árvore,
# chega a O(log n), sendo n a quantidade de itens naquele bucket.
# Resumindo: Python tem complexidade mais baixa, mas gasta muito espaço. Java
# utiliza bem melhor a memória, porém tem maior complexidade para consultas.

##############################################################################

# Instanciando a classe Dict
employee_registry = {}

# Inserindo dados
# objeto[chave] = valor
employee_registry[14] = 'name1'
employee_registry[23] = 'name2'
employee_registry[10] = 'name3'
employee_registry[9] = 'name4'
print(employee_registry)

# Alterando o nome do id 10
# objeto[chave] = novo_valor
employee_registry[10] = 'name30'
print(f"Novo valor do id 10, após a atualização: {employee_registry[10]}")


# Instanciação do objeto vazio
dict1 = {}
dict2 = dict()

# Instanciação com preenchimento inicial de dados
dict3 = {1: 'name1', 2: 'name2'}
print(f"Dicionário 1: {dict1}")
print(f"Dicionário 2: {dict2}")
print(f"Dicionário 3: {dict3}")

# Inserção e Alteração
# Se a chave não existir no dict, uma nova entrada será criada
# Se já existir, o valor será sobreposto
dict1[14] = 'name1'
print(f"Novo dicionário 1, pós inserção/alteração: {dict1}")

# Consulta e Remoção
# Se a chave não existir no dict, causa erro
name = dict1[14]
del dict1[14]
print(f"Dicionário 1 pós consulta e deleção: {dict1}")


##############################################################################

double = {i: i*2 for i in range(3, 21)}

for key in double.keys():
    if key % 2 is not 0:
        double[key] = key * 3


print(double)


# Para cada char na string:
#     - Se o char não estiver no dicionário, inclua com o valor 1;

#     - Se estiver, incremente o valor.


# Exemplo:

str = "bbbbaaaacccaaaaaaddddddddccccccc"
# saída: {'b': 4, 'a': 10, 'c': 10, 'd': 8}

str = "coxinha"
# saída: {'c': 1, 'o': 1, 'x': 1, 'i': 1, 'n': 1, 'h': 1, 'a': 1}
# Explicação: Nenhuma letra repete em coxinha :)

count_chars = {}

for char in str:
    if char not in count_chars:
        count_chars[char] = 1
    else:
        count_chars[char] += 1

print(count_chars)
