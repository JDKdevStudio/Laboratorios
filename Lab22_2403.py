#1.7 Escribe el código para un bucle tipo for el cual imprime desde número 0 hasta el 7. Utiliza una variable auxiliar llamada n.

for n in range (8):
    print(n)

#1.8 Modifica el rango del bucle anterior para que ahora imprima del número 1 hasta el 12.

for n in range (1,13,1):
    print(n)

#1.9 El siguiente programa cuenta cuantos de los números naturales menores que mil tienen un cubo terminado en siete. Explica cada línea de código e impleméntalo

c = 0
for i in range(1000):
    ultimo_digito = (i ** 3) % 10
    if ultimo_digito == 7:
        c += 1 #suma de la variable optimizada
print(c)

#2.1 Implementa dos ejemplos en tu Git de bucles anidados.
    #Ejemplo1
for i in range(0, 10):
    for j in range(0, i + 1):
        print("* ", end="")
    print("\r")

    #Ejemplo2
for i in range(0, 10):
    for j in range(0, i + 1):
        print(j, " ", end="")
    print("\r")
#Fin del laboratorio   
