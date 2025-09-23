nome = input("Qual seu nome?" )
idade = int(input("Qual a sua idade?" ))

with open("aula.9.txt","w") as arquivo:
    arquivo.write(f"nome : {nome}\n")
    arquivo.write(f"idade : {idade}\n")
