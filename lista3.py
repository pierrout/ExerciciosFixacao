
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
