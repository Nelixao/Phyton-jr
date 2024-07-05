

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
    print("son iguales 2 o todos los valores")