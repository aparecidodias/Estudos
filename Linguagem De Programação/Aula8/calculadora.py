import operacoes

print("== Calculadora ==")
print("1- somar")
print("2- subtrair")
print("3- multiplicar")
print("4- divisão")

opcao= int(input ("escolha a operação"))
A= float(input("digite o primeiro número:"))
B= float(input("digite o segundo número:"))

if opcao==1:
    print("resultado:", operacoes.soma(A,B))

elif opcao==2:
    print("resultado:", operacoes.subtração(A,B))
      
elif opcao==3:
    print("resultado:", operacoes.multiplicação(A,B)) 

elif opcao==4:
    print("resultado:", operacoes.Divisão(A,B))

else:
    print("opção invalida")

