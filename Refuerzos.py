# 1) Un vendedor recibe un sueldo base más un 10% extra por
# comisión de sus ventas, el vendedor desea saber cuánto
# dinero obtendrá por concepto de comisiones por las tres
# ventas que realiza en el mes y el total que recibirá en
# el mes tomando en cuenta su sueldo base y comisiones.

# solucion 

# sueldo_base = float(input("Ingrese el sueldo base del vendedor: "))
# venta1 = float(input("Ingrese la primera venta del mes: "))
# venta2 = float(input("Ingrese la segunda venta del mes: "))
# venta3 = float(input("Ingrese la tercera venta del mes: "))

# comision = (venta1 + venta2 + venta3) * 0.1
# total_mes = sueldo_base + comision

# print(f"La comisión obtenida por las tres ventas es de: {comision}")
# print(f"El vendedor recibirá en el mes un total de: {total_mes}")


# 2) Una tienda ofrece un descuento del 15% sobre el total
# de la compra y un cliente desea saber cuánto deberá
# pagar finalmente por su compra.

# precio_total = float(input("Ingrese el precio total de la compra: "))
# descuento = 0.15 * precio_total
# precio_final = precio_total - descuento
# print(f"El precio final con descuento es: {precio_final:.2f}")


# 3) Un alumno desea saber cuál será su calificación final en
# la materia de Algoritmos. Dicha calificación se compone
# de tres exámenes parciales.
# nombre_estudiante = (input("Escriba su nombre para resgistrarlo y dar su  nota definitiva : "))
# cal1 = float(input("Digite la calificación 1: "))
# cal2 = float(input("Digite la calificación 2: "))
# cal3 = float(input("Digite la calificación 3: "))

# # prom = round((cal1 + cal2 + cal3)/3, 2)

# # print(f"Estudiante {nombre_estudiante} El promedio es= {prom}")
# # Pedimos al usuario que ingrese el número de hombres y mujeres
# num_hombres = int(input("Ingrese el número de hombres: "))
# num_mujeres = int(input("Ingrese el número de mujeres: "))

# # Calculamos el total de estudiantes y los porcentajes de hombres y mujeres
# total_estudiantes = num_hombres + num_mujeres
# porcentaje_hombres = (num_hombres / total_estudiantes) * 100
# porcentaje_mujeres = (num_mujeres / total_estudiantes) * 100

# # Mostramos los resultados
# print(f"Porcentaje de hombres: {porcentaje_hombres:.2f}%")
# print(f"Porcentaje de mujeres: {porcentaje_mujeres:.2f}%")



# /////////////////////////////////////////////////// refuerzo ciclo for 

#1 Crear un bucle que cuente todos los números pares hasta
# el 100 ciclo for


#2 Haz una tabla de multiplicar utilizando el ciclo for
# ciclo for

# num = int(input("Digite el número de la tyabla de multiplicar: "))
# for i in range(11):
#   print(i, " x ", num , " = ", i * num  )


# 3. Escribir un programa que pregunte al usuario su edad y
# muestre por pantalla todos los años que ha cumplido
# (desde 1 hasta su edad). ciclo for

# edad = int(input("ingrese su edad actual : "  ) )

# for i in range ( 1, edad ):
#     print (i , "años" )

# 4. Escribir un programa que pida al usuario un número entero
# positivo y muestre por pantalla todos los números
# impares desde 1 hasta ese número separados por comas.

# Definir una lista de números
# numeros = int(input("Imgrese un numero entero positivo : "))

# Recorrer la lista y mostrar los números impares
# for i in  range (numeros):
#     if i % 2 != 0:
#          print(i, end=", ")


# 5. Encuentra la suma de todos los números pares del 1 al
# 100 ciclo for
# suma = 0
# for i in range(2, 101, 2):
#     suma += i
# print("La suma de todos los números pares del 1 al 100 es:", suma)

# # otra forma 


# # variable acumuladora
# acu = 0

# for i in range(0,101,2):
#   acu = acu + i
# print(f"El total de la suma de los números pares del 0-100= {acu}")