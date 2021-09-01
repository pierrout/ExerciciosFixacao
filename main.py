# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
listaNumerica = ["1,2,3,4,5,6,7,8,9,10"]
print(listaNumerica)

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
novaLista = [21, 45, "maça", "fighting!", 5]
print(novaLista)

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
a = 'Bom'
b = ' Dia'
c = a + b
print(c)
print(a+b)

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla
tuplaNumerica = (1, 2, 2, 3, 4, 4, 4, 5)
print(tuplaNumerica.count(4))

# Exercício 5 - Crie um dicionário vazio e imprima na tela
dicionarioVazio = {}
print(dicionarioVazio)

# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
dicionarioIdade = {"Joao":13, "Rafaela":20, "Arielly":17}
print(dicionarioIdade)

# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
dicionarioIdade["Ana"]=21
print(dicionarioIdade)

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos.
# Imprima o dicionário na tela.
dicionarioNota = {"Matematica":10, "Portugues":8, "Fisica": ['6', '5']}
print(dicionarioNota)

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string,
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.
dicionarioMaluco = {"key1":"valor1","key2":"valor2"}
listaMaluca = ["pizza", (1,2), dicionarioMaluco,"valor2",8.5 ]
print(listaMaluca)

listaMaluca2 = ["pizza", (1,5), {"key1":"valor1","key2":"valor2"} ,"valor2",8.5 ]
print(listaMaluca2)

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
frase2 = frase[0:18]
print(frase2)
