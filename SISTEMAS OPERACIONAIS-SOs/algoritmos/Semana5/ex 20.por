programa {
  funcao inicio() {
    
    const inteiro XP_POR_MONSTRO_X = 150
    const real GP_MEDIO_POR_MONSTRO_X = 25.5
    const real PESO_LOOT_MEDIO_POR_MONSTRO_X = 3.2 
    const cadeia NOME_MONSTRO_PADRAO = "Cyclops"
    cadeia np
    inteiro md ,xpt
    real tt,ct,gpt,pt,lpc,xph,gph,pel
    
    escreva("--- Relatório Detalhado de Caçada no Tíbia --- \n")

    escreva("Monstro Caçado: ", NOME_MONSTRO_PADRAO, "\n")
    
  
    escreva("Nome do seu Personagem: ")
    leia(np)

    escreva("Quantos  ", NOME_MONSTRO_PADRAO,"(s) você derrotou? ")
    leia(md)

  
    escreva("Tempo total gasto na caçada (em horas, ex: 1.5 para 1h30min): ")
    leia(tt)

    escreva("custo total dos suprimentos (poções, etc.) em GPs: ")
    leia(ct)

    escreva("--- Relatório  da Caçada de Paladino Aventureiro --- \n")

    xpt= md * XP_POR_MONSTRO_X
    gpt= md * GP_MEDIO_POR_MONSTRO_X
    pt=  md * PESO_LOOT_MEDIO_POR_MONSTRO_X
    lpc= gpt - ct
    xph= xpt / tt
    gph= gpt/tt
    pel= md * PESO_LOOT_MEDIO_POR_MONSTRO_X 

    escreva("Monstro Focado: ",NOME_MONSTRO_PADRAO,"\n")
    escreva("Quantidade Derrotada:" ,md,"\n")
    escreva("Tempo da Caçada: ",tt," Horas\n")
    escreva("------------------------------------------------------\n")
    escreva("XP Total Ganhada: ",xpt," pontos de experiência \n")
    escreva("GP Total Estimado Coletado: ",gpt, " GPs \n")
    escreva("Peso Estimado do Loot: ", pel , " Oz \n")
    escreva("------------------------------------------------------\n")
    escreva("Custo dos Suprimentos: ",ct, " GPs \n")
    escreva("Lucro/Prejuízo Estimado: ",lpc, " GPs \n")
    escreva("------------------------------------------------------\n")
    escreva("Média de XP por Hora: ",xpt, " XP/h \n")
    escreva("Média de GP por Hora: ",gpt, " GP/h \n")
    escreva("------------------------------------------------------\n")
    escreva("Bom jogo, Paladino Aventureiro!")




  
    

   

    
  }
} 