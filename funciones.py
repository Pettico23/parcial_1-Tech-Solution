from datetime import datetime
import json
import os
from parseado import *
from validaciones import*
import time

def agregar_proyecto(proyectos): #gestionar una lista de hasta 50 proyectos activos
    numero_de_activos = 0
    for proyecto in proyectos:
        if proyecto['Estado'] == 'Activo':
            numero_de_activos += 1
    
    if numero_de_activos >= 50: #Si se alcanza el límite de 50 proyectos activos, se deberá notificar al usuario.
        print('\nSe ha alcanzado la máxima cantidad de proyectos activos') #1 consideracion
        return False
    
    if proyectos:
        max_id = 0
        for p in proyectos:
            if p['id'] > max_id:
                max_id = p['id'] # ID INCREMENTAL
            nuevo_id = max_id + 1
    else:
        nuevo_id = 1
    
    nombre = validacion_nombre()  #VALIDACION NOMBRE
    nombre = nombre.capitalize()
    descripcion = input("Descripción: ")

    while len(descripcion) > 200: #Descripción: Debe ser un texto alfanumérico de no más de 200 caracteres.
        print('\nIngrese una descripción más corta.') 
        descripcion = input("Descripción: ")
    
    fecha_inicio = valiadcion_fecha_de_inicio() #VALIDACION FECHA: Fecha de Inicio y Fecha de Fin: Deben ser fechas válidas en el formato "DD/MM/AAAA"
    fecha_fin = valiadcion_fecha_de_fin()       

    if validacion_fecha(fecha_inicio, fecha_fin) == False:               #La Fecha de Fin no puede ser anterior a la Fecha de Inicio.
        print('\nLa fecha de inicio debe ser anterior a la fecha de fin.\n')
        return False
    
    presupuesto = input("Presupuesto: $").replace(',', '') #Presupuesto: Debe ser un valor numérico entero no menor a $500000.
    presupuesto = validacion_presupuesto(presupuesto)
    presupuesto = float(presupuesto)

    while presupuesto < 500000:

        print('El presupuesto ingresado no supera el mínimo esperado.')
        presupuesto = input("Presupuesto: $").replace(',', '')
        presupuesto = validacion_presupuesto(presupuesto)
        presupuesto = float(presupuesto)
    
    estado = "Activo"
    
    nuevo_proyecto = {
        'id': nuevo_id,
        'Nombre del Proyecto': nombre,
        'Descripción': descripcion,
        'Fecha de inicio': fecha_inicio,
        'Fecha de Fin': fecha_fin,
        'Presupuesto': presupuesto,
        'Estado': estado
    }
    
    proyectos.append(nuevo_proyecto)
    print("\nProyecto agregado exitosamente.\n")


def modificar_proyecto(proyectos, id_proyecto):
    id_bandera = True
    for proyecto in proyectos:
        if str(proyecto['id']) == id_proyecto:
            id_bandera = False
            while True:
                print("\n¿Qué datos desea modificar?")
                print("1. Nombre del Proyecto")
                print("2. Descripción")
                print("3. Fecha de Inicio")
                print("4. Fecha de Fin")
                print("5. Presupuesto")
                print("6. Estado")
                print("7. Salir")
                
                opcion = input("Ingrese su opción: ")
                
                if opcion == "1":
                    nuevo_nombre = input("Ingrese el nuevo nombre del proyecto: ")
                    proyecto['Nombre del Proyecto'] = nuevo_nombre
                
                elif opcion == "2":
                    nueva_descripcion = input("Ingrese la nueva descripción del proyecto: ")
                    proyecto['Descripción'] = nueva_descripcion
                
                elif opcion == "3":
                    nueva_fecha_inicio = input("Ingrese la nueva fecha de inicio (DD/MM/AAAA): ")
                    proyecto['Fecha de inicio'] = datetime.strptime(nueva_fecha_inicio, '%d/%m/%Y')
                
                elif opcion == "4":
                    nueva_fecha_fin = input("Ingrese la nueva fecha de fin (DD/MM/AAAA): ")
                    proyecto['Fecha de Fin'] = nueva_fecha_fin
                    proyecto['Fecha de Fin'] = datetime.strptime(nueva_fecha_fin, '%d/%m/%Y')
                
                elif opcion == "5":
                    nuevo_presupuesto = input("Ingrese el nuevo presupuesto: ")
                    proyecto['Presupuesto'] = nuevo_presupuesto
                
                elif opcion == "6":
                    nuevo_estado = input("Ingrese el nuevo estado (Activo/Cancelado/Finalizado): ")
                    proyecto['Estado'] = nuevo_estado
                
                elif opcion == "7":
                    break
                
                else:
                    print("Opción no válida. Por favor, ingrese un número de opción válido.")
    if id_bandera:
        print('\nID no encontrada.\n')


