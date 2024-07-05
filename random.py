import random
#usuario adivine si la adivuina 

numero=int(input("ingresa un numero: "))
  
valor = random.randint(1,10)

print (valor)

while(numero!=valor):
  
  print ("incorrecto")

  numero=int(input("ingresa un numero: "))
  valor = random.randint(1,10)

  print (valor)
print("correcto")



  

