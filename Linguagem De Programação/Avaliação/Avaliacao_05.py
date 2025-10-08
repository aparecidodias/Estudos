try:
   a = int(input ("numerador : "))

   b = int(input ("denominador : "))

   d = a/b

except ZeroDivisionError:
   print ("não é possível dividir por zero.")

except ValueError:
   print ("valor inválido, digite um numero inteiro")   

else: 
   print (f"o resultado é : {d}")

finally: 
   print("seu programa foi executado")    
