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
