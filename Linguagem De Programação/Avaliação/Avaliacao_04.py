nome = input("digite seu nome: ")
nome = input("digite um nome: ")
nome = input("digite outro nome: ")

with open("aluno.txt", "w") as arquivo:
    arquivo.write(f"nome: {nome}\n")
    arquivo.write(f"nome: {nome}\n")
    arquivo.write(f"nome: {nome}\n")
    