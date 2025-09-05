programa {
  funcao inicio() {
  real pc,cc,dv,ct
  
  
  escreva("Preço do combustível (R$/L): ")
  leia (pc)

  escreva("Consumo do carro (km/L): ")
  leia(cc)

  escreva("Distãncia da viagem (km): ")
  leia(dv)
  

  ct=dv/(cc/pc ) 
  escreva("O custo total da viagem será de R$ " ,ct ) 
  
  


  
  }
}
