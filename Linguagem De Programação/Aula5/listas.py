 #aula de hoje :criar listas

numero = [2,5,10,1,4,9,22,100,3]

print(len(numero)) # lentamanho da lista

print(min(numero)) # mino menor valon(numero) da lista

print(max(numero)) # max: o maior valor da lista

print(sum(numero)) # sum: e a soma de todos valores da lista

print(sorted(numero)) #sorted: ele organiza os numeros em ordem crescente

print(sorted(numero, reverse=True)) #reverse=Trueordem decrescente

print(numero[1]) #mostra o proximo numero da lista

print(1 in numero)  #mostra se o numero esta na lista 9true)

print(100 in numero)# mostra que o numero nao esta na lista(false)

print(numero)#mostra a lista

print(numero[2:8])#mostra a lista + 1 ate o valor 8

print(numero [2:] )#mesma coisa , porem se não especificar o terminal o programa vai usar o resto da lista

del(numero[1]) #del:ele deleta on numero desse valor
print(numero)

numero.append(101)#ele adiciona numeros
print(numero)