def cancelar_proyecto(proyectos, id_proyecto):
    id_existe = False
    for proyecto in proyectos:
        
        if proyecto['id'] == id_proyecto:
            if proyecto['Estado'] == 'Cancelado' or proyecto['Estado'] == 'Finalizado':
                print('Este proyecto ya fue cancelado/finalizado.')
                id_existe = True
            else:
                proyecto['Estado'] = 'Cancelado'
                print("El proyecto ha sido cancelado exitosamente.")
                id_existe = True

        
    if id_existe == False: 
        print("El proyecto con ese ID no fue encontrado.")


def comprobar_proyectos(proyectos):
    fecha_actual = datetime.now()
    for proyecto in proyectos:
        fecha_de_fin = proyecto['Fecha de Fin']
        if proyecto["Estado"] != "Cancelado":
            if fecha_de_fin <= fecha_actual:
                proyecto['Estado'] = 'Finalizado'
            
    print('\nLos proyectos han sido comprobados.\n')


def mostrar_todo(proyectos):
    
    encabezado = "| {:^33} | {:^54} | {:^17} | {:^15} | {:^12} | {:^10} |"
    print(encabezado.format("Nombre del Proyecto", "Descripción", "Presupuesto", "Fecha de Inicio", "Fecha de Fin", "Estado"))
    
    print("-" * 160)

    for proyecto in proyectos:
        
        presupuesto = proyecto['Presupuesto']
        presupuesto = f"${presupuesto:,.2f}"
        
        descripcion = proyecto['Descripción']
        if len(descripcion) > 50:
            descripcion = proyecto['Descripción'][:50] + '...'
        
        nombre = proyecto["Nombre del Proyecto"]
        if len(nombre) > 30:
            nombre = proyecto["Nombre del Proyecto"][:30] + '...'

        fila = "| {:^33} | {:^34} | {:^17} | {:^15} | {:^12} | {:^10} |".format(
            nombre, descripcion, presupuesto,
            proyecto["Fecha de inicio"].strftime("%d/%m/%Y"), proyecto["Fecha de Fin"].strftime("%d/%m/%Y"), proyecto["Estado"])
        print(fila)


def presupuesto_promedio(proyectos):
    presupuesto_total = 0
    contador = 0
    
    for proyecto in proyectos: 
        contador += 1
        presupuesto_total += proyecto['Presupuesto']
    
    promedio = presupuesto_total / contador
    print(f"\nEl presupuesto promedio es ${promedio:,.2f}\n")


def buscar_por_nombre(nombre, proyectos):
    proyecto_encontrado = False
    for proyecto in proyectos:
        nombre_proyecto = proyecto['Nombre del Proyecto'].lower()
        if nombre_proyecto == nombre:
            print('- - - -')
            print(f'Nombre del proyecto: {proyecto["Nombre del Proyecto"]}')
            print(f'Descripción: {proyecto["Descripción"]}')
            print(f'Fecha de inicio: {proyecto["Fecha de inicio"].strftime("%d/%m/%Y")}')
            print(f'Fecha de fin: {proyecto["Fecha de Fin"].strftime("%d/%m/%Y")}')
            print(f'Presupuesto: ${proyecto["Presupuesto"]:,.2f}')
            print(f'Estado: {proyecto["Estado"]}')
            print('- - - -')
            proyecto_encontrado = True
            break
    if proyecto_encontrado == False:
        print('Proyecto no encontrado')


