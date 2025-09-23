try:
    a = int(input("numerador: "))

    b = int(input ("demonimador: "))
    d = a / b

except ZeroDivisionError:
    print("Não é possível dividir um numero por zero")

except ValueError:
    print ("Valor invalido. Digite apenas números inteiros.")

else:
    print (f"o resultado é {d}.")

finally:
    print ("O programa foi executado.")