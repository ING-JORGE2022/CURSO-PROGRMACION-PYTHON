# Taller 1
# No de Identificación, Nombres, Apellidos, Dirección, Teléfono, Edad, Estado Civil,
# Número de hijos, Estatura en centímetros, fecha de contratación (Día/mes/año), Sueldo básico, Días Laborados.

# ////////////////// solucion #1

# numeroId = ("107062892")
# nombre = ("Pepito")
# apellido = ("perez")
# direccion = ("Calle 1 - 2b barrio la fuente de ")
# telefono = ( 31181568915)
# edad = (24)
# estadocivil = (" soltero")
# numeDeHijos = (1)
# estatura = (1,70)
# fechaContratacion =( "4 / 11 / 2022")
# sueldo = ("$ 1.200.000")
# diasLaborados = (5)

# ////////////////////////////////// solucion #2
# numeroId = input(" DIGITE EL NUMERO DE INDETIFICACION : ")
# nombre = input ("Digite su Nombre : ")
# apellido = input ("Digite su apellido :  ")
# direccion = input ("Digite su direccion :  ")
# telefono = input ( "Digite el telefono :")
# edad = input ("Digite su edad : ")
# estadocivil = input ("Digite el estado civil : ")
# numeDeHijos = input ("Digite el numero de hijos : ")
# estatura = input ("Diguite su estatura : ")
# fechaContratacion =input ( "Diguite la fecha de contratacion : ")
# sueldo = input ("DIGUITE EL SUELODO : ")
# diasLaborados = input ("diguire cuantos dias estubo : ")

# # imprimir valores
# print(numeroId)
# print(nombre)
# print(apellido)
# print(direccion)
# print(telefono)
# print(edad)
# print(estadocivil)
# print(numeDeHijos)
# print(estatura)
# print(fechaContratacion)
# print(diasLaborados)



# Taller 2:

# Dando continuidad con la primera entrega del proyecto, en esta oportunidad el estudiante debe realizar las siguientes
# validaciones utilizando la sentencia condicional IF.

# Si el empleado es mayor de 55 años disfrutará de un bono de prepensión correspondiente al 5% de su sueldo básico.

# Si el empleado es casado y tiene hijos se le otorgará un paseo cada diciembre

# Si el sueldo básico está entre 1000000 y 1500000 tendrá una comisión del 2% sobre el valor del sueldo;
# Si el sueldo básico está entre 1500001 y 2000000 tendrá una comisión del 5% sobre el valor del sueldo;
# para todos los demás casos no habrá comisión.

# Si el empleado trabajó más de 20 días al mes y su sueldo es menor a 1000000 tendrá derecho a un bono de alimentación.

# Definir las variables
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
estado_civil = input("Ingrese su estado civil (soltero/casado): ")
tiene_hijos = input("¿Tiene hijos? (si/no): ")
sueldo_basico = float(input("Ingrese su salario básico: $"))
dias_trabajados = int(input("Ingrese el número de días trabajados en el mes: "))

# VALIDACION DE BONO DE PESIONES 
if edad >= 55:
   bono = sueldo_basico * 0.05
   total = bono + sueldo_basico
   print(f"Felicidades, {nombre} ha adquirido un BONO de pensión de ${bono:,.2f}. Por lo tanto, su sueldo total será de ${total:,.2f}")
else:
   print(f"{nombre}, usted no cumple con los requisitos para obtener el BONO de pensión")

# VALIDACION DE PASEO 

if estado_civil == "casado" and tiene_hijos == "si" :
   print(f"felicidades {nombre} te  ganaste un paseo para que disfurtes con tu familia para  la fecha de DICIEMBRE")
else : print (f"lo siento {nombre} no cumples con los requisitos para otorgarte el paseo ")

# Validación de la comisión según el rango del sueldo básico
if sueldo_basico >= 1000000 and sueldo_basico <= 1500000:
    comision = sueldo_basico * 0.02
    sueldo_total = sueldo_basico + comision
    print(f"{nombre}, su comisión es del 2% sobre el valor del sueldo, por lo tanto su sueldo total será de ${sueldo_total:,.2f}")
elif sueldo_basico > 1500000 and sueldo_basico <= 2000000:
    comision = sueldo_basico * 0.05
    sueldo_total = sueldo_basico + comision
    print(f"{nombre}, su comisión es del 5% sobre el valor del sueldo, por lo tanto su sueldo total será de ${sueldo_total:,.2f}")
else:
    print(f"{nombre}, usted no tiene derecho a comisión")
    
        # Validación del bono de alimentación para empleados con sueldo menor a 1000000 y más de 20 días trabajados
if dias_trabajados > 20 and sueldo_basico < 1000000:
    bono_alimentacion = 20000 * dias_trabajados
    sueldo_total = sueldo_basico + bono_alimentacion
    print(f"{nombre}, por trabajar más de 20 días al mes y tener un sueldo menor a $1,000,000, se le otorgará un bono de alimentación de ${bono_alimentacion:,.2f}. que lo puedes redimir en supermercados de cadena o se agregara a la nomina, Por lo tanto, su sueldo total será de ${sueldo_total:,.2f}")

print("codigo finalizado........")
print ("Realizado por Jorge sarmiento romero TALLER #2  ")