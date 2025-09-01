programa {

  //Variaaveis
  cadeia prod_1, prod_2,item_1,item_2
  inteiro quant_1, quant_2
  real preco_1, preco_2, subt_1,subt_2, vt
 
  funcao inicio() {
    
      //boas vindas

  escreva("--- Supermercado Preço Bom ---\n")
  escreva("Vamos registrar sua compra!\n")

  // entrada dados produtos

  escreva("--- PRODUTO 1 ---\n ")
  escreva("digite o nome do produto: ")
  leia(prod_1)
  escreva("digite a quantidade: ")
  leia(quant_1)
  escreva("digite o preço unitário: ")
  leia(preco_1)
  
  escreva("--- PRODUTO 2 ---\n")
  escreva("digite o nome do produto: ")
  leia(prod_2)
  escreva("digite a quantidade: ")
  leia(quant_2)
  escreva("digite o preço unitário: ")
  leia(preco_2)

  //cauculo recibo compra

  item_1=prod_1
  subt_1=quant_1*preco_1

  item_2=prod_2
  subt_2=quant_2*preco_2

  vt=subt_1+subt_2

  // recibo compra
  escreva("--- RECIBO DE COMPRA ---\n ")
  escreva("item: " ,  prod_1,"\n")
  escreva("qtde: " ,  quant_1,"| Preço Unit R$: ",preco_1, "| Subtotal: R$  ", subt_1,"\n")
 

  escreva("item: " ,  prod_2,"\n")
  escreva("qtde: ", quant_2,"| Preço Unit R$: ",preco_2, "| Subtotal: R$ ", subt_2,"\n")
  //VALOR TOTAL

  escreva("---------------------------------\n")
  escreva("VALOR TOTAL DA COMPRA:  R$",vt,"\n")
  escreva("-----------------------------------")

  


}
}
