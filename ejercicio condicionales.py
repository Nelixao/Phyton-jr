#sentencia condicionales
edad=int(input("ingrsa tu edad:"))
if edad <= 12:
    print("niño")
elif edad <= 18:
  print("adolecente")
elif edad <= 64:
  print("adulto")
else:
  print("anciano")

  #calif
calificacion=int(input("calificacion obtenida: "))

if calificacion >= 90:
  print("A")
elif calificacion <=89 and calificacion>=80:
  print("B")
elif calificacion <=79 and calificacion>=60:
 print("C") 
elif calificacion <=59 and calificacion>=40:
  print("D")
else:
  print("F")
  #par impar
num=int(input("ingresa tu numero:"))
residuo=num%2
if residuo==0:
 print("es par")
else:
 print("impar")
 #mayor menor
a=int(input("valor a: "))
b=int(input("valor b: "))
c=int(input("valor c: "))

if a>b and a>c:
    print("el mayor es a",a)

elif b>a and b>c:
    print ("el mayor es b",b)

elif c>a and c>b:
    print ("el mayor es c",c)

else:
    print("son iguales")
    #calculadora
x=float(input("primer valor: "))
y=float(input("segundo valor: "))
operador=input("ingresa aperador:")

if operador == "+":
 suma=x+y
 print(suma)

elif operador == "-":
 resta=x-y
 print(resta)

elif operador == "*":
 mul=x*y
 print(mul)

elif operador == "/":
 div=x/y
 print(div)


else:
 print("operador no conocido")
