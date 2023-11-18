#Programa para identificar tipos de datos
#Por: Melania Valdez
# Ingreso de datos
cedula = (input('Ingrese su número de cédula: '))

print(cedula)

nombres = (input('Ingrese su apellido y nombre: '))
direccion = (input('Ingrese su dirección: '))
sueldo = float(input ('Ingrese su sueldo: '))
horas_extras = int(input('Ingrese el número de horas extras: '))
costo_hora_extra = int(input('Ingrese el costo de la hora extra: '))
valortotal_he = horas_extras * costo_hora_extra
bonificacion = int(input('Ingrese el valor por bonificaciones: '))
valores = [sueldo,valortotal_he, bonificacion]
print('Ingrese las cargas familiares: ')
esposa = (input('Ingrese el nombre del cónyuge: '))
hijo1 = (input('Ingrese el nombre del hijo 1: '))
hijo2 = (input('Ingrese el nombre del hijo 2: '))
hijo3 = (input('Ingrese el nombre del hijo 3: '))
cargas_familiares = { esposa, hijo1, hijo2, hijo3}
#Presentación de datos
print('PRESENTACIÓN DE DATOS')
print('Cédula:', cedula)
print('Apellidos y nombres:', nombres)
print('Dirección:', direccion)
print('Los valores de sus ingresos son:', valores)
print('Cargas familiares:', cargas_familiares)