def retomar_proyecto(proyectos, id_proyecto):
    id_existe = False
    validacion_bandera = True
    for proyecto in proyectos:
        
        if proyecto['id'] == id_proyecto:
            
            id_existe = True

            if proyecto['Estado'] == 'Finalizado':
                print('\nEste proyecto ya fue finalizado\n.')
            elif proyecto['Estado'] == 'Activo':
                print('\nEste proyecto no fue cancelado.\n')
            else:
                fecha_inicio = proyecto['Fecha de inicio']
                fecha_final = proyecto['Fecha de Fin']
                
                if fecha_inicio > fecha_final:
                    print('\nLa fecha de inicio es mayor a la fecha final.\n')
                    validacion_bandera = False

                if len(proyecto['Descripción']) > 200:
                    print('\nLa descripcion es demasiado larga.\n')
                    validacion_bandera = False

                if proyecto['Presupuesto'] < 500000:
                    print('\nEl presupuesto es menor al esperado.\n')
                    validacion_bandera = False

                if validacion_bandera:
                    proyecto['Estado'] = 'Activo'
                    print("\nEl proyecto ha sido activado exitosamente.\n")       
        
    if id_existe == False: 
        print("El proyecto con ese ID no fue encontrado.")


def reporte_presupuesto(presupuesto, proyectos):
    reporte = []
    fecha_solicitud = datetime.now().strftime("%d%m%Y")
    
    for proyecto in proyectos:
        if proyecto['Presupuesto'] > presupuesto:
            reporte.append((proyecto['id'], proyecto['Nombre del Proyecto'], proyecto['Presupuesto']))

    cantidad_proyectos = len(reporte)
    
    numero_de_reportes = 1
    archivo = f"reporte_presupuesto_{numero_de_reportes}.txt"

    while os.path.exists(archivo):
        numero_de_reportes += 1
        archivo = f"reporte_presupuesto_{numero_de_reportes}.txt"

    with open(archivo, 'w', encoding='utf-8') as file:
        fecha_solicitud = datetime.now().strftime("%d/%m/%Y")
        file.write(f"Cantidad de reportes hasta la fecha: {numero_de_reportes}\n")
        file.write(f"Fecha de Solicitud: {fecha_solicitud}\n")
        file.write(f"Cantidad de Proyectos: {cantidad_proyectos}\n")
        file.write("\nListado de Proyectos:\n")
        for proyecto in reporte:
            file.write(f"id: {proyecto[0]}, {proyecto[1]}, ${proyecto[2]:,.2f}\n")
    
    print(f'Reporte guardado como: {archivo}')

    return reporte


