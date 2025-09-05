programa {
  funcao inicio() {
    real kl,alt,imc
    escreva("Digite seu peso (kg): ")
    leia(kl)

    escreva("Digite sua altura (m): ")
    leia(alt)
    imc=kl / (alt*alt)
    escreva ("Seu IMC é: ",imc)
  }
}
