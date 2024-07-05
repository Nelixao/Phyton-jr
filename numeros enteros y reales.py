#Ejercicio 1. 
#Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
#Recordar qla fórmula para la conversión es:  ([°F] − 32) × 5 ⁄ 9.
fahrenheit=float(input("ingresa el grado en Farenrenheit: "))
celsius= (fahrenheit - 32) *5 /9
print("Celsius es igual", celsius,"°")

#Ejercicio 2. 
#Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
numero1=float(input("primer numero: "))
numero2=float(input("segundo numero: "))

print("la suma:",numero1+numero2)
print("la resta:",numero1-numero2)
print("la divicion:",numero1/numero2)
print("la multiplicacion:",numero1*numero2)

#Ejercicio 3. 
#Calcular el perímetro y área de un rectángulo dada su base y su altura.
x=float(input("ingresa la base:"))
y=float(input("ingresa la altura:"))

area=x*y/2
perimetro=(2*x)+(2*y)

print("el area es ",area)
print("el perimetro es",perimetro)

#Ejercicio 4. 
#Calcular la media de tres números pedidos por teclado.
x=float(input("ingresa primer numero:"))
y=float(input("ingresa segundo numero:"))
z=float(input("ingresa tercer numero: "))

media=(x+y+z)/3
print("la media es",media) 