def reporte_proyecto(proyectos,proyecto_a_buscar):
    fecha_solicitud = datetime.now().strftime("%d%m%Y")
    numero_de_reportes = 1
    archivo = f"reporte_proyecto_{numero_de_reportes}.txt"

    while os.path.exists(archivo):
        numero_de_reportes += 1
        archivo = f"reporte_proyecto_{numero_de_reportes}.txt"
    
    nombre_existe = False
    
    for proyecto in proyectos:
        
        nombre_proyecto = proyecto['Nombre del Proyecto']
        
        if proyecto_a_buscar.lower() == nombre_proyecto.lower():
            
            nombre_existe = True

            with open(archivo, 'w', encoding='utf-8') as file:
                fecha_solicitud = datetime.now().strftime("%d/%m/%Y")
                file.write(f"Cantidad de reportes hasta la fecha: {numero_de_reportes}\n")
                file.write(f"Fecha de Solicitud: {fecha_solicitud}\n")
                file.write("\nProyecto:\n")                
                    
                proyecto['Fecha de inicio'] = proyecto['Fecha de inicio'].strftime('%d/%m/%Y')
                proyecto['Fecha de Fin'] = proyecto['Fecha de Fin'].strftime('%d/%m/%Y')
                proyecto['Presupuesto'] = f"${proyecto['Presupuesto']:,.2f}"
                    
                file.write(f"{proyecto['id']}, ")
                file.write(f"{proyecto['Nombre del Proyecto']}, ")
                file.write(f"{proyecto['Descripción']}, ")
                file.write(f"{proyecto['Fecha de inicio']}, ")
                file.write(f"{proyecto['Fecha de Fin']}, ")
                file.write(f"{proyecto['Presupuesto']}, ")
                file.write(f"{proyecto['Estado']}")
                file.write("\n")
    
                print(f'Reporte guardado como: {archivo}')
                    
    if nombre_existe == False:
        print('Ese proyecto no existe.')


def proyectos_finalizados(proyectos):
    lista_proyectos_finalizados = []
    
    for proyecto in proyectos:
        if proyecto['Estado'] == 'Finalizado': 
            lista_proyectos_finalizados.append(proyecto)
            
    return lista_proyectos_finalizados


def proyectos_finalizados_json(proyectos):
    finalizados = proyectos_finalizados(proyectos)
    with open('ProyectosFinalizados.json', 'w', encoding='utf-8', newline = '' ) as file:
        json.dump(finalizados, file, indent=4, ensure_ascii=False)

def p_proyectos_finalizados_menos_3_años(proyectos):
    contador = 0
    bandera_proyecto_encontrado = False
    
      
    for proyecto in proyectos:
        tres_años = False
        if proyecto['Estado'] == 'Finalizado':
            fecha_inicio = proyecto['Fecha de inicio']
            fecha_fin = proyecto['Fecha de Fin']

            if fecha_inicio.year + 3 > fecha_fin.year:
                    tres_años = True
            if fecha_inicio.year + 3 >= fecha_fin.year:
                if fecha_inicio.month > fecha_fin.month:
                    tres_años = True
                if fecha_inicio.month == fecha_fin.month:
                    if fecha_inicio.day >= fecha_fin.day:
                        tres_años = True
        if   tres_años == True:
            contador += 1
            bandera_proyecto_encontrado = True
            if contador == 1:
                print('- - - -')
            print(f'ID: {proyecto["id"]}')
            print(f'Nombre del proyecto: {proyecto["Nombre del Proyecto"]}')
            print(f'Descripción: {proyecto["Descripción"]}')
            print(f'Fecha de inicio: {proyecto["Fecha de inicio"].strftime("%d/%m/%Y")}')
            print(f'Fecha de fin: {proyecto["Fecha de Fin"].strftime("%d/%m/%Y")}')
            print(f'Presupuesto: ${proyecto["Presupuesto"]:,.2f}')
            print(f'Estado: {proyecto["Estado"]}')
            print('- - - -') 
            
            time.sleep(4)
                
            
    if bandera_proyecto_encontrado == False:
        print("Proyecto menor de 3 años no encontado") 
           
            
            
    
    

def r_presupuesto_de_proyecto_activo_que_contiene_desarrollo(proyectos):
    bandera_proyecto = True
    for proyecto in proyectos:
        
        if proyecto['Estado'] == 'Activo':
            if 'Desarrollo' in proyecto['Descripción'] or 'desarrollo' in proyecto['Descripción']:
                
                presupuesto = proyecto['Presupuesto']
                
                print(proyecto['Nombre del Proyecto'])
                print(f'${presupuesto:,.2f}\n')
                bandera_proyecto = False
    if bandera_proyecto:
        print("No se encontro ningun proyecto con la palabra Desarrollo")
        
        