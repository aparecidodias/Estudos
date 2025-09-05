programa {
  funcao inicio() {
    const cadeia nome="Energy Beam"
    const inteiro numero=20
    inteiro num, ct
    escreva("--- cauculadora de custo de Mana (Magia:" , nome ,") ---\n" )
  
    escreva("Quantas vezes você pretende lançar a magia " , nome ," ? " , num )
    leia(num)

  ct=num*numero
   escreva("Para lançar a magia '" , nome ,"' " , num , " vez(es), você gastará: ", ct , " de mana.")

    
  }
}