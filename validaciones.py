from datetime import datetime

def validacion_nombre():
    nombre = input("Nombre del proyecto: ")
    nombre_sin_espacios = nombre.replace(' ', '')
    while nombre_sin_espacios.isalpha() == False or len(nombre) > 30:
        print('\nIngrese un nombre válido.')
        nombre = input("Nombre del proyecto: ")
        nombre_sin_espacios = nombre.replace(' ', '')
    return nombre


def validacion_fecha(fecha_inicio, fecha_fin):
    if fecha_inicio > fecha_fin:
        return False
    else: 
        return True

def validacion_presupuesto(presupuesto):
    presupuesto_sin_puntos = presupuesto.replace('.','')
    while presupuesto_sin_puntos.isnumeric() == False:
        print('\nNo ha ingresado numero  válido.\n')
        presupuesto = input("Vuelva a ingresar un presupuesto: $").replace(',', '')
        presupuesto_sin_puntos = presupuesto.replace('.','')
    presupuesto = float(presupuesto)
    return presupuesto

def valiadcion_fecha_de_inicio():
    
    bandera_fecha = False
    while bandera_fecha == False:
        fecha_inicio_input = input("Fecha de inicio (dd/mm/aaaa): ")
        if len(fecha_inicio_input) == 10 and fecha_inicio_input[2] == '/' and fecha_inicio_input[5] == '/':
            dia = fecha_inicio_input[:2]
            mes = fecha_inicio_input[3:5]
            año = fecha_inicio_input[6:]
            if dia.isdigit() and mes.isdigit() and año.isdigit():
                dia = int(dia)
                mes = int(mes)
                año = int(año)
                if 1 <= dia <= 31 and 1 <= mes <= 12 and año < 10000:
                    fecha_inicio = datetime(año, mes, dia)
                    bandera_fecha = True
                else:
                    print("Fecha no válida. Por favor, usa una fecha real.")
            else:
                print("Formato de fecha incorrecto. Por favor, usa el formato dd/mm/aaaa.")
        else:
            print("Formato de fecha incorrecto. Por favor, usa el formato dd/mm/aaaa.")
    return fecha_inicio

def valiadcion_fecha_de_fin():
    bandera_fecha = False
    while bandera_fecha == False:
        fecha_fin_input = input("Fecha de fin (dd/mm/aaaa): ")
        if len(fecha_fin_input) == 10 and fecha_fin_input[2] == '/' and fecha_fin_input[5] == '/':
            dia = fecha_fin_input[:2]
            mes = fecha_fin_input[3:5]
            año = fecha_fin_input[6:]
            if dia.isdigit() and mes.isdigit() and año.isdigit():
                dia = int(dia)
                mes = int(mes)
                año = int(año)
                if 1 <= dia <= 31 and 1 <= mes <= 12 and año < 10000:
                    fecha_fin = datetime(año, mes, dia)
                    bandera_fecha = True
                else:
                    print("Fecha no válida. Por favor, usa una fecha real.")
            else:
                print("Formato de fecha incorrecto. Por favor, usa el formato dd/mm/aaaa.")
        else:
            print("Formato de fecha incorrecto. Por favor, usa el formato dd/mm/aaaa.")
    return fecha_fin