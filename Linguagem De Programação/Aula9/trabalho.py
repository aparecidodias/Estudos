try:
    numero_a = int (input("Digite um número Inteiro: "))# colocar a variavel

except ValueError:#se der erro vai ser executado
    print("Entrada invalida. Tente novamente. ")

else:# se der certo vai ser executado
    print("Número válido. ")

finally:#esse vai ser executado de qualquer jeito
    print("o programa foi executado com sucesso. ")