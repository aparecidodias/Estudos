programa {
  funcao inicio() {
   real quant,mv
   real dv,ca,num1,cc
   escreva("Qual a quantidade de cigarros fumados por dia? ") 
   leia(quant)

   escreva("Quantos anos você ja fumou? ") 
   leia(num1)
   //cc=cada cigarro por hora, ca=cigarros por ano
   //mv=minuto de vida , dv= cada cigarro por dia
   ca=(quant*365)*num1
   mv=10
   cc=(ca*mv)/60
   dv=cc/24

   escreva("Quantos dias de vida irei perder se continuar fumando? \n")

   escreva("Você perdera  ",dv, " dias ")
   
  }
}
