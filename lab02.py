def soma (num1,num2):
  resultado = num1 + num2
  return resultado

print("\n1 - somatório\n 2 - subtração\n 3 - multiplicação\n 4 - divisão")
operacaoDesejada = int(input("Digite o numero da operação desejada: "))

primeiroNumero = int(input("Digite o primeiro numero: "))
segundoNumero = int(input("Digite o segundo numero: "))

if (operaçãoDesejada == 1):
   print("resultado é ",soma(primeiroNumero,segundoNumero))

elif(operacaoDesejada == 2): 
  resultado = primeiroNumero - segundoNumero
  print(resultado)

elif(operacaoDesejada == 3):
  resultado = primeiroNumero*segundoNumero
  print(resultado)

else: 
  resultado = primeiroNumero/segundoNumero
  print(resultado)
