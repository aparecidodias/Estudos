programa {
  funcao inicio() {
    cadeia np
    real po,pf,vl
    const real desconto=0.15

    escreva("Nome do produto: ")
    leia(np)
  
    escreva("Preço original: ")
    leia(po)

    escreva("--- Preço Promocional --- \n")
    

  vl=po * desconto
  pf= po -vl
   escreva("Produto: ",np,"\n")

   escreva("Preço Original: R$",po, "\n")

   escreva("Desconto (15.0%): R$",vl, "\n")

   escreva("Preço Final: R$" ,pf)

    
  }
} 