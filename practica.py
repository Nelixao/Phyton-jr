

import math



num =int(input("ingresa numero= "))


while num<0:
   print("no, vuelve a intentar")
   num =int(input("ingresa numero= "))

print("respuesta")

         
raiz=math.sqrt(num)
print(raiz)

#2---------------
v=9

while v>=2:
  print("no")

#3--------------

oracion= "ten un buen dia "
contador=0
for i in oracion:
    contador=contador+1

print(f"tiene: {contador} caracteres")

#3.1--------------
oracion= input("ingresa: ")
contador=0
for i in oracion:
    contador=contador+1

print(f"tiene: {contador} caracteres")

#4------------
numero= int(input("la tabla del:"))
i=1
while i<=10:
 resultado=numero*i
 print(f"{i}x{numero}={resultado}")
 i=i+1
  
 

  



