import operacoes

print("== Conversão ==")
print("1- metro->cm")
print("2- cm->metro")
print("3- km->metro")


opcao= int(input ("escolha a operação"))
A= float(input("digite o  número:"))


if opcao==1:
    print("resultado:", operacoes.mcm(A))

elif opcao==2:
    print("resultado:", operacoes.cmm(A))
      
elif opcao==3:
    print("resultado:", operacoes.kmm(A)) 


else:
    print("opção invalida")
