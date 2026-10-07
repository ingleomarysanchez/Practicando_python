

#*          Ejercicio 1: Condicional Simple
# Escribe un programa que solicite o defina una variable temperatura. 
# Si la temperatura es mayor a $30, debe imprimir el mensaje: "Hace mucho calor".
# (Si no es mayor a $30$, no debe hacer nada).

Temperatura = 40
Calor= True


if Temperatura > 30:
    print ("Hace mucho Calor")

#*========================================================*#

# *     Ejercicio 2: Condicional Doble (if-else)
# Escribe un programa que reciba un número entero en una variable numero.
#  Si el número es par, debe imprimir "El número es par". En caso contrario,
#  debe imprimir "El número es impar".
# (Pista: Recuerda usar el operador módulo %).

# Para saber si un número es par, debemos verificar el residuo de dividirlo entre $2$.
# Si el residuo es igual a 0 (numero % 2 == 0), el número es par.

numero = 3

if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")


#** ====================================================*##

 # *            Ejercicio 3: Condicional Anidado (if dentro de otro if)
# Crea un programa que verifique si una persona puede votar.
# Primero, debe evaluar si la persona tiene 18 años o más
# Si cumple la edad,  debe evaluar una segunda condición:
# si tiene su documento_identidad en regla (usando una variable booleana True o False). 
# Si lo tiene, imprime "Puede votar". Si no lo tiene, imprime "No puede votar por falta de documento"
# Si de entrada no tiene 18 años o más, debe imprimir "No tiene la edad mínima para votar".


edad = 15
documento_identidad = True

# Primer if (Evaluación de edad)
if edad >= 18:
    # Segundo if anidado (Evaluación de documento)
    if documento_identidad:
        print("Puede votar")
    else:
        print("No puede votar por falta de documento")
else:
    print("No tiene la edad mínima para votar")

# **=============================================**#

#*       Ejercicio 4: Condicional Múltiple (if-elif-else)
# Crea un sistema de calificación escolar según la nota asignada a una variable nota (valor entre 0 y 10):
# ? Si la nota es mayor o igual a 9:  Imprime "Excelente".
# ? Si la nota es mayor o igual a 7 y menor que 9: Imprime "Bueno"
# ? Si la nota es mayor o igual a 5 y menor que 7: Imprime "Aprobado".
# ? En cualquier otro caso (menor a 5): Imprime "Reprobado".


Calificacion = 10

if Calificacion >= 9:
    print("Excelente")
elif Calificacion >= 7:
    print("Bueno")
elif Calificacion >= 5:
    print("Aprobado")
else:
    print("Reprobado")

#*=============================================================*#

# *         Ejercicio 5: Operador Ternario
# Dado el valor de una variable edad (por ejemplo, edad = 20),
# utiliza una sola línea de código (operador ternario)
# para asignar a la variable estado la palabra "Mayor de edad"
# si edad >= 18, o "Menor de edad" en caso contrario. 
# Luego, imprime la variable estado.

edad = 20

if edad >=18: 
    estado = "Mayor_de_edad" 
else:
    estado = "Menor_de_edad"

estado = "Mayor_de_edad" if edad >= 18 else "Menor_de_edad"
print (estado)








