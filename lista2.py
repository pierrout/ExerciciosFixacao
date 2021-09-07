# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou 
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"
diaDaSemana = input("Qual dia da semana? ")

if (diaDaSemana == 'domingo') or (diaDaSemana == 'sabado'):
        print ("Hoje é dia de descanso")
else:
        print("Você precisa trabalhar")
    
# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista   
frutas = ['morango','uva','abacaxi','laranja','banana']
for saude in frutas:
    if saude == 'morango':
        print("tem!")
        break
    else:
        print("não tem")
        
        
# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma 
# lista
tp = (1,2,3,4)
lista = []
for elemento in tp:
    nv = elemento * 2
    lista.append(nv)   
print(lista)  

# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela
for contando in range (100,151):
     if (contando%2) == 0:
        print(contando)
        
        
# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35, 
# imprima as temperaturas na tela
temperatura = 40
while(temperatura > 35):
    print (temperatura)
    temperatura -= 1
    
# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa
contador = 0
while (contador < 100):
    print (contador)
    contador += 1
    if(contador ==23):
        break
  
 
# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, 
# adicione à lista, apenas os valores pares e imprima a lista
lista = []
x = 4
while (x <= 20):
    if (x%2==0):
        lista.append(x)
    x = x+1
print(lista)

# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)
nums = range(5, 45, 2)
# função list para converter
list(range(5, 45, 2))

# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.
temperatura = float(input('Qual a temperatura? '))
if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')

# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na 
# sua instrução de impressão

# “É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a 
# vantagem de existir.” (Machado de Assis)

frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir." 

cont = 0

for caracter in frase:
  if caracter == 'r':
    cont += 1
print (cont)

