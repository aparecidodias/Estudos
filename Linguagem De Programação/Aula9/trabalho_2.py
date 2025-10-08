nome = input("Qual seu nome?" )
bv = input ("Boas vindas")

with open("avaliaçãoBruno.txt","w") as arquivo:
    arquivo.write(f"nome : {nome}\n")
    arquivo.write(f"Boas vindas : {bv}")
