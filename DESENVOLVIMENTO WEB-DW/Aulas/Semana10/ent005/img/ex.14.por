programa {

  
  funcao inicio() {
    real quant
    real di, pt,carro,km
    
    escreva("Qual a quantidade de KM percorrido pelo carro?: ")
    leia(quant)

    escreva("Qual a quantidade de dias que o carro foi alugado?: ")
    leia(di)

    carro=90
    km=0.20
    pt=(quant*km) + (di*carro)
   
    escreva("O valor total a pagar e : ", pt )
  }
}
