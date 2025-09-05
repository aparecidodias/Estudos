programa {
  funcao inicio() {
    cadeia ni
    real pu,pt
    inteiro quant
    escreva("Nome do item: ")
    leia(ni)
  
    escreva("Peso unitário (Oz): ")
    leia(pu)

    escreva("Quantidade em posse: ")
    leia(quant)

    escreva("--- Detalhes do Item --- \n")

  pt=quant*pu
   escreva("Item: ",ni,"\n")

   escreva("Quantidade: ",quant, "\n")

   escreva("Peso Unitário: ",pu," Oz \n")

   escreva("Peso Total: ",pt, " Oz")

    
  }
}