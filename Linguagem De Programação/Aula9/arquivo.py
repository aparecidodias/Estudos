#read: ler
#write: subscreve/subscreve
#a = append

with open("dados.txt","w") as arquivo:
    arquivo.write("Bruno.\n")

with open("dados.txt","r") as arquivo:
    conteudo=arquivo.read()
    print(conteudo)
with open("dados.txt","a") as arquivo:
    arquivo.write("\nDias")

