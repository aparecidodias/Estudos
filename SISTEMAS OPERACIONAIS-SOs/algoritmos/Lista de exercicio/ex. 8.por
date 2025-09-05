programa {
real dist1,km,hm,dam,dm,cm,mm
  funcao inicio() {
    //entrada
   escreva("Digite uma distáncia em metros: ") 
   leia (dist1)

   //Saída
escreva("A distância de " ,dist1,"m corresponde a:\n")
//km
  km=dist1/1000 
escreva(km,"km")

//hm
  hm=dist1/100
escreva(hm,"hm")

//dam
  dam=dist1/10
  escreva(dam,"dam")

//dm
  dm=dist1*10
  escreva(dm,"dm")

  //cm
  cm=dist1*100
  escreva(cm,"cm")

  //mm
  mm=dist1*1000
  escreva(mm,"mm")


  
 

  }
}
