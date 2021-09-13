
# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) e 
# depois faça uma chamada à função para listar os números      

def numPar ():
  for i in range (0,21,2):
    print (i)
  return

numPar()

# Exercício 2 - Crie uam função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string

def maiusculo (palavra):
  palavra = palavra.upper()
  print(palavra)
  return palavra

maiusculo('aluno aki ')

# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista

listaNumerica = ["1,2,3,4"]

def adicionar (lista):
  # função para adicionar elementos a lista
  # append vs extend 
  # append adiciona qualuqer valor por completo, a lista inteira por ex
  # extend é em uma estrutura iterável, se tem uma lista vai varrer essa lista e adicionará objeto por objeto
  lista = ["5,6"]
  listaNumerica.extend(lista)
  print(listaNumerica)
  return

adicionar(listaNumerica)


# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas 
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos

listaNumerica2 = []

def adicionar2 (arg1,*lista):

  print(arg1)

  for contador in lista:   
      print(contador)
  return;
  
adicionar2(1)
adicionar2(2,3,4)


# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2 
# números como parâmetro e retornar a soma deles

numeros = [40,50]
soma = lambda valores: sum (valores)
soma(numeros)


# Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local
total = 0
def soma( arg1, arg2 ):
    total = arg1 + arg2; 
    print ("Dentro da função o total é: ", total)
    return total;

soma( 10, 20 );
print ("Fora da função o total é: ", total)


# Exercício 7 - Abaixo você encontra uma lista com temperaturas em graus Celsius
# Crie uma função anônima que converta cada temperatura para Fahrenheit
# Dica: para conseguir realizar este exercício, você deve criar sua função lambda, dentro de uma função 
# (que será estudada no próximo capítulo). Isso permite aplicar sua função a cada elemento da lista
# Como descobrir a fórmula matemática que converte de Celsius para Fahrenheit? Pesquise!!!
Celsius = [39.2, 36.5, 37.3, 37.8]
# o map intera cada item da lista e cria uma nova lista c os numeros novos
Fahrenheit = map(lambda totalGrau: ((totalGrau * 1.8)+32),Celsius)
print (list(Fahrenheit))

#veja filter, map, functools, reduce

# Exercício 8
# Crie um dicionário e liste todos os métodos e atributos do dicionário

dicionario  = {"chave1": "valor1", "chave2": "valor2"}
dir(dicionario)


# Exercício 9
# Abaixo você encontra a importação do Pandas, um dos principais pacotes Python para análise de dados.
# Analise atentamente todos os métodos disponíveis. Um deles você vai usar no próximo exercício.
import pandas as pd
dir(pd)


# ************* Desafio ************* (pesquise na documentação Python)

# Exercício 10 - Crie uma função que receba o arquivo abaixo como argumento e retorne um resumo estatístico descritivo 
# do arquivo. Dica, use Pandas e um de seus métodos, describe()
# Arquivo: "binary.csv"
import pandas as pd
file_name = "binary.csv"

def recebendo (arquivo):
  df = pd.read_csv(arquivo)
  
  return df.describe()

recebendo(file_name